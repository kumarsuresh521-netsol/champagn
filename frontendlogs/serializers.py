from frontendlogs.models import FrontLog
from rest_framework import serializers


class FrontLogSerializer(serializers.ModelSerializer):
    '''
    serializer for front end exceptions api
    '''

    class Meta:
        '''inner class'''
        model = FrontLog
        fields = ('id', 'exception',)
