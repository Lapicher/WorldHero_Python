from django.conf.urls import url
from blog.views import HomeView

urlpatterns = [
    #url(r'^blogs/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    #url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    #url(r'^photos/$', PhotoListView.as_view(), name='photos_my_photos'),
    #url(r'^$', HomeView.as_view(), name='photos_home'),

    url(r'^$', HomeView.as_view(), name="blog_home"),
]