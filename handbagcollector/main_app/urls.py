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
    path('handbags/<int:handbag_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
    path('handbags/<int:handbag_id>/unassoc_item/<int:item_id>/', views.unassoc_item, name='unassoc_item'),
    path('items/', views.ItemList.as_view(), name='items_index'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]
