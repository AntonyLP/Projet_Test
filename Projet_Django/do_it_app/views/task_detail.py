from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView

from do_it_app.models.task import Task


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    # raise exception when a user want to see a task that he is not the owner
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != self.request.user:
            raise Http404("You don't have permission to see this Task")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dateNow'] = datetime.now()

        return context
