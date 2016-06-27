'''
for middleware
'''
import sys
import traceback
import logging
import time
from django.conf import settings
from django.db import connection
from dateutil.parser import parse
from log.models import Log


class LoggingMiddleware(object):
    '''
    logging middleware
    '''
    @classmethod
    def process_request(self, request):
        '''
        process request
        '''
        self.start_time = time.time()

        self.request_body = request.body
        self.request_get_params = request.GET
    
    def process_response(self, request, response):
        '''
        process response
        '''
        try:
            lst_app_for_logging = settings.LST_APP_FOR_LOGGING
            full_stack_trace = ''
            exception_short_value = ''
            user_email = '-'
            extra_log = ''

            log = Log()
            type_exc, value, tb = sys.exc_info()

            log.request_datetime = parse(time.ctime(self.start_time))
            log.response_datetime = parse(time.ctime(time.time()))
            log.total_time_taken = time.time() - self.start_time

            remote_addr = request.META.get('REMOTE_ADDR')
            str_token = request.META.get('HTTP_AUTHORIZATION', None)

            if str_token:
                log.access_token = str_token
            if remote_addr in getattr(settings, 'INTERNAL_IPS', []):
                remote_addr = request.META.get(
                    'HTTP_X_FORWARDED_FOR') or remote_addr

            log.remote_address = remote_addr

            if hasattr(request, 'user'):
                user_email = getattr(request.user, 'email', '-')
            log.user_email = user_email
            if self.request_body:
                log.request_content_length = sys.getsizeof(
                    self.request_body) / float(1000)
                log.request_content = self.request_body

            log.response_content = response.content

            log.response_content_length = sys.getsizeof(
                response.content) / float(1000)
            # Return the size of object in bytes.

            if str(response.status_code) == '500' or str(
                    response.status_code) == '401' and type_exc:
                full_stack_trace = ' '.join(
                    traceback.format_exception(type_exc, value, tb))
                exception_short_value = str(value)
                log.exception_full_stack_trace = full_stack_trace
                log.exception_short_value = exception_short_value
                log.response_content = None
                log.response_content_length = None

            if settings.DEBUG:
                sql_time = sum(float(q['time'])
                               for q in connection.queries) * 1000
                extra_log += " (%s SQL queries, %s ms)" % (
                    len(connection.queries), sql_time)
                log.extra_log = extra_log

            log.method_type = request.method
            log.method_name = request.get_full_path()
            log.response_status_type = response.status_code
            if request.get_full_path().split('/')[1] in lst_app_for_logging:
                log.save()
        except Exception, e:
            logging.error("LoggingMiddleware Error: %s" % e)
        return response
