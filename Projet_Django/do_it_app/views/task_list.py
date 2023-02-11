from random import choice
from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from do_it_app.models.task import Task

from django.contrib.auth.mixins import LoginRequiredMixin


greetings = [
    'Bonjour',
    'Hello',
    'Hallo',
    'Hola'
]

emojis = ['😝', '😁', '😀', '🙂', '🤪', '🤗', '🤖', '🤡', '🐶', '🐱']


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        tasks = super().get_queryset()
        tasks = tasks.filter(user=self.request.user).order_by('-create')
        search_input = self.request.GET.get('search') or ''
        if search_input:
            tasks = tasks.filter(title__contains=search_input)
        return tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = choice(greetings)
        context['emoji'] = choice(emojis)
        context['dateNow'] = datetime.now()

        return context
