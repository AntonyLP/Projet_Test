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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.user)
    #     context['count'] = context['tasks'].filter(complete=False).count()
    #     context['greeting'] = choice(greetings)
    #     context['emoji'] = choice(emojis)
    #     context['dateNow'] = datetime.now()
    #
    #     search_input = self.request.GET.get('search') or ''
    #     if search_input:
    #         context['tasks'] = context['tasks'].filter(title__contains=search_input)
    #
    #     context['search_input'] = search_input
    #
    #     return context

    def get_queryset(self):
        tasks = super().get_queryset()
        # sorting with order_by() on current User tasks to prevent from all Tasks display
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
