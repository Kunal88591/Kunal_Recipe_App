from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def receipes(request):
    context = {}
    query = request.GET.get('search', '')
    
    if query:
        queryset = Receipe.objects.filter(receipe_name__icontains=query)
    else:
        queryset = Receipe.objects.all()

    context['receipes'] = queryset

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_image=receipe_image,
            receipe_description=receipe_description,
        )
        return redirect("success")

    return render(request, "receipes.html", context)

    

def delete_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)
    queryset.delete()
    return redirect("/receipes/")



def update_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("/receipes/")

    context = {
        "receipe": queryset,
    }
    return render(request, "update.html", context)

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        terms = request.POST.get('terms')

        
        if not terms:
            messages.error(request, "You must agree to the terms of service.")
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'register.html')

        try:
            
            user = User.objects.create(
                username=email,  
                first_name=name,
                email=email,
                password=make_password(password)  
            )
            user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')


def login_view(request):

    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("/receipes/")  
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, "login.html")

def terms(request):
    return render(request, "terms.html")

def my(request):
    return render(request, "index.html" )

def contact (request):
    return render(request, "contact.html" )

