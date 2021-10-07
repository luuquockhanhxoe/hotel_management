from django.shortcuts import render
from .models import Room_Info

def home_page(request):
    Room_Info_list = Room_Info.objects.all()
    return render(request, "home_page.html", {'Room_Info_list': Room_Info_list})