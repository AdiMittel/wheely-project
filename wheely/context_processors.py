from .models import *

def category(request):
    return {'categories':Category.objects.all()}