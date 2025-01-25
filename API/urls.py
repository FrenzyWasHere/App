from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('user-list/', views.userList, name="userList"),
    path('user-create/', views.userCreate, name="userCreate"),
    path('user-login/', views.userLogin, name='userLogin'),
    path('test-token/', views.testToken, name="testToken"),
    path('user-update/<str:pk>/', views.userUpdate, name="userUpdate"),
    path('user-delete/<str:pk>/', views.userDelete, name="userDelete"),
    path('doctors/', views.getDoctors, name="doctors"),
    path('get-doctor/<str:doctorId>/', views.getDoctor, name="get-doctor"),
    path('appointments/create/', views.createAppointment, name="createAppointment"),
    path('appointments/', views.listAppointments, name="list_appointments"),
    path('appointments/<str:appointment_id>/', views.getAppointment, name="getAppointment"),
    path('appointments/<str:appointment_id>/update/', views.updateAppointment, name="updateAppointment"),
    path('appointments/<str:appointment_id>/delete/', views.deleteAppointment, name="deleteAppointment"),
    path('user-appointments/<str:profileId>/', views.userAppointments, name="userAppointments"),
    path('profile/<str:profileId>/setImage/', views.setProfileImage, name="set_profile_image")
]