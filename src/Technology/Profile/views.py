from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ApplicationModelForm


@login_required
def index(request):
    
    if request.method == 'POST':
        form = ApplicationModelForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
        return render(request, 'profile/confirmation.html')
    else:
        form = ApplicationModelForm()
    return render(request, 'profile/index.html', {'form':form})


def home_index(request):
    return render(request, 'profile/home.html')






















