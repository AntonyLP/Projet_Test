from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from do_it_app.models.task import Task


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks')

    # raise exception when a user want to delete a task that he is not the owner
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != self.request.user:
            raise Http404("You don't have permission to delete this Task")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dateNow'] = datetime.now()

        return context
