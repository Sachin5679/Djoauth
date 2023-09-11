from django.shortcuts import redirect, render


def page(request):
    return render(request, 'page.html')

def redirect(request):
    return redirect("oauth")