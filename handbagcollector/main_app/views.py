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

def handbags_detail(request, handbag_id):
  handbag = Handbag.objects.get(id=handbag_id)
  return render(request, 'handbags/detail.html', {'handbag': handbag})