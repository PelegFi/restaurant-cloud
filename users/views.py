from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from .forms import CustomUserCreationForm , EditUserForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from final_project.views import home_page
from django.contrib.auth.models import User
from Dishes.models import Dish , Category


# Create your views here.
def signup(request):
   form = CustomUserCreationForm()
   if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('user_login')
       else:
           messages.success(request , 'singup success') 
           return render(request, 'signup.html', {"form": form})
   elif request.method == 'GET':
       if request.user != None and request.user.is_staff :
            return render(request, 'signup_admin.html', {"form": form})
       else:
            return render(request, 'signup.html' , {"form": form})



def user_login(request):
    if request.method=='POST':
        user=authenticate(request,
                          username=request.POST['username'],
                          password=request.POST['password']
                          )
        if user is not None:
            login(request,user)
            return redirect ('user_screen')
        else : 
            messages.error (request,'Wrong username or password')
            return redirect('home_page')
         
    if request.method=='GET':
        return redirect('home_page')

@login_required(login_url='user_login')
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST)
        if edit_form.is_valid():
            if request.user.is_staff:
                user.username = edit_form.cleaned_data['username']
                user.password = make_password(edit_form.cleaned_data['password'])
                user.first_name = edit_form.cleaned_data['first_name']
                user.last_name = edit_form.cleaned_data['last_name']
                user.email = edit_form.cleaned_data['email']
                user.is_staff = edit_form.cleaned_data.get('is_staff', False)
                user.save()
                return redirect('home_page')
            else:
                user.username = edit_form.cleaned_data['username']
                user.password = make_password(edit_form.cleaned_data['password'])
                user.first_name = edit_form.cleaned_data['first_name']
                user.last_name = edit_form.cleaned_data['last_name']
                user.email = edit_form.cleaned_data['email']
                user.is_staff = False
                user.save()
                return redirect('home_page')
    else:
        edit_form = EditUserForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff
        })
    if request.user.is_staff:
        return render(request, 'edit_user_admin.html', {'form': edit_form})
    else:
        return render(request, 'edit_user.html', {'form': edit_form})

@login_required
def manager_page(request):
    if request.method == 'GET':
        return render(request,'manager_page.html')

@login_required
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home_page')
    else:
        return redirect('home_page')

@login_required
def user_screen(request):
    categories=Category.objects.all()
    dishes=Dish.objects.all()
    if request.method=='POST':
        current_category=Category.objects.get(id=request.POST['category_id'])
        return render(request ,'dish_by_category.html',{"category":current_category,"dishes":current_category.dish_set.all()})
    if request.method=='GET':
        if request.user.is_staff:
            return render (request,'manager_page.html',{"dishes":dishes,"categories":categories})
        else:
            return render(request,'user_screen.html',{"dishes":dishes,"categories":categories})


   
@login_required()
def edit_managers(request):
    users_list=User.objects.all()
    if request.method == 'POST':
        current_user = User.objects.get(id=request.POST['is_staff'])
        current_user.is_staff = not current_user.is_staff
        current_user.save()
        return redirect('edit_managers')
    if request.method == 'GET':
        return render(request,'edit_managers.html',{"user_list":users_list})