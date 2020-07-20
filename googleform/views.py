from django.shortcuts import render,redirect
from .models import CVModel
from .forms import CVForm
# Create your views here.


def home_view(request):
    if request.method=="POST":
        form=CVForm()
        context={}
        form=CVForm(request.POST ,request.FILES )
        if form.is_valid():
            print('validate')
            form.save()
            return redirect('/')
        else:
            return render(request,'home.html',{'error': 'Please enter valid information'})
        context['form']=form
    else:
        return render(request,'home.html')
