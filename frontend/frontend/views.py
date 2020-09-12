from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader

# from .forms import FeedbackForm

# def index(request):
#     template = loader.get_template('frontend/index.html')
#     if request.method=='POST':
#         form=FeedbackForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['email']
#             msg=form.cleaned_data['message']
#             # The delay is used to asynchronously process the task
#             send_feedback_email_task.delay(name,email,msg)
#             return HttpResponseRedirect('viz/')
#     else:
#         form=FeedbackForm
#     return HttpResponse(template.render({'form':form}, request))
#     # return render(request,'frontend/index.html', {'form':form})


def viz(request):
    return HttpResponse("Welcome to Viz!")