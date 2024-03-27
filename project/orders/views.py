from django.shortcuts import render

from orders.models import SalesOrder


# Create your views here.

def order_pages(request):
    return render(request, 'index.html',
                  {"orders": SalesOrder.objects.all()})
