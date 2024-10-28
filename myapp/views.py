# myapp/views.py
from django.shortcuts import render, redirect
from .models import Details
from django.views.generic import TemplateView  # Optional, if you're using it in views


def index(request):
    return render(request, 'myapp/index.html')  # Points to the correct template path

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')
        
        # For testing: Print submitted data to console
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Address:", address)
        print("Message:", message)
        
        # You can add further processing here, like saving data to the database
        
    return render(request, 'myapp/index.html')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Create a new instance of the Details model and save it to the database
        detail = Details(name=name, email=email, phone=phone, address=address, message=message)
        detail.save()  # Save the instance to the database

        return redirect('success')  # Redirect to a success page after saving

    return render(request, 'myapp/index.html')