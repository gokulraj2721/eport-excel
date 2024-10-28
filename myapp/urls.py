from django.urls import path
from . import views
from django.views.generic import TemplateView  # Import TemplateView for the success page

urlpatterns = [
    path('', views.index, name='index'),  # Main index view
    path('success/', TemplateView.as_view(template_name='myapp/success.html'), name='success'),  # Success page
]
