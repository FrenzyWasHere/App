from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('user-list/', views.userList, name="userList"),
    path('user-create/', views.userCreate, name="userCreate"),
]
