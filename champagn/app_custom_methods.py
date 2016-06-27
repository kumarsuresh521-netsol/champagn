from datetime import datetime, timedelta
from oauth2_provider.models import Application, AccessToken, RefreshToken
from oauthlib.oauth2.rfc6749.tokens import random_token_generator
from champagn.utility import FizzUtility
from app.serializers import UpdateSerializer
from django.template.loader import render_to_string
from job.models import Email
from champagn.constants import OAUTH_EXPIRY_SECONDS


class AppCustomMethods():
    '''
    class for common functions in app.api file
    '''
    @classmethod
    def update_user(self, user, data, is_busness_user):
        '''
        update function
        '''
        # comment below 2 lines when testing with device.
        serializer = UpdateSerializer(user, data, partial=True)
        response = {}
        response_data = {}
        if serializer.is_valid():
            user = serializer.save()
            update_serializer = UpdateSerializer(user)
            response = FizzUtility.data_wrapper(response_data)
            return response
        return {}
    
    @classmethod
    def create_access_token(self, user, request, application_name):
        '''
        API for create access token funcion
        '''
        scopes = 'read write'
        application = Application.objects.get(name=application_name)
        expires = datetime.now() + timedelta(seconds=OAUTH_EXPIRY_SECONDS)
        access_token = AccessToken.objects.create(user=user,
                                                  token=random_token_generator(
                                                      request),
                                                  application=application,
                                                  expires=expires, scope=scopes)
        RefreshToken.objects.create(user=user,
                                    token=random_token_generator(request),
                                    access_token=access_token,
                                    application=application)
        return access_token.token

    @staticmethod
    def send_email(user, request, template, subject):
        '''
        send email
        '''
        html_content = render_to_string(
            template, {"user": user})
        Email.objects.create(
            to_email=user.email,
            subject=subject,
            message=html_content)