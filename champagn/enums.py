'''
enums for all the apps
'''
from django_enumfield import enum


class DeviceType(enum.Enum):
    '''
    enums for device type
    '''
    IOS = 0
    ANDROID = 1

class GenderType(enum.Enum):
    '''
    enums for gender type
    '''
    NOT_MENTIONED = 0
    MALE = 1
    FEMALE = 2

class SentStatusType(enum.Enum):
    '''
    Enum for sent status Type
    '''
    PENDING = 0
    INPROGRESS = 1
    SUCCESS = 2
    ERROR = 3
    
class DataType(enum.Enum):
    '''
    enums for device type
    '''
    TEXT = 0
    IMAGE = 1 
    
    labels = {
        TEXT: 'Text',
        IMAGE: 'Image',
    }
    
class CmsPageType(enum.Enum):
    '''
    Enum for sent status Type
    '''
    CONTACT_US = 0
    ABOUT_US = 1
    PRIVACY = 2
    TERMS_OF_USE = 3
    MEDIA_CONTACT = 4
    INVESTERS = 5
    APP_DEVELOPER = 6
    NONE = 7

    labels = {
        CONTACT_US: 'Contact Us',
        ABOUT_US: 'About Us',
        PRIVACY: 'Privacy',
        TERMS_OF_USE: 'Terms of use',
        MEDIA_CONTACT: 'Media Contact',
        INVESTERS: 'Investors',
        APP_DEVELOPER: 'App Developers',
        NONE: 'None'
    }
