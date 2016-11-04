from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator
from django.views import View

from blog.forms import BlogForm
from blog.models import Blog, VISIBILITY_PUBLIC, VISIBILITY_PRIVATE
from blog.util import generate_responsive_images
from categorias.models import Category
from django.utils.translation import ugettext as _


class HomeRedirect(View):
    def get(self, request):
        """
        Reedirecciona al Blogs
        :param request:
        :return:
        """
        return redirect('blogs/')


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con un listado de los blogs.
        si el usuario no se encuentra autentificado solo podra ver los posts publicos.
        si el usuario si se encuentra autentificado podra ver toso los posts publicos y privados donde sea propietario.

        :param request: objeto HttpRequest con los datos de la peticion
        :return: objecto HttpResponse con los datos de la respuesta
        """

        categorys_totals = Category.objects.all()

        categoria = request.GET.get('category')
        hoy = datetime.today()
        blogs = Blog.objects.all().select_related('owner').filter(datePub__lte=hoy).order_by('-datePub')

        blogs = BlogQueryset.get_posts_by_user(blogs, request.user)

        if categoria is not None:

            object_category = get_object_or_404(Category, name=categoria)
            blogs = blogs.filter(type=object_category)

        # agrego busqueda de posts por titulo del post o contenido en el body
        search = request.GET.get('search')
        if search is not None:
            blogs = blogs.filter(Q(title__contains=search) | Q(body__contains=search) | Q(intro__contains=search))

        context = {'blogs_list': blogs, 'category_list': categorys_totals}

        return render(request, 'blog/list_posts.html', context)


class HomeUserView(View):

    def get(self, request, user):
        """
        Renderiza el home con un listado de los blogs.
        si el usuario

        :param request: objeto HttpRequest con los datos de la peticion
        :return: objecto HttpResponse con los datos de la respuesta
        """
        categorys_totals = Category.objects.all()
        user_object = get_object_or_404(User, username=user)
        blogs = Blog.objects.all().filter(owner=user_object)
        if request.user.is_authenticated:
            blogs = blogs.order_by('-created_at').select_related('owner')
        else:
            blogs = blogs.filter(datePub__lte=datetime.today()).order_by('-datePub').filter(visibility=VISIBILITY_PUBLIC)

        context = {'blogs_list': blogs, 'category_list': categorys_totals, 'homeUser': True, 'usuario': user_object}
        return render(request, 'users/profile.html', context)


class BlogQueryset(object):

    @staticmethod
    def get_posts_all():
        possible_photos = Blog.objects.all().select_related("owner")
        return possible_photos

    @staticmethod
    def get_posts_by_user(queryset, user):
        if not user.is_authenticated:
            return queryset.filter(visibility=VISIBILITY_PUBLIC)
        elif user.is_superuser:
            return queryset
        else:
            return queryset.exclude(Q(visibility=VISIBILITY_PRIVATE) & ~Q(owner=user))


class DetailView(View):
    @method_decorator(login_required())
    def get(self, request, pk, user):
        """
        Renderiza el detalle del post de un usuario espesifico.
        :param request:
        :return:
        """
        user_object = get_object_or_404(User, username=user)  # consulta al usuario a actualizar.

        blogs = BlogQueryset.get_posts_by_user(Blog.objects.all().filter(pk=pk, owner=user_object), request.user)

        if len(blogs) == 0:
            return HttpResponseNotFound(_("El blog que buscas no existe"))
        elif len(blogs) > 1:
            return HttpResponse("Multiples Opciones", status=300)

        post = blogs[0] if len(blogs) > 0 else None
        categorias = Category.objects.all()
        context = {'post': post, 'category_list': categorias}

        return render(request, 'blog/detail.html', context)
        # return HttpResponse('/blog/detail.html')


class CrearPostView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Renderiza la plantilla para crear un post y publicarlo.
        :param request:
        :return:
        """
        message = ""
        blog_form = BlogForm()
        categorias = Category.objects.all()
        context = {'form': blog_form, 'message': message, 'category_list': categorias}
        return render(request, 'blog/create_post.html', context)

    def post(self, request):
        """
        Presenta el formulario para crear una foto y en caso de que la peticion sea post, la valida y la crea en caso de que
        sea valida.
        :param request:
        :return:
        """

        message = ""
        post_with_user = Blog(owner=request.user)
        post_form = BlogForm(request.POST, request.FILES, instance=post_with_user)

        if post_form.is_valid():

            new_post = post_form.save()
            generate_responsive_images(new_post)
            post_form = BlogForm()  # limpia los campos para que se pueda crear una nueva foto.
            mes = _("Post creado satisfactoriamente. Ver post: ")
            message = "{2}<a href='/../blogs/{0}/{1}'>POST</a>".format(request.user.username, new_post.pk, mes, )
        categorias = Category.objects.all()
        context = {'form': post_form, 'message': message, 'category_list': categorias}
        return render(request, 'blog/create_post.html', context)
