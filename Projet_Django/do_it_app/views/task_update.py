from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from do_it_app.models.task import Task


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete', 'importance']
    template_name = 'task_update.html'
    success_url = reverse_lazy('tasks')

    # raise exception when a user want to edit a task that he is not the owner
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != self.request.user:
            raise Http404("You don't have permission to edit this Task")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dateNow'] = datetime.now()

        return context
