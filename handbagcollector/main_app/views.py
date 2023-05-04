from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Handbag, Item
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
  id_list = handbag.items.all().values_list('id')
  items_handbag_doesnt_have = Item.objects.exclude(id__in=id_list)
  worn_form = WornForm()
  return render(request, 'handbags/detail.html', {
    'handbag': handbag,
    'worn_form': worn_form,
    'items': items_handbag_doesnt_have
  })

class HandbagCreate(CreateView):
  model = Handbag
  fields = ['name', 'price', 'description', 'brand', 'color', 'image']

class HandbagUpdate(UpdateView):
  model = Handbag
  fields = ['description', 'brand', 'color', 'image']

class HandbagDelete(DeleteView):
  model = Handbag
  success_url = '/handbags'

def add_when_worn(request, handbag_id):
  form = WornForm(request.POST)
  if form.is_valid():
    new_worn = form.save(commit=False)
    new_worn.handbag_id = handbag_id
    new_worn.save()
  return redirect('detail', handbag_id=handbag_id)

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items'

def assoc_item(request, handbag_id, item_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Handbag.objects.get(id=handbag_id).items.add(item_id)
  return redirect('detail', handbag_id=handbag_id)

def unassoc_item(request, handbag_id, item_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Handbag.objects.get(id=handbag_id).items.remove(item_id)
  return redirect('detail', handbag_id=handbag_id)
