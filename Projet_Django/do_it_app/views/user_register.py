from datetime import datetime

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView


class UserRegister(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:  # if user successfully created -> run the login function
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        # if user already connected, redirect to tasks page to prevent some spamming user creation
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegister, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dateNow'] = datetime.now()

        return context
