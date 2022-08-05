from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    return render(
        request, './index.html', {
            'slider_list': slider_list,
        }
    )


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    order = Order(order_name=name, order_phone=phone)
    order.save()
    return render(
        request, './thanks.html',
        {
            'name': name,
            'phone': phone
        }
    )
