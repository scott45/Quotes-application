from .models import Quote
from django.template import RequestContext
from .forms import QuoteForm, UserForm
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})


def quote(request):
    context_dict = {}
    context = RequestContext(request)
    quote_list = Quote.objects.all()
    for quote in quote_list:
        context_dict = {'quotes': quote_list}
    return render_to_response('quotes/available_quote.html', context_dict, context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'registration/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'index.html')
            else:
                return render(request, 'registration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'index.html')
    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)
