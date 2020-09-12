from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import FeedbackForm


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
    return HttpResponse("This is home!")

def login(request):
    return HttpResponse("This is the login page")

def about(request):
    return HttpResponse("About This App!")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})