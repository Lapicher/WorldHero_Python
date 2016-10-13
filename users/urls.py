from django.conf.urls import url
from users.views import UserRegisterView, ActualizarUser

patrones_user = [

    url(r'^register$', UserRegisterView.as_view(), name="register_user"),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)/updateUser$', ActualizarUser.as_view(), name="update_user"),
]