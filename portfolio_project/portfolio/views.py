from django.shortcuts import render,redirect
from .models import Skill,Project
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.
def index(request):
    skill_list=Skill.objects.all()
    project_list=Project.objects.all()
    context={
        'skill_list':skill_list,
        'project_list':project_list,
    }
    if (request.method=="POST"):
        form=ContactForm(request.POST)
        if (form.is_valid()==False):
            form=ContactForm()
        else:
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            send_mail(subject=name,message=message,from_email=email,fail_silently=False,recipient_list='benup211@gmail.com')
            return redirect('portfolio:index')

    return render(request,'portfolio/index.html',context)