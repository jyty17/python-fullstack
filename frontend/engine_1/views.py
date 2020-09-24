from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib import messages

from .forms import FeedbackForm
from .forms import CreateUserForm
from .forms import UploaderForm
from .forms import EditUserForm

from .models import Uploads

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
    user = request.user
    # print(user, request.user.is_authenticated)
    if request.user.is_authenticated:
        username = request.user.username
        # uploads = Uploads.object.filter(user_id=user.id)
        # uploads = Uploads.objects.select_related('user_id').get(id=user.id)
        context = {'user': user, 'heading': f"Welcome {username}!"}
    else:
        content="Welcome to BenAna, a service used to analyze your script"
        context={'user': None, 'heading': content}
    # return HttpResponse("This is home!")
    return render(request, 'engine_1/home.html', context=context)

def user_login(request):
    if request.user and request.user.is_authenticated:
        return redirect("/engine")
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
    context = {'user': None, 'form': form}
    return render(request=request, template_name="engine_1/login.html", context=context)
    # return HttpResponse("This is the login page")

def user_logout(request):
    user = request.user
    if user and user.is_authenticated:
        logout(request)
        context = {
            'user': user
        }
    else:
        return redirect('/engine')
    return render(request, 'engine_1/logout.html', context=context)

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
    return render(request, 'engine_1/signup.html', {'form': form, 'user': None})

def about(request):
    user = request.user if request.user.is_authenticated else None
    context = {
        'user': user,
    }
    return render(request, 'engine_1/about.html', context=context)
    # return HttpResponse("About This App!")

def user_profile(request, id):
    user = request.user if request.user.is_authenticated else None
    if user:
        profile = User.objects.get(pk=user.id)
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user)
            # .exclude(field_value="password")
            if form.is_valid():
                form.save()
                return redirect(f'/engine/{user.id}/profile')
        else:
            form = EditUserForm(instance=user)
            context = {
                'form': form
            }
            return render(request, 'engine_1/profile.html', context=context)
    else:
        return redirect('/engine/login')


    return HttpResponse(f"User {id}'s profile")

def user_upload(request, id):
    user = request.user
    if not user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UploaderForm(request.POST)
        return redirect('/')
    else:
        form = UploaderForm()
    return render(request, 'engine_1/upload.html', {'user': user, 'form': form})































