'''
for handling all the action redirected from urls
'''
import os
from datetime import datetime
from django.conf import settings
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from champagn.messages import Messages
from champagn.utility import FizzUtility
from app.utility import AppUtility
from django.contrib.auth import authenticate
from oauth2_provider.models import AccessToken
from django.db.models import Q
from champagn.permissions import IsOwnerOrReadOnly
from champagn.app_custom_methods import AppCustomMethods
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from champagn.constants import PROFILE_PIC_URL, PIC_KEY, VALID_EXTENSIONS 
from app.serializers import UserSerializer, AccessTokenSerializer, User
from django.contrib.sites.shortcuts import get_current_site


class SignUp(generics.CreateAPIView):
    '''
    API for registering new user
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kw):
        'for handling post request of signup service'
        response = {}
        response_data = {}
        device_id, device_token, device_type = FizzUtility.get_device_keys_from_request(request)

        user = User.objects.filter(email__iexact=request.data.get('email', None)).first()
        if user:
            response = {settings.MESSAGE_KEY: Messages.ALREADY_REGISTER_USER}
            response_data = FizzUtility.data_wrapper(
                response, settings.HTTP_USER_ERROR)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            user = self.create(request, *args, **kw)
            token_application_name = settings.APPLICATION_NAME
            user = User.objects.get(id=user.data.get('id', None))
            
            current_site = get_current_site(request)
            domain = current_site.domain

            user.protocol = 'http'
            user.domain = domain
            
            AppCustomMethods.send_email(user, request,
                            'thankyou_after_registration.html',
                            'The ChampagnFizz App - Welcome Email.')

            access_token = AppUtility.create_oauth_token(
                 user, request, token_application_name)\

            AppUtility.add_device_detail(
                device_type, device_id, user, device_token)

            user_serializer = UserSerializer(user)
            response_data['access_token'] = access_token.token
            response_data['user'] = user_serializer.data
            response = FizzUtility.data_wrapper(response_data)
            return Response(response, status=status.HTTP_200_OK)
        
 
class SignIn(APIView):
    '''
    API for SignIn to return User, Profile, Contact, Address models
    along with access token.
    '''
    queryset = User.objects.all()

    @classmethod
    def post(self, request, *args, **kw):
        'for handling post request of signin service'
        response = {}
        response_data = {}
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        device_id, device_token, device_type = FizzUtility.get_device_keys_from_request(request)

        if User.objects.filter(Q(email__iexact=email) & Q(is_superuser=False)).exists():
            user = authenticate(email=email, password=password)
            response = AppUtility.check_user_create_outh_token(
                user, device_id, device_type, request)

            res = response.get('response', None)
            if res:
                token = res.get('access_token', None)
                access_token = AccessToken.objects.filter(
                        token=token)
                if len(access_token) > 0:
                    AppUtility.add_device_detail(
                        device_type, device_id, user, device_token)

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {settings.MESSAGE_KEY: Messages.INVALID_USER_PASSWORD}
            response_data = FizzUtility.data_wrapper(
                response, settings.HTTP_USER_ERROR)
            return Response(response_data, status=status.HTTP_200_OK)
        

class SignOut(APIView):
    '''
    API for Expire Access Token to Sign out the User
    '''
    serializer_class = AccessTokenSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
 
    @classmethod
    def put(self, request, *args, **kw):
        'for handling post request of signout service'
        token = request.META['HTTP_AUTHORIZATION']
        lst_token = token.split(' ')
        access_token = get_object_or_404(AccessToken, token=lst_token[1])
        access_token.expires = timezone.now()
        access_token.save()
 
        response = {settings.MESSAGE_KEY: Messages.ACCESS_TOKEN_EXPIRED}
        response_data = FizzUtility.data_wrapper(
            response, status.HTTP_200_OK)
        return Response(response_data, status=status.HTTP_200_OK)
    

class GetProfile(generics.RetrieveAPIView):
    '''
        API for save the data for user sending request
    '''
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @classmethod
    def get(self, request, *args, **kwargs):
        'for handling get request of view profile'
        response_data = {}
        if request.user:
            user_serializer = UserSerializer(request.user)

            response_data['user'] = user_serializer.data
            response = FizzUtility.data_wrapper(response_data)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {settings.MESSAGE_KEY: Messages.NOT_FOUND}
            response_data = FizzUtility.data_wrapper(
                response, settings.HTTP_USER_ERROR)
            return Response(response_data, status=status.HTTP_200_OK)
        

class EditProfile(generics.UpdateAPIView):
    '''
    API for update the profile it will get the user access_token and find the
    user, update the user fields
    '''
    serializer_class = User
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    @classmethod
    def put(self, request, *args):
        user = request.user
        
        self.check_object_permissions(self.request, user)
        profile_pic_key = request.data.get(PIC_KEY, None)
      
        if profile_pic_key is not None:
            my_file = request.FILES[PIC_KEY]
            valid_extensions = VALID_EXTENSIONS
            if os.path.splitext(my_file.name)[1] in valid_extensions:
                ext = os.path.splitext(my_file.name)[1]
                filename = 'profile_pictures/' + str(datetime.now()).replace(" ", "_").replace("-", "_").replace(".", "_").replace(":", "_") + ext
            else:
                filename = 'profile_pictures/' + str(datetime.now()).replace(" ", "_").replace("-", "_").replace(".", "_").replace(":", "_") + '.jpg'
            request.data[PROFILE_PIC_URL] = filename
            with open(settings.MEDIA_ROOT + filename, 'wb') as temp_file:
                for chunk in my_file.chunks():
                    temp_file.write(chunk)
                temp_file.close()
        access = AppCustomMethods()
        response = access.update_user(user, request.data, False)
        return Response(response, status=status.HTTP_200_OK)


class ChangePassword(generics.CreateAPIView):
    '''
    API for Change Password
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    @classmethod
    def post(self, request):
        old_password = self.request.data.get('old_password', None)
        new_password = self.request.data.get('new_password', None)
        user = request.user
        self.check_object_permissions(self.request, user)
        match = user.check_password(old_password)
        response_data = {}
        response = {}
        if match:
            user.set_password(new_password)
            user.save()
            response_data[settings.MESSAGE_KEY] = Messages.PASSWORD_CHANGED_SUCCESSFULLY
        else:
            response_data['error'] = Messages.INVALID_PASSWORD
            response['status_code'] = status.HTTP_406_NOT_ACCEPTABLE
            response['response'] = response_data
            return Response(response)
        response = FizzUtility.data_wrapper(response_data)
        return Response(response)