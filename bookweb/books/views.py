from django.shortcuts import render, redirect
import random
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


from .forms import CreateUserForm
from .models import *
from .forms import OrderForm


quote_options = ['“And so it goes...” - Kurt Vonnegut', 
                    '“O teach me how I should forget to think” - William Shakespeare',
                    '“Nothing contributes so much to tranquilize the mind as a steady purpose” - Mary Shelley',
                    '“There is nothing alive more agonized than man / of all that breathe and crawl across the earth.” - Homer',
                    '“A thing is not necessarily true because a man dies for it.” - Oscar Wilde',
                    '“I don`t want to die without any scars” -  Chuck Palahniuk',
                    ]



def quotes(request):
    
    random_text = random.choice(quote_options)
    
    return render(request, 'books/main.html', {'random_text': random_text})

def homepage(request):
    
    random_text = random.choice(quote_options)
    
    return render(request, 'books/homepage.html', {'random_text': random_text})


def discover(request):
    
    return render(request, 'books/discover.html')

def mybooks(request):
    
    return render(request, 'books/mybooks.html')

def myprofile(request):
    signup_form = CreateUserForm()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = CreateUserForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()  

        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('success_page')

    context = {'signup_form': signup_form, 'login_form': login_form}
    return render(request, 'books/myprofile.html', context)

def aboutus(request):
    
    return render(request, 'books/aboutus.html')
def success_page(request):
    return render(request, 'books/success.html')