from django.shortcuts import render, redirect
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Task

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detailnew', kwargs={'pk': self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'update.html'
    success_url = reverse_lazy('views')






















def home(request):
    task1= Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority, date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})



# def display(request):
#     # task=Task.objects.all()
#     return render(request,'display.html',{'task':task})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


# def edit(request, id):
#     task= Task.objects.get(id=id)
#     form = TodoForms(request.POST or None, instance=task)
#     if form.is_valid():
#         return redirect('/')
#
#     return render(request, 'edit.html', {'task': task, 'form': form})


def edit(request, id):
    task= Task.objects.get(id=id)
    form=TodoForms(request.POST or None, instance=task)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'edit.html', {'task': task, 'form': form})
