"""Projet_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from do_it_app.views.profile import ProfileUpdateView
from do_it_app.views.send_webhook import SendDiscordWebhookView
from do_it_app.views.task_create import TaskCreate
from do_it_app.views.task_delete import TaskDelete
from do_it_app.views.task_detail import TaskDetail
from do_it_app.views.task_list import TaskList
from do_it_app.views.task_update import TaskUpdate
from do_it_app.views.user_login import UserLogin
from do_it_app.views.user_register import UserRegister
from django.contrib.auth.views import LogoutView  # default logout view from django

from do_it_app.views import send_webhook

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('register/', UserRegister.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create/task/', TaskCreate.as_view(), name='task_create'),
    path('update/task/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('delete/task/<int:pk>', TaskDelete.as_view(), name='task_delete'),
    # path('send_discord_webhook/', SendDiscordWebhookView.as_view(), name='send_discord_webhook'),
    path('send_discord_webhook/<int:task_id>', SendDiscordWebhookView.as_view(), name='send_discord_webhook'),
]
