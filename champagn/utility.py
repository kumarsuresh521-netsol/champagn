'''
utitlity for all the apps
'''
from django.conf import settings
from rest_framework import status


class FizzUtility:
    '''
    firend utitlity
    '''
    @staticmethod
    def data_wrapper(response=None, status_code=status.HTTP_200_OK):
        'data wrapper for handling standard response'
        response_dic = {}
        response_dic['status_code'] = status_code
        if settings.HTTP_USER_ERROR == status_code:
            response_dic['error'] = response
        elif response:
            response_dic['response'] = response

        return response_dic

    @staticmethod
    def get_device_keys_from_request(request):
        '''
        get device keys from request
        '''
        device_id = request.data.get('device_id', None)
        device_token = request.data.get('device_token', None)
        device_type = request.data.get('device_type', None)
        return device_id, device_token, device_type