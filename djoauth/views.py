from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import os
from dotenv import load_dotenv

load_dotenv()

@login_required
def welcome_page(request):
    return render(request, 'welcome.html')

def page(request):
    return render(request, 'page.html')

def initiate_oauth(request):
    client_id = os.getenv('CLIENT_ID')
    redirect_uri = os.getenv('CALLBACK_URI')
    scope = 'full'

    authorization_url = f'https://login.salesforce.com/services/oauth2/authorize?response_type=token&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}'

    return redirect(authorization_url)

def oauth_callback(request):
    return render(request, 'welcome.html')

