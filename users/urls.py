from django.conf.urls import url
from users.views import UserRegisterView, ActualizarUser, LoginView, LogoutView

patrones_user = [

    url(r'^register$', UserRegisterView.as_view(), name="register_user"),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)/updateUser$', ActualizarUser.as_view(), name="update_user"),

    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', LogoutView.as_view(), name="logout")
]