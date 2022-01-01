from .models import *

def category(request):
    return {'categories':Category.objects.all()}

def item(request):
    return {'items':Product.objects.all()}

def skater(request):
    return {'skaters':Skaters.objects.all()}