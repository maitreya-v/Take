
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import createtask,CreateUserForm
from .models import Task
from django.contrib.auth import authenticate,login,logout
# User = get_user_model()

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("Hello")

def register(request):
    form =CreateUserForm()

    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'Register.html',context)

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('in here')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            print('worked')
            return redirect(readtask)
        print(user)
    context ={}
    return render(request,'Login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def addtask(request):
    context={}

    form = createtask(request.POST ,request.FILES)
    # print(request.FILES)
    if form.is_valid():
        form.save()
        return redirect(readtask)
    context["form"]=form
    # context['image']= 
    return render(request,'Form.html',context)

@login_required(login_url='login')
def readtask(request):
    list = Task.objects.all()
    data={
        'tasks' :list
    }
    return render (request,'List.html',data)

def updatetask(request,title):
    try:
        get_task= Task.objects.get(title=title)
    except Task.DoesNotExist:
        return redirect('readtask')
    update_task = createtask(request.POST or None, instance=get_task)
    print(title)
    if update_task.is_valid():
        update_task.save()
        print('it saved')
        return redirect(readtask)

    return render(request,'Update.html',{'update':update_task})

def deletetask(request,title):
    try:
        get_task= Task.objects.get(title=title)
    except Task.DoesNotExist:
        return redirect(readtask)
    get_task.delete()
    return redirect(readtask)