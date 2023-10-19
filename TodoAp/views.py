
from django.shortcuts import render,redirect
from.models import Task
from.forms import TodoForm




#Add Field To Database:
def add(request):
    task1=Task.objects.all()
    if request.method =='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})


#delete function
def delete(request,id):
    if request.method =='POST':
        deletetask=Task.objects.get(id=id)
        deletetask.delete()
        return redirect('/')
    return render(request,'delete.html')
# update:
def update(request,id):
    taskupdate=Task.objects.get(id=id)
    taskform=TodoForm(request.POST or None,request.FILES,instance=taskupdate)
    if taskform.is_valid():
        taskform.save()
        return redirect('/')
    return render(request,'update.html',{'taskform':taskform,'taskupdate':taskupdate})


# Create your views here.