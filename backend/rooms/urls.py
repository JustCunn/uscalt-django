from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'getroom', views.RoomApi)
router.register(r'rooms', views.GetRoomAPI, basename='rooms')
router.register(r'allrooms', views.GetAllRoomsView, basename='allrooms')

urlpatterns = [
    path('', include(router.urls)),
    path('registerroom/', views.RegisterRoom.as_view()),
    path('link/register/', views.RegisterLink.as_view()),
    path('test/', views.test.as_view()),
    path('link/buy/', views.BuyData.as_view()),
    path('link/upload/', views.UploadData.as_view()),
    path('link/check/', views.CheckIfExists.as_view()),
    re_path('link/download/(?P<link>.+)/(?P<uid>.+)/$', views.DownloadData.as_view()),
    re_path('room/(?P<argname>.+)/$', views.RoomLinks.as_view()),
    re_path('sample/(?P<link>.+)/$', views.DownloadSample.as_view()),
    #path('linkdata/reg/send/', views.UploadData.as_view()),
    re_path('^activelinks/(?P<room>.+)/$', views.GetRoomLinksByRoom.as_view()),
    re_path('^link/retrieve/(?P<name>.+)/$', views.RetrieveLink.as_view()),
    #re_path('^linkdata/reg/get/(?P<name>.+)/$', views.RetrieveData.as_view()),
]