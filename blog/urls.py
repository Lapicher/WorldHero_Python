from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from blog.views import HomeView, DetailView, HomeUserView, HomeRedirect, CrearPostView
from blog.api import BlogViewSet

router = DefaultRouter()
router.register('api/1.0/blogs', BlogViewSet, 'api_blogs_')

urlpatterns = [

    url(r'^$', HomeRedirect.as_view(), name="home"),
    url(r'^blogs/$', HomeView.as_view(), name="blog_home"),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', DetailView.as_view(), name='post_detail'),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)$', HomeUserView.as_view(), name="home_user"),
    url(r'^blogs/new_post/$', CrearPostView.as_view(), name="new_post"),

    # URLS APis
    url(r'', include(router.urls)),
]