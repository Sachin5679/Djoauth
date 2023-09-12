from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from salesforce.auth import SalesforceAuth
import os
from dotenv import load_dotenv
from django.contrib import messages

load_dotenv()

@login_required
def welcome_page(request):
    return render(request, 'welcome.html')

def page(request):
    return render(request, 'page.html')

def initiate_oauth(request):
    client_id = os.getenv('CLIENT_ID')
    redirect_uri = os.getenv('CALLBACK_URI')
    scope = 'full'  # Adjust scopes as needed

    # Build the Salesforce authorization URL
    authorization_url = f'https://login.salesforce.com/services/oauth2/authorize?response_type=token&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}'

    return redirect(authorization_url)

def oauth_callback(request):
    # code = request.GET.get('code')
    # access_token, refresh_token, instance_url = Salesforce  Auth.authenticate(code)
    # # Store access_token, refresh_token, and instance_url in your database
    # # Redirect to the welcome page
    # return redirect(reverse('welcome'))
        # Check if the access_token is present in the URL fragment
    return render(request, 'welcome.html')

