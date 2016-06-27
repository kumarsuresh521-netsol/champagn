import os
import sys
import django
# Add this line if your script is not in your app directory

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'champagn.settings'

from threading import Timer
from datetime import datetime
from django.core.mail.message import EmailMessage

django.setup()
from job.models import Email
from champagn import enums
from champagn.constants import SCHEDULER_TIMING


def shedular_of_email():
    email_set = Email.objects.filter(
        sent_status_type=enums.SentStatusType.PENDING)
    for email in email_set:
        try:
            email.sent_status_type = enums.SentStatusType.INPROGRESS
            email.save()
            from_email = email.from_email
            to_email = email.to_email
            html_content = email.message
            subject = email.subject
            lst_cc_email = email.cc
            print (to_email)

            '''Send Email'''
            msg = EmailMessage(
                subject, html_content, from_email, [to_email], cc=lst_cc_email)
            msg.content_subtype = "html"  # Main content is now text/html

            sent_status = msg.send()

            if int(sent_status) == 1:
                email.sent_status_type = enums.SentStatusType.SUCCESS
                email.sent_date = datetime.now()
                email.save()
                print ('Success:')
                print ('Email sent successfully for :  %s' % email.id)
            elif int(sent_status) == 0:
                email.sent_status_type = enums.SentStatusType.ERROR
                email.send_date = datetime.now()
                email.save()
                print ('Error:')
                print ('Not sent - Error in notification : %s' % email.id)
        except:
            email.sent_status_type = enums.SentStatusType.PENDING
            email.save()
            print ("Unexpected error:", sys.exc_info())
            print ('Not sent - Error in notification (Loop Level) : %s' %
                   email.id)


class RepeatedTimer(object):
    '''
    for repeated timer
    '''
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


# it auto-starts, no need of rt.start()
runScheduler = RepeatedTimer(SCHEDULER_TIMING, shedular_of_email)
