import requests

from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import redirect
from django.views import View

from do_it_app.models.task import Task


def send_discord_webhook(self, request, task):
    user_discord_username = task.user.profile.discord_username
    user_discord_id = task.user.profile.discord_id

    if request.method == 'GET':
        url = task.user.profile.discord_webhook
        payload = {
            "username": user_discord_username,
            "embeds": [{
                "title": f"Nouveau rappel pour {task.user}",
                "description": f"Heyy <@{user_discord_id}> ! Tu as un nouveau rappel de tâche ! \n\n"
                               f"> **Titre de la tâche :** {task} \n"
                               f"> **Description de la tâche :** {task.description} \n"
                               f"> **Importance :** {task.importance}\n"
                               f"> **Complété :** {task.complete}\n"
                               f"> **Crée le :** {task.create.strftime('%d/%m/%Y - %H:%M')}",
                "color": 15158332
            }]
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(url, json=payload, headers=headers)
        return HttpResponse(status=200)
    return HttpResponseBadRequest()


class SendDiscordWebhookView(View):
    def dispatch(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        task = Task.objects.get(id=task_id)

        if task.user.profile.discord_webhook is None:
            raise Http404("You need to enter a webhook url in your profile")
        send_discord_webhook(self, request, task)
        return redirect('tasks')
