from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages

from .forms import FeedbackForm, CreateUserForm


#  ----------------------------------------------------------------------------------------
#  Initial placeholder pages

def index(request):
    # template = loader.get_template('engine_1/index.html')
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            msg=form.cleaned_data['message']
            # The delay is used to asynchronously process the task
            send_feedback_email_task.delay(name,email,msg)
            return HttpResponseRedirect('viz/')
    else:
        form=FeedbackForm
    # return HttpResponse(template.render({'form':form}, request))
    return render(request,'engine_1/index.html', {'form':form})

def viz(request):
    return HttpResponse("Welcome to Viz!")

#  ----------------------------------------------------------------------------------------

def home(request):

    if request.user.is_authenticated:
        username = request.user.username
        content=f"Welcome {username}!"
    else:
        content="Welcome to BenAna, a service used to analyze your script"
    # return HttpResponse("This is home!")
    return render(request, 'engine_1/home.html', context={'heading': content})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{user} logged in.")
                return redirect("/engine")
            else:
                messages.error(request, 'Invalid user login attempt.')
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="engine_1/login.html", context={'form': form})
    # return HttpResponse("This is the login page")

def about(request):
    return HttpResponse("About This App!")


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            # if form.validate_password
            user = authenticate(username=username, password=raw_password)
            login(user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'engine_1/signup.html', {'form': form})