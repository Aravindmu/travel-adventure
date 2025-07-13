from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
from django.contrib import messages


# Create your views here.
def show_cart(request): 
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create( ## Get or create an order object for the customer ,it includes all the products in the cart
        owner=customer,
        order_status=Order.CART_STAGE
    )
    print(cart_obj.added_items.all())
 

    context = {
        'carts': cart_obj,
        
    }
    return render(request, 'cart.html',context)



def add_to_cart(request):
    if request.POST:
        user = request.user## Get the currently logged-in user
        customer = user.customer_profile## Get the customer's profile associated with the user ,the user==customer User: aravindmu Customer: aravindmu
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj, created = Order.objects.get_or_create( ## created is using for checking whether the order is created or not representing by true or false
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item = OrderedItem.objects.create(
            product=product,
            owner=cart_obj,
            quantity=quantity
        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity + quantity
            ordered_item.save()    
        

    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        try: 
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.save()
                messages.success(request, "Order placed successfully!")
            else:
                messages.error(request, "No items in the cart to checkout.")
        except Exception as e:
            messages.error(request, "An error occurred")
    return redirect('cart')


def remove_from_cart(request, pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
         item.delete()
         return redirect('cart')