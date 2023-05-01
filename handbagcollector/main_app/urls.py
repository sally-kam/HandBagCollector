from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for handbags index
    path('handbags/', views.handbags_index, name='index'),
]
