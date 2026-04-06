from django.shortcuts import render, redirect
from .models import Item, Order, Purchase
from django.contrib.auth.models import User
from datetime import date

def item(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items': items})

def order(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(order_id=order_id)
    purchases = Purchase.objects.filter(order_id=order)

    return render(request, 'order_detail.html', {
        'order': order,
        'purchases': purchases
    })

def success(request):
    return render(request, 'success.html')

def buy_item(request, item_id):
    item = Item.objects.get(item_id=item_id)
    user = User.objects.first()

    order = Order(
        order_id=Order.objects.count() + 1,
        user_id=user,
        date=date.today()
    )
    order.save()

    Purchase.objects.create(
        order_id=order,
        item_id=item,
        quantity=1
    )

    return redirect('/orders/')

def add_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Item.objects.create(
            name=name,
            price=price,
            description=description
        )

        return redirect('/items/')

    return render(request, 'add_item.html')