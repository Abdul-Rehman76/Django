from django.urls import path
from . import views


app_name = 'food'         #adding namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:food_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
]