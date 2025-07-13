from django.shortcuts import render ,redirect
from .models import Product
from django.core.paginator import Paginator
from .forms import adding_content

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')
    latest_products = Product.objects.order_by('-id')  
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products
    }
    return render(request, 'index.html', context)
def list_products(request):
    """
    _summary_
    returns products list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page=1
    if request.GET.get('page'):
        page = request.GET.get('page',1)
    product_list = Product.objects.order_by('priority')  
    product_paginator = Paginator(product_list, 2)  # Show 2 products per page
    product_list = product_paginator.get_page(page) ## Get the products for the requested page
    context = {
        'products': product_list
    }
    return render(request, 'products.html', context)
def detail_product(request, pk):
    product=Product.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request, 'product_detail.html', context)

def add_content(request):
    if request.method == 'POST':
        form = adding_content(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            customer = user.customer_profile  # Assuming OneToOneField to Customer
            content = form.save(commit=False)
            content.owner = customer  # Set owner to current customer
            content.save()
            return redirect('home')
    else:
        form = adding_content()
    return render(request, 'add_content.html', {'form': form})
