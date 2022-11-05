from django.shortcuts import render
from .models import img_details

# Create your views here.

def index(request):

    ims = img_details.objects.all()

    return render(request,'index.html',{'ims':ims})