from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from blog.models import Blog
from categorias.models import Category


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

        :param request: objeto HttpRequest con los datos de la peticion
        :return: objecto HttpResponse con los datos de la respuesta
        """

        categorys_totals = Category.objects.all()

        categoria = request.GET.get('category')
        if categoria is None:

            blogs = Blog.objects.all().order_by('-created_at').select_related('owner')

        else:
            object_category = get_object_or_404(Category, name=categoria)
            blogs = Blog.objects.filter(type=object_category).order_by('-created_at')

        context = {'blogs_list': blogs[:4], 'category_list': categorys_totals}

        return render(request, 'blog/index.html', context)


class HomeUserView(View):
    def get(self, request, user):
        """
        Renderiza el home con un listado de los blogs.

        :param request: objeto HttpRequest con los datos de la peticion
        :return: objecto HttpResponse con los datos de la respuesta
        """
        categorys_totals = Category.objects.all()
        user_object = get_object_or_404(User, username=user)
        blogs = Blog.objects.all().order_by('-created_at').select_related('owner').filter(owner=user_object)
        context = {'blogs_list': blogs[:4], 'category_list': categorys_totals}
        return render(request, 'blog/index.html', context)


class BlogQueryset(object):

    @staticmethod
    def get_posts_by_user(user):
        possible_photos = Blog.objects.all().select_related("owner")
        """
        if not user.is_authenticated():
            possible_photos = possible_photos.filter(visibility=VISIBILITY_PUBLIC)
        else:
            # query mas avanzada es como decir en sql: visibility='public' or owner='usuario'
            possible_photos = possible_photos.filter(Q(visibility=VISIBILITY_PUBLIC) | Q(owner=user))
        return possible_photos
        """
        return possible_photos


class DetailView(View):

    def get(self, request, pk, user):
        """
        Renderiza el detalle del post de un usuario espesifico.
        :param request:
        :return:
        """
        user_object = get_object_or_404(User, username=user)  # consulta al usuario a actualizar.
        blogs = BlogQueryset.get_posts_by_user(request.user).filter(pk=pk, owner=user_object)
        if len(blogs) == 0:
            return HttpResponseNotFound("El blog que buscas no existe")
        elif len(blogs) > 1:
            return HttpResponse("Multiples Opciones", status=300)

        post = blogs[0] if len(blogs) > 0 else None
        context = {'post': post}
        return render(request, 'blog/detail.html', context)
        # return HttpResponse('/blog/detail.html')

