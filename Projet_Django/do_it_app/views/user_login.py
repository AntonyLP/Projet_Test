from datetime import datetime

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class UserLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'  # send all attributes like => ['attr', 'attr', .. ]
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dateNow'] = datetime.now()

        return context
