from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Dish
from django.contrib import messages

# dishes
@login_required
def dish_manage(request):#show all dishes with option to edit / delete them 
    category_list=Category.objects.all()
    dishes_list=Dish.objects.all()
    if request.method=='POST':
        current_category=Category.objects.get(id=request.POST['category_id'])
        return render(request ,'manage_dish_by_category.html',{"category":current_category,"dishes":current_category.dish_set.all()})
    if request.method=='GET':
        return render(request, 'dish_manage.html',{"dishes":dishes_list,"categories":category_list})

@login_required
def new_dish(request):#create a new dish
    category_list=Category.objects.all()
    if request.method=='POST':
        #validate all important fields are there 
        if request.POST.get('category_id',None)==None or request.POST['dish_name']=='' or request.POST['dish_price']=='' or  request.POST['dish_image']=='' :
            messages.error(request, 'cant leave empty field empty')
            return redirect('new_dish')
        else:#creates a new dish 
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

@login_required
def edit_dish(request,id):#edit dish details
    category_list=Category.objects.all()
    current_dish=Dish.objects.get(id=id)
    if request.method=='POST':#validates requested dish field
            if request.POST.get('category_id',None)==None or request.POST['dish_name']=='' or request.POST['dish_price']=='' or  request.POST['dish_image']=='' :
                messages.error(request, 'cant leave empty field empty')
                return redirect('edit_dish' ,id=id)
            else:#apply changes to dish 
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

@login_required
def delete_dish(request,id):#delete a dish object
    if request.method=='GET':
        current_dish=Dish.objects.get(id=id)
        current_dish.delete()
        return redirect('dish_manage')
    
    
#categories :
@login_required
def category_manage(request):#shows a screen that allows to manage categories 
    if request.method=='POST':
        pass
    if request.method=='GET':
        category_list=Category.objects.all()
        return render(request, 'category_manage.html',{'categories':category_list})

@login_required     
def new_category(request):#create new category object 
    if request.method == 'POST':
        if request.POST.get('category_name')=='' or request.POST['category_image']=='':#validates requested fields
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

@login_required
def edit_category(request,id):# edit category object 
    current_category=Category.objects.get(id=id)
    if request.method=='POST':
        if request.POST.get('category_name')=='' or request.POST['category_image']=='':#validates requested fields
            messages.error(request, 'cant leave empty field empty')
            return redirect('edit_category' , id=id)
        else:#apply changes 
            current_category.name=request.POST['category_name']
            current_category.image=request.POST['category_image']
            current_category.save()
        return redirect('category_manage')
    if request.method=='GET':
        return render(request,'edit_category.html',{"category":current_category})
    
@login_required
def delete_category(request,id):#delete a category object 
    if request.method=='GET':
        current_category=Category.objects.get(id=id)
        current_category.delete()
        return redirect('category_manage')

