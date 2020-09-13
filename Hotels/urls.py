from django.urls import path
from . import views

urlpatterns=[
    
    path('Register/',views.Register,name='Register'),
    path('Login/',views.Login,name='Login'),
    path('',views.Home,name='Home'),
    path('<int:Room_id>/RoomDetail/',views.RoomDetail,name='RoomDetail'),
    path('BookedRoom/',views.BookedRoom,name='BookedRoom'),
    path('aboutUs/',views.aboutUs,name='BookedRoom'),
    path('Booking/',views.Booking,name='Booking'),
]