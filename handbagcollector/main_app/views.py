from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Handbag
from .forms import WornForm

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
  worn_form = WornForm()
  return render(request, 'handbags/detail.html', {
    'handbag': handbag,
    'worn_form': worn_form
  })

class HandbagCreate(CreateView):
  model = Handbag
  fields = '__all__'

class HandbagUpdate(UpdateView):
  model = Handbag
  fields = ['description', 'brand', 'color', 'image']

class HandbagDelete(DeleteView):
  model = Handbag
  success_url = '/handbags'