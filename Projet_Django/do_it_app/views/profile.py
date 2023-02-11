from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from do_it_app.models.profile import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['discord_username', 'discord_id', 'discord_webhook']
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        try:
            profile = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            profile = self.model(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = self.request.user.task_set.count()
        tasks_complete = self.request.user.task_set.filter(complete=True).count()

        if tasks == 0:
            ratio = 1
        else:
            ratio = tasks_complete/tasks

        context['dateNow'] = datetime.now()
        context['task_count'] = tasks
        context['completed_task_count'] = tasks_complete
        context['incomplete_task_count'] = self.request.user.task_set.filter(complete=False).count()
        context['task_ratio'] = "{:.0%}".format(ratio)

        return context
