from django.shortcuts import render
from .models import Handbag

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def handbags_index(request):
  handbags = Handbag.objects.all()
  return render(request, 'handbags/index.html', {
    'handbags': handbags
  })