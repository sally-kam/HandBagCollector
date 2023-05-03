from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for handbags index
    path('handbags/', views.handbags_index, name='index'),
    path('handbags/<int:handbag_id>/', views.handbags_detail, name='detail'),
    path('handbags/create/', views.HandbagCreate.as_view(), name='handbags_create'),
    path('handbags/<int:pk>/update/', views.HandbagUpdate.as_view(), name='handbags_update'),
    path('handbags/<int:pk>/delete/', views.HandbagDelete.as_view(), name='handbags_delete'),
    path('handbags/<int:handbag_id>/add_when_worn/', views.add_when_worn, name='add_when_worn'),
]
