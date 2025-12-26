from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('me/', views.current_user),
    path('', include(router.urls)),
]