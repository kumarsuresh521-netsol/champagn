'''
for handling reusable set of code
'''
from datetime import datetime, timedelta
from rest_framework import status
from django.utils import timezone
from django.conf import settings
from oauth2_provider.models import Application, AccessToken, RefreshToken
from oauthlib.oauth2.rfc6749.tokens import random_token_generator
from app.models import User, UserDevice
from app.serializers import UserSerializer, UserDeviceSerializer
from champagn.utility import FizzUtility
from champagn.messages import Messages


class AppUtility:
    '''
    app utility for friendin
    '''
    @staticmethod
    def create_oauth_token(user_id, request, application_name):
        '''
        Create Outh token by user_id and application name
        '''
        scopes = 'read write'
        application = Application.objects.get(
            name=application_name)

        expires = datetime.now() + \
            timedelta(seconds=settings.OAUTH_EXPIRY_SECONDS)
        access_token = AccessToken.objects.create(
            user=user_id,
            token=random_token_generator(request),
            application=application,
            expires=expires,
            scope=scopes)

        RefreshToken.objects.create(
            user=user_id,
            token=random_token_generator(request),
            access_token=access_token,
            application=application
        )
        return access_token

    @staticmethod
    def check_user_create_outh_token(user, device_id=None, device_type=None, request=None):
        '''
        check user and create auth token
        '''
        response = {}
        response_data = {}

        if user:
            if user.is_active:
                # User is valid, active and authenticated
                if len(User.objects.filter(id=user.id)) > 0 and request is not None and device_type is not None:
                    obj_acces_token = AppUtility.create_oauth_token(
                        user, request, settings.APPLICATION_NAME)
                    response_data['access_token'] = obj_acces_token.token

                user_serializer = UserSerializer(user)
                response_data['user'] = user_serializer.data
                response["status_code"] = status.HTTP_200_OK
                response['response'] = response_data
                return response

            else:
                # The password is valid, but the account has been disabled!
                response = {
                    settings.MESSAGE_KEY:
                    Messages.PASSWORD_MATCHED_ACCOUNT_DISABLED % settings.ADMIN_EMAIL}
                response_data = FizzUtility.data_wrapper(
                    response, settings.HTTP_USER_ERROR)
                return response_data
        else:
            response = {settings.MESSAGE_KEY: Messages.INVALID_USER_PASSWORD}
            response_data = FizzUtility.data_wrapper(
                response, settings.HTTP_USER_ERROR)
            return response_data

    @staticmethod
    def check_and_update_device_token(device_type, device_id, device_token):
        '''
        check and update device token
        '''
        if device_token:
            UserDevice.objects.filter(
                device_token=device_token, is_device_token_valid=True).update(
                    is_device_token_valid=False)

    @staticmethod
    def add_device_detail(device_type, device_id, user, device_token=None):
        '''
        add device detail
        '''
        device_info = {'user': user.id, 'device_id': device_id,
                       'device_type': device_type,
                       'device_token': device_token}
        device_serializer = UserDeviceSerializer(data=device_info)
        if device_serializer.is_valid():
            AppUtility.check_and_update_device_token(device_type, device_id,
                                                     device_token)
            device_serializer.save()
        else:
            print (device_serializer.errors)

    @classmethod
    def expire_token(lst_acces_token):
        '''
        expire token
        '''
        count = 0
        for access_token in lst_acces_token:
            if not access_token.is_expired():
                access_token.expires = timezone.now()
                access_token.save()
                count = count + 1
        return count