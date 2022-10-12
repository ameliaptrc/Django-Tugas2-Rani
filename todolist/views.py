from django.shortcuts import HttpResponse, render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


# fungsi to do list
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'username' : request.user.username,
        'list_task' : data_task,
    }
    return render(request, "todolist.html", context)


# fungsi registrasi
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


# fungsi login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

# fungsi log out
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# fungsi create task
@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            Task.objects.create(
            user = request.user,
            date = datetime.datetime.today(),
            title = form.cleaned_data['title'],
            description = form.cleaned_data['description'],
            is_finished = False,
                )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    else:
        context = {'form': form,
    } 
    
    return render(request, 'create_task.html', context)                

# fungsi delete task
def delete_task(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

# fungsi status
def status(request,id):
    status_data = Task.objects.get(pk=id)
    if status_data.is_finished:
       status_data.is_finished = False
    else:
        status_data.is_finished = True
    status_data.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def show_json_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

def show_todolist_ajax(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'username' : request.user.username,
        'list_task' : data_task,

    }
    return render(request, "todolist_ajax.html", context)


@csrf_exempt
def todolist_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.date.today()
        user = request.user
        todo = Task.objects.create(title=title, description=description, date=date, user=user)

        result = {
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'date':todo.date,
            },
            'pk':todo.pk
        }
        return JsonResponse(result)