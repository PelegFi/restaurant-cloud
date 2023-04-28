from django.shortcuts import render ,redirect
from .models import Category, Dish
from django.contrib import messages

# dishes
def dish_manage(request):
    category_list=Category.objects.all()
    dishes_list=Dish.objects.all()
    if request.method=='POST':
        current_category=Category.objects.get(id=request.POST['category_id'])
        return render(request ,'manage_dish_by_category.html',{"category":current_category,"dishes":current_category.dish_set.all()})
    if request.method=='GET':
        return render(request, 'dish_manage.html',{"dishes":dishes_list,"categories":category_list})


def new_dish(request):
    category_list=Category.objects.all()
    if request.method=='POST':
        if request.POST.get('category_id',None)==None or request.POST['dish_name']=='' or request.POST['dish_price']=='' or  request.POST['dish_image']=='' :
            messages.error(request, 'cant leave empty field empty')
            return redirect('new_dish')
        else:
            new_dish=Dish(
                name=request.POST['dish_name'],
                price=int(request.POST['dish_price']),
                description=request.POST['dish_description'],
                image=request.POST['dish_image'],
                is_gluten_free=request.POST.get('is_gluten_free', False)=='on',
                is_vegeterian=request.POST.get('is_vegeterian', False)=='on',
                category_id=Category.objects.get(id=request.POST.get('category_id',None))
        )
            new_dish.save()
            return redirect('dish_manage')
    if request.method=='GET':
        return render(request,'new_dish.html',{"categories":category_list})


def edit_dish(request,id):
    category_list=Category.objects.all()
    current_dish=Dish.objects.get(id=id)
    if request.method=='POST':
            current_dish.name=request.POST['dish_name']
            current_dish.price=int(request.POST['dish_price'])
            current_dish.description=request.POST['dish_description']
            current_dish.image=request.POST['dish_image']
            current_dish.is_gluten_free=request.POST.get('is_gluten_free',False)=='on'
            current_dish.is_vegeterian=request.POST.get('is_vegeterian',False)=='on'
            current_dish.category_id=Category.objects.get(id=request.POST['category_id'])
            current_dish.save()
            return redirect('dish_manage')
    if request.method=='GET':
        return render(request,'dish_edit.html',{"dish":current_dish,"categories":category_list})

def delete_dish(request,id):
    if request.method=='GET':
        current_dish=Dish.objects.get(id=id)
        current_dish.delete()
        return redirect('dish_manage')
    
    
#categories :
def category_manage(request):
    if request.method=='POST':
        pass
    if request.method=='GET':
        category_list=Category.objects.all()
        return render(request, 'category_manage.html',{'categories':category_list})
        
def new_category(request):
    if request.method == 'POST':
        if request.POST.get('category_name')=='' or request.POST['category_image']=='':
            messages.error(request, 'cant leave empty field empty')
            return redirect('new_category')
        else:
            new_category = Category(
                name=request.POST['category_name'],
                image=request.POST['category_image']
            )
            new_category.save()
            return redirect('category_manage')
    if request.method == 'GET':
        return render(request, 'add_category.html')

def edit_category(request,id):
    current_category=Category.objects.get(id=id)
    if request.method=='POST':
        if request.POST.get('category_name')=='' or request.POST['category_image']=='':
            messages.error(request, 'cant leave empty field empty')
            return redirect('edit_category' , id=id)
        current_category.name=request.POST['category_name']
        current_category.image=request.POST['category_image']
        current_category.save()
        return redirect('category_manage')
    if request.method=='GET':
        return render(request,'edit_category.html',{"category":current_category})
    
def delete_category(request,id):
    if request.method=='GET':
        current_category=Category.objects.get(id=id)
        current_category.delete()
        return redirect('category_manage')

