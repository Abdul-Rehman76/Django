from django.shortcuts import render
from django.http import HttpResponse
from .models import Food    
from django.template import loader

# Create your views here.
def index(request):
    food_list = Food.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'food_list': food_list,
    }
    return HttpResponse(template.render(context=context, request=request))


food_list = Food.objects.all()
def item(request): 
    return HttpResponse(food_list)

def detail(request, food_id):
    food_item=Food.objects.get(pk=food_id)
    template = loader.get_template('food/food_item_detail.html')
    context = {
        'food_item': food_item,
    }
    return HttpResponse(template.render(context=context, request=request))