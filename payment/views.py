from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderForm
from basket.basket import Basket
from django.contrib import messages

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            # You might calculate the total amount based on the cart or selected items
            order.total_amount = calculate_total_amount(request)
            order.save()
            
            basket = Basket(request)
            for item in basket:
                # Use the correct key names
                print(f"Item: {item}")

                if 'qty' in item and 'price' in item:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['qty'],  # Changed from 'quantity' to 'qty'
                        #price=item['price'],
                        price=item['price'] * item['qty'], 
                    )
                else:
                    # Handle the case where qty or price is missing
                    print("Error: 'qty' or 'price' key missing in item")
            basket.clear()
          
            return redirect('payment:order_success', order_id=order.id)
    else:
        form = OrderForm()
    
    return render(request, 'payment/create_order.html', {'form': form})

def calculate_total_amount(request):
    basket = Basket(request)
    return basket.get_total_price()

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'payment/order_success.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'payment/order_history.html', {'orders': orders})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.order_status not in ['CANCELLED', 'SHIPPED', 'DELIVERED']:
        order.order_status = 'CANCELLED'
        order.save()
        messages.success(request, 'Your order has been cancelled successfully.')
    else:
        messages.error(request, 'Your order cannot be cancelled.')
    return redirect('payment:order_history')