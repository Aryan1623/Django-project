from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.forms import taskform
from todolist_app.models import tasklist
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == 'POST':
        form = taskform(request.POST or None)
        if form.is_valid():
            form.save(commit = False).manage = request.user
            form.save()
            messages.success(request,("New task added"))
            return redirect('todolist')  # Use redirect instead of render to avoid form resubmission

    else:
        all_objects = tasklist.objects.filter(manage = request.user)
        paginator = Paginator(all_objects,2)
        page = request.GET.get('pg')
        all_objects = paginator.get_page(page)
        
         
        return render(request, 'todolist.html', {'welcome_message': all_objects})


@login_required
def contactus(request):
    return render(request, 'contactus.html', {'welcome_message': "Welcome to contact"})

def about(request):
    return render(request, 'about.html', {'welcome_message': "Welcome to about"})

@login_required
def delete_task(request,task_id):
    task = tasklist.objects.get(pk= task_id)
    if(task.manage == request.user):
       task.delete()
       return redirect('todolist')
    else:
      messages.error(request,("Access forbidden"))
      return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method == 'POST':
        task = tasklist.objects.get(pk= task_id)
        form = taskform(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
            messages.success(request,("Task edited"))
            return redirect('todolist')  # Use redirect instead of render to avoid form resubmission

    else:
        task_obj = tasklist.objects.get(pk = task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required   
def pending_task(request,task_id):
    task = tasklist.objects.get(pk= task_id)
    if(task.manage == request.user):
      task.done = False
      task.save()
      return redirect('todolist')
    else:
        messages.error(request,("you cannot make chabges"))
        return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task = tasklist.objects.get(pk= task_id)
    if(task.manage == request.user):
      task.done = True
      task.save()
      return redirect('todolist')
    else:
        messages.error(request,("you cannot make chabges"))
        return redirect('todolist')

def home(request):
    return render(request, 'home.html', {})