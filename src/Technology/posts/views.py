from django.shortcuts import render
from .models import Events

def post_page(request):
    posts = Events.objects.all()
    context = {'post':posts}
    return render(request, 'profile/base.html', context)
