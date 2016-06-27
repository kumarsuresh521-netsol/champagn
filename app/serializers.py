'''
app serializers
'''
from rest_framework import serializers
from app.models import User, UserDevice
from oauth2_provider.models import AccessToken



class UserSerializer(serializers.ModelSerializer):
    '''
    serializer for update user
    '''
    class Meta:
        '''
        meta for user
        '''
        model = User
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    @classmethod
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UpdateSerializer(serializers.ModelSerializer):
    '''
    serializer for Update api for the purpose to save
    '''

    class Meta:
        '''inner class'''
        model = User
        fields = ('id', 'name', 'email', 'gender_type',)
        

class UserDeviceSerializer(serializers.ModelSerializer):
    '''
    serializer for user device
    '''
    class Meta:
        '''
        meta for user device
        '''
        model = UserDevice


class AccessTokenSerializer(serializers.ModelSerializer):
    '''
    Serializer for Access Token
    '''
    class Meta:
        '''
        meta for access token
        '''
        model = AccessToken
        fields = ('token',)



