from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart,Items,Delivery , User
from Dishes.models import Category
from django.contrib import messages
from Dishes.models import Dish
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='user_screen')
def cart(request):
        if request.method=='GET':
            new_cart=Cart(user_id=User.objects.get(id=request.user.id))
            new_cart.save()
            return redirect('order' , cart_id=new_cart.id )
        

@login_required
def order(request, cart_id ):
    current_cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    dishes = Dish.objects.all()

    if request.method == 'POST':

        if request.POST.get('category_id',None) is not None:
            return redirect ('order_by_category' , category_id=request.POST['category_id'] , cart_id=cart_id)
        
        dish_id = request.POST.get('current_dish_id')
        amount = request.POST.get('selected_dish_amount')
        if not dish_id or not amount:
            messages.error(request, 'enter a valid amount ')
        elif int(amount) <= 0:
            messages.error(request, 'Amount must be greater than 0.')
        else:
            dish = Dish.objects.get(id=dish_id)
            item = Items.objects.create(dish_id=dish, cart_id=current_cart, amount=amount)
            messages.success(request, f'Successfully added {dish.name} to your cart.')
        return redirect('order', cart_id=cart_id)
    else:
        return render(request, 'order.html', {'cart_id': cart_id, 'dishes': dishes, 'current_cart': current_cart, 'categories': categories})


@login_required   
def order_by_category(request,category_id , cart_id):
    current_cart = Cart.objects.get(id=cart_id)
    dishes = Dish.objects.filter(category_id=category_id)
    if request.method=='POST':
        dish_id = request.POST.get('current_dish_id')
        amount = request.POST.get('selected_dish_amount')
        if not dish_id or not amount:
            messages.error(request, 'enter a valid amount ')
        elif int(amount) <= 0:
            messages.error(request, 'Amount must be greater than 0.')
        else:
            dish = Dish.objects.get(id=dish_id)
            item = Items.objects.create(dish_id=dish, cart_id=current_cart, amount=amount)
            messages.success(request, f'Successfully added {dish.name} to your cart.')
        return redirect('order_by_category',category_id=category_id, cart_id=cart_id)
    if request.method=='GET':
        return render(request, 'order_by_category.html', {'cart_id': cart_id, 'dishes': dishes, 'current_cart': current_cart})

@login_required()  
def delivery(request,cart_id):
    current_cart=Cart.objects.get(id=cart_id)
    if request.method=='POST':
        if request.POST['delivery_address']=='':
            messages.error(request, 'cant leave empty Adress field ')
            return redirect('delivery' , cart_id=cart_id)
        else:
            new_delivery=Delivery(
                order_id=current_cart,
                is_delivered=False,
                adress=request.POST['delivery_address'],
                comments=request.POST['comments']
            )
            new_delivery.save()
            return redirect('user_screen')
    if request.method=='GET':
        total_price=0
        for item in current_cart.items_set.all():
            total_price+=int((item.dish_id.price)*(item.amount))
        return render(request,'delivery.html',{"current_cart":current_cart,"total_price":total_price})

@login_required  
def order_history(request):
    if request.method == 'GET':
        if request.user.is_staff:
            deliveries=Delivery.objects.filter(is_delivered=True)
            return render(request, 'order_history_manager.html', {'delivered_list': deliveries})
        else:
            user_carts = request.user.cart_set.all()
            delivered_list = []
            for cart in user_carts:
                deliveries = Delivery.objects.filter(order_id=cart, is_delivered=True)
                delivered_list.extend(list(deliveries))
            return render(request, 'order_history.html', {'delivered_list': delivered_list})
    
@login_required
def active_orders(request):
    if request.method=='GET':
        user_carts = request.user.cart_set.all()
        delivered_list = []
        for cart in user_carts:
            deliveries = Delivery.objects.filter(order_id=cart, is_delivered=False)
            delivered_list.extend(list(deliveries))
        return render(request, 'order_history.html', {'delivered_list': delivered_list})
    
@login_required()
def order_management(request):
    active_orders = Delivery.objects.filter(is_delivered=False)

    if request.method == 'POST':
        order_id = request.POST.get('is_delivered', None)
        if order_id is not None:
            current_delivery = Delivery.objects.get(order_id=order_id)
            current_delivery.is_delivered = True
            current_delivery.save()

        return redirect('order_management')

    if request.method == 'GET':
        return render(request, 'order_management.html', {"active_orders": active_orders})


