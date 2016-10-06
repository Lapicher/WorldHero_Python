from django.conf.urls import url
from users.views import UserRegisterView

patrones_user = [

    url(r'^register$', UserRegisterView.as_view(), name="register_user"),
]