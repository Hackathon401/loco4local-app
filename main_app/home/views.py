from django.shortcuts import render
from django.http import HttpResponse
from .models import VendorPost


# Create your views here.
def index(request):
    businesses = VendorPost.objects.all
    context = {'businesses': businesses}
    return render(request, 'home.html', context)

def create_business(request):
    return render(request, 'create_business.html', {})

def account_info(request):
    return render(request, 'account_info.html', {})

def vendor_info(request, list_id):
    item = VendorPost.objects.get(pk=list_id)
    
    return render(request, 'vendor_info.html', {'item': item})

def business_info(request):
    vendors = VendorPost.objects.all()

    context = {'vendor':vendors}
    return render(request, 'business_info.html', context)

