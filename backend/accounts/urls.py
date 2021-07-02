from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserProfileAPI)
router.register(r'u', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]