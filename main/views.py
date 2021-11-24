from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime
from .models import WebData, Skill, SocialMedia, ContactFormData, Config
from discord_webhook import DiscordEmbed, DiscordWebhook
from django.conf import settings

# Create your views here.
def home(request:HttpRequest):
    vishal = WebData.objects.get(pk='vishal')
    skills = sorted(vishal.skills.all(), key=lambda skill:skill.percentage, reverse=True)
    context = {
        'name': vishal.name,
        'short_descr': vishal.short_descr,
        'med_descr': vishal.med_descr,
        'long_descr': vishal.long_descr,
        'socialmedias': vishal.socialmedias.all(),
        'age': datetime.utcnow().year - 2003,
        'email': vishal.email,
        'address': vishal.address,
        'status': vishal.status,
        'key_skills': skills[:(len(skills)+1)//2],
        'skills': skills[(len(skills)+1)//2:]
    }
    if request.method == 'POST':
        webhook = Config.objects.get(name='webhook')
        webhook = DiscordWebhook(url=webhook.url)
        embed = DiscordEmbed(title=request.POST['name'], description=request.POST['message'])
        embed.set_footer(text=request.POST['email'])
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
        ContactFormData(name=request.POST['name'], email=request.POST['email'],  message=request.POST['message']).save()
        return redirect('/')
    return render(request, 'main/index.html', context=context)