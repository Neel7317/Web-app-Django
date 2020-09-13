from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Booking,Room
from django.http import Http404
#from .models import Room
# Create your views here.
"""def index(request):
    return HttpResponse("Hello world")"""
    
def Register(request):
      if request.method=='POST':
            nm=request.POST['t1']
            mi=request.POST['t2']
            mob=request.POST['t3']
            psw=request.POST['t4']

            u=User.objects.create(Name=nm,Mail=mi,phone_number=mob,passwd=psw)
            u.save()
            return redirect('Login')
      else:

            return render(request,'Hotels/Register.html')

def Login(request):
      if request.method=='POST':

            m=request.POST['t1']
            p=request.POST['t2']
      
            a=User.objects.all()
            for x in a:
                  if  x.Mail==m and x.passwd==p:
                        return redirect('Home')
                  else:
                        return render(request,'Hotels/Login.html')
      return render(request,'Hotels/Login.html')
    
def Home(request):
      rooms=Room.objects.all()
      context={'rooms':rooms}
      return render(request,'Hotels/Home.html',context)

def RoomDetail(request,Room_id):
      try:
        room = Room.objects.get(pk=Room_id)
      except room.DoesNotExist:
              raise Http404("Room Dosent exist")
      return render(request,'Hotels/RoomDetails.html', {'rooms': room})
      

def BookedRoom(request):
      return HttpResponse("Looking for Booked Room page")

def aboutUs(request):
      return HttpResponse("Looking for about us page")


def Booking(request):
      return render(request,'Hotels/Booking.html')
