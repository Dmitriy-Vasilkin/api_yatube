from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet


router_api_v1 = DefaultRouter()
router_api_v1.register('posts', PostViewSet, basename='posts')
router_api_v1.register('groups', GroupViewSet, basename='groups')
router_api_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
