
from django.shortcuts import render,redirect
from django.views import View
from users.models import CustomUser
from users.forms import UserCreateForm, UserLoginForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages




class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        
        context = {
            'form':create_form
        }  
        return render(request, 'users/register.html',context)
    
    def post(self,request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
              
            return redirect('users:login')
        else: 
            context = {
                'form':create_form
            }   
        return render(request, 'users/register.html', context)
  
    
class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        context =  {'form':login_form}
        return render(request,'users/login.html', context)
    
    def post(self, request):        
        login_form = AuthenticationForm(data=request.POST)
        
        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)
            messages.success(request, 'You have successully loged in')
            
            return redirect('books:list')
        else:        
        
            context =  {'form':login_form}
            
            return render(request,'users/login.html', context)
    
 
class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
          
       
        context = {'user':request.user}
        return render(request, 'users/profile.html', context) 
    
    

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.info(request, 'You have successfully loged out')
        
        return redirect('landing_page')
    
    
class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        context = {'form': user_update_form}
        return render(request,"users/profile_edit.html",context)    
        
    def post(self,request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
            )
        
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request,"You have successfully update your profile.")
            return redirect('users:profile')
        
        context = {'form':user_update_form}
        return render(request,"users/profile_edit.html", context) 
        
        

