from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddClientForm
from .models import Client



def home(request):

    clients = Client.objects.all()

    # Check to see if Logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging you in!")
            return redirect('home')

    else:
        return render(request, 'home.html', {'clients':clients})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


def client_info(request, pk):
    if request.user.is_authenticated:
        #Look up Records
        client_info = Client.objects.get(id=pk)
        return render(request, 'client_info.html', {'client_info':client_info})
    else:
        messages.success(request, "You have login to view that page!")
        return redirect('home')
    
def delete_client(request, pk):
    if request.user.is_authenticated:
        delete_it = Client.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Client Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that...")
        return redirect('home')
    

def add_client(request):
    form = AddClientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_client = form.save()
                messages.success(request, "Client created successfully...")
                return redirect('home')
        return render(request, 'add_client.html', {'form':form})
    else:
        messages.success(request, "You have to login before creating a client....")
        return redirect('home')
    

def update_client_info(request, pk):
    if request.user.is_authenticated:
        current_client = Client.objects.get(id=pk)
        form = AddClientForm(request.POST or None, instance=current_client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client info updated...")
            return redirect('home')
        return render(request, 'update_client_info.html', {'form':form})
    else:
        messages.success(request, "You must be logged in...")
        return render('home')