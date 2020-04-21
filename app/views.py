from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todoitem

def todoview(request):
	all_items = Todoitem.objects.all()
	return render(request,'todo/index.html',{'all_items':all_items})

def addtodo(request):
	new_task = Todoitem(content = request.POST['content'])
	new_task.save()
	return HttpResponseRedirect('/todo/')

def deletetask(request,task_id):
	deletetask = Todoitem.objects.get(id = task_id).delete()
	return HttpResponseRedirect('/todo/')