from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from catalogue.models import Product

def get_or_create_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            return cart
    cart = Cart.objects.create()
    request.session['cart_id'] = cart.id
    return cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    items = cart.items.all() if cart else []
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})

def remove_from_cart(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    if cart:
        cart.items.filter(product_id=product_id).delete()
    return redirect('cart:cart_detail')