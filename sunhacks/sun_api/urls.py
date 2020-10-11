from django.urls import include, path
from rest_framework import routers
from .views import *
from knox import views as knox_views
from .views import LoginAPI

router = routers.DefaultRouter()
router.register('Roadmap',RoadmapViewSet)
router.register('Course',CourseViewSet)
router.register('Achievement',AchievementViewSet)
router.register('Fork',ForkViewSet)
router.register('User',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
