from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task, Category
from .forms import TaskForm, CategoryForm

def home(request):
    tasks = Task.objects.all().order_by('-date_created')

    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')
    category_filter = request.GET.get('category')

    if status_filter == 'completed':
        tasks = tasks.filter(completed=True)
    elif status_filter == 'pending':
        tasks = tasks.filter(completed=False)

    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    if category_filter:
        tasks = tasks.filter(category__id=category_filter)

    categories = Category.objects.all()

    context = {
        'tasks': tasks,
        'categories': categories,
        'selected_status': status_filter,
        'selected_priority': priority_filter,
        'selected_category': category_filter
    }

    return render(request, 'tasks/home.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})
