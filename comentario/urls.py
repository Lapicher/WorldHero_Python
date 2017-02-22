from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from comentario.api import CommentViewSet

router = DefaultRouter()
router.register('api/comments', CommentViewSet, 'api_comments_')


urlpatternsComment = [

    # URLS APis
    url(r'', include(router.urls)),
]
