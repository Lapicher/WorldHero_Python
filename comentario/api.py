from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blog.models import Blog
from blog.util import find_hashtags, send_mail
from comentario.models import Comment
from comentario.serializer import CommentListSerializer, CommentSerializer


class CommentViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    # search_fields = ('owner', 'text', )
    # order_fields = ('-created_at', )
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter, )


    def get_queryset(self):

        """
        blogs = Blog.objects.all().select_related("owner").order_by('-datePub')

        if self.request.user.is_superuser:
            # como administrador obtiene todos los posts.
            return blogs
        elif self.request.user.is_authenticated():
            # no obtiene los posts que esten privados de otros usuarios. y solo los publicados hasta al dia de hoy.
            blogs = blogs.filter(datePub__lte=datetime.today())
            return blogs.exclude(Q(visibility=VISIBILITY_PRIVATE) & ~Q(owner=self.request.user))

        else:
            # invitado prodra ver los posts publicos.
            return blogs.filter(datePub__lte=datetime.today(), visibility=VISIBILITY_PUBLIC)
        """
        datos = self.request.data;
        comments = Comment.objects.all()
        total = len(comments)
        return comments

    # se comenta la linea anterior para permitir al metodo siguiente seleccionar que serializador escoger.
    def get_serializer_class(self):

        if self.action != 'list':
            serializador = CommentSerializer
        else:
            serializador = CommentListSerializer

        return serializador


    # metodo que nos sirve para crear la foto con el propietario que se logueo en la API.

    def perform_create(self, serializer):

        datos = self.request.data;
        id_blog = datos.get('idArticle')
        texto = datos.get('message')
        userBlog= datos.get('userArticle')

        blog = Blog.objects.filter(pk=id_blog)
        user = User.objects.filter(username=userBlog)

        commentario = serializer.save(owner=user[0], blog=blog[0], text=texto)

        # busca en el titulo, cabecera, cuerpo del post un usuario mencionado por hashtag para notificarle de la
        # mencion.
        users = find_hashtags('{0}'.format(texto))
        list_emails = []
        for username in users:
            usuario = User.objects.filter(username=username)
            if len(usuario) > 0 and usuario[0].email is not None:
                list_emails.append(usuario[0].email)

        # elimina elementos repetidos de la lista
        lst2 = []
        for key in list_emails:
            if key not in lst2:
                lst2.append(key)
        list_emails = lst2

        # reenvio notificacion a todos los usuarios mencionados en el post.
        for email in list_emails:
            mailOptions = {
                'from': '"WoldHero" <notifications@worldhero.com>',
                'to': email,  # list of receivers
                'subject': 'Hello, You have been mentioned in a comment✔',  # Subject line
                'text': 'Hello world ?',  # plaintext body
                'html': '<b>Estimado Usuario, te avisamos que has sido mencionado en un comentario. ver</b>'  # html body
            }
            send_mail.delay(mailOptions)


        return commentario


