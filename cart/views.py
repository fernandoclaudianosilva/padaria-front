from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import CheckoutForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, active=True)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    messages.success(request, f"{product.name} added to your cart.")
    return redirect(request.POST.get('next') or 'cart:cart_detail')


@require_POST
def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart:cart_detail')


@require_POST
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product)
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f"{product.name} removed from your cart.")
    return redirect('cart:cart_detail')


@require_POST
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart, 'page_title': "Your Cart | Gerardo's Italian Bakery"}
    return render(request, 'cart/cart.html', context)


def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.info(request, "Your cart is empty — add something delicious first!")
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order_context = {
                'name': f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}",
                'email': form.cleaned_data['email'],
                'total': cart.get_total_price(),
            }
            cart.clear()
            return render(request, 'cart/success.html', {
                'order': order_context,
                'page_title': "Order Received | Gerardo's Italian Bakery",
            })
    else:
        form = CheckoutForm()

    context = {
        'cart': cart,
        'form': form,
        'page_title': "Checkout | Gerardo's Italian Bakery",
    }
    return render(request, 'cart/checkout.html', context)
