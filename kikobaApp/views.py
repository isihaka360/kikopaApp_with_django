from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
from .models import Customer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# view controlling panel
def callback_requuests(request):
    # handling callback requests
    pass

def kikoba_investment_view(request):
    # logics for investment
    return render(request, 'kikobaApp/investment.html')

def loan_Application_view(request):
    # handling loan application requests
    return render(request, 'kikobaApp/loan_Application.html')

def about_us_view(request):
    return render(request,'kikobaApp/about.html')

def home_view(request):
    return render(request,'kikobaApp/home.html')

def register_view(request):
    
    """This function handles registration and
       The function accepts the POST request with five arguments as
       fistName , lastName , emailAddress , password and confirmed password
       The function uses the make_password method for password Encryption"""
       
    if request.method == 'POST':
        
        firstName = request.POST['firstName']
        lastName  = request.POST['lastName']
        email     = request.POST['email']
        password  = request.POST['password']
        confirmed_password = request.POST['confirmed_password']
        
        # checking validity of password and confirmed password
        if password == confirmed_password:
            hash_password = make_password(password)
            
            User = Customer(firstName = firstName , lastName = lastName , email = email , password = hash_password)
            User.save()
            return redirect('login')
            
        else:
            return render (request,'kikobaApp/register.html',{'error_message':'password do not match'})
    else:
        return render(request,'kikobaApp/register.html')
    
def login_view(request):
    
    if request.method == 'POST':
       email = request.POST['email']
       password = request.POST['password']
       user = authenticate(request, username=email, password=password)

       if user is not None:
        login(request, user)
        return redirect('dashboard')
    
       else:
         
         return render(request, 'kikobaApp/login.html', {'error_message': 'Invalid email or password.'})
     
    else:
        
        return render(request, 'kikobaApp/login.html')   
    
def logout_view(request):
    return redirect('login')   
            
@login_required
def dashboard_view(request):
    return render(request,'kikobaApp/dashboard.html')
    
