from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'ranking', views.ProfileViewSet, basename='ranking')
router.register(r'challenges', views.ChallengeViewSet, basename='challenges')
router.register(r'completed', views.CompletedViewSet, basename='completed')
router.register(r'attempt', views.AttemptViewSet, basename='attempt')
router.register(r'user', views.UserEditViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]