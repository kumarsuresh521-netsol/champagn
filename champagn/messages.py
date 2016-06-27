'''
for handling messages for all the apps
'''


class Messages:
    '''
    messages definition
    '''
    INACTIVE_USER = 'Inactive User'
    ALREADY_REGISTER_USER = "User already exist!"
    NOT_AUTHENTICATED = "Not authenticated!"
    PASSWORD_MATCHED_ACCOUNT_DISABLED = 'Your account has been de-activated. For further information please send an email to %s!'
    '''
    parameter will be replaced with the value from ADMIN_EMAIL in settings.py
    '''
    PASSWORD_CHANGED_SUCCESSFULLY = "Password changed successfully!"
    INVALID_PASSWORD = 'Invalid Password'
    ACCESS_TOKEN_EXPIRED = "Access token expired!"
    USER_DOES_NOT_EXIST = "User does not exist!"
    INTERNAL_SERVER_ERROR = "Internal server error"
    SUCCESS = "Success"
    ERROR = "error"
    INVALID_TOKEN = "Invalid token!"
    INVALID_USER_PASSWORD = "Invalid username/password !"
    NOT_FOUND = 'Not Found!'
    TEHCNICAL_ISSUE = 'Due to some technical issue, unable to fetch data!'
    VIEW_PROFILE_BLOCKED_USER = 'The profile cannot be viewed at this time!'
    REPORT_EMAIL_MESSAGE_SUBJECT = '%s %s reported %s %s !'
    REPORT_BLOCK_EMAIL_MESSAGE_SUBJECT = '%s %s report/bock %s %s !'
    '''
    1st param = from_first_name
    2nd param = from_last_name
    3rd param = to_first_name
    4th param = to_last_name
    '''
    REACTIVATION_EMAIL_SUBJECT = 'Your account has been re-activated!'
    REACTIVATION_EMAIL_MESSAGE = 'Your account has been re-activated, now you can login on VIP FIZZ !'
    SEND_REQUEST_BLOCKED_USER = 'Request cannot be sent at this time!'
    REPORTED_REASON = 'Reported "%s" reason against this user.'
    BLOCKD_USR_UNABLE_LKE_COMENT = 'Operation cannot be completed at this time!'
    DEACTIVATION_EMAIL_SUBJECT = 'Your account has been de-activated!'
    DEACTIVATION_EMAIL_MESSAGE = 'Your account has been de-activated. For further information please send an email to %s!'
    ADMIN_UNABELE_TO_LOGIN = 'You are not authorize to login!'

