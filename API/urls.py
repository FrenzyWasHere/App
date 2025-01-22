from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('user-list/', views.userList, name="userList"),
    path('user-create/', views.userCreate, name="userCreate"),
    path('user-login/', views.userLogin, name='userLogin'),
    path('test-token/',views.testToken,name="testToken"),
    path('user-update/',views.userUpdate,name="userUpdate"),
    path('user-delete/<str:pk>/',views.userDelete,name="userDelete"),
]
