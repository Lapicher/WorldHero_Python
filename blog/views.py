from django.shortcuts import render

# Create your views here.
from django.views import View
from blog.models import Blog


class HomeView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de los blogs.

        :param request: objeto HttpRequest con los datos de la peticion
        :return: objecto HttpResponse con los datos de la respuesta
        """

        blogs = Blog.objects.all().order_by('-created_at').select_related('owner')
        context = {'photo_list': blogs[:4]}
        return render(request, 'blog/index.html', context)
