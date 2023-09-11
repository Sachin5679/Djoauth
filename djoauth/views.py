from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def welcome_page(request):
    return render(request, 'welcome.html')

def page(request):
    return render(request, 'page.html')

def redirect(request):
    return redirect("oauth")