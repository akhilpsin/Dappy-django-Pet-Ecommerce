from django.shortcuts import render
from app.models import Product
from django.db.models import Q
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#@csrf_exempt
def search_result(request):
    products=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(des__contains=query))

    return render(request,'search.html',{'query':query,'products':products})