from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'room', views.RoomApi)

urlpatterns = [
    path('', include(router.urls)),
    path('r/', views.Rooom.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]