# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from users.views import UserRegisterView, ActualizarUser, LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

router = DefaultRouter()
router.register('api/1.0/users', UserViewSet, base_name='api_users_')

patrones_user = [

    url(r'^signup$', UserRegisterView.as_view(), name="register_user"),
    url(r'^blogs/(?P<user>[a-zA-Z0-9]+)/updateUser$', ActualizarUser.as_view(), name="update_user"),

    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', LogoutView.as_view(), name="logout"),


    # URLS API
    url(r'', include(router.urls))
]