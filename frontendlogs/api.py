from champagn.utility import FizzUtility
from rest_framework import generics, status
from rest_framework.response import Response

from frontendlogs.models import FrontLog
import serializers


class FrontendLog(generics.CreateAPIView):
    '''
    API for Signup
    '''
    serializer_class = serializers.FrontLogSerializer

    def post(self, request, *args, **kwargs):
        exception = self.create(request, *args, **kwargs)
        exception = FrontLog.objects.get(id=exception.data.get('id', None))

        exception_serializer = serializers.FrontLogSerializer(exception)
        response_data = {}
        response_data['exception'] = exception_serializer.data
        response = FizzUtility.data_wrapper(response_data)
        return Response(response, status=status.HTTP_200_OK)
