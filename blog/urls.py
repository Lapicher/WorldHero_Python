from django.conf.urls import url
from blog.views import HomeView, DetailView, HomeUserView, HomeRedirect

urlpatterns = [

    url(r'^$', HomeRedirect.as_view(), name="home"),
    url(r'^blogs/$', HomeView.as_view(), name="blog_home"),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', DetailView.as_view(), name='post_detail'),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)$', HomeUserView.as_view(), name="home_user")

]