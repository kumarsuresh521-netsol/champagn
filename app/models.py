'''
models for app
'''
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,\
    BaseUserManager
from django.db import models
from django_enumfield import enum
from champagn import enums
from champagn.validators import validate_product_image
from product.models import Product


class CustomUserManager(BaseUserManager):
    """
    for handling create user for user model
    """
    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given ,
        email and password.
        """
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        Creates and saves a Super User with the given ,
        email and password.
        """
        return self._create_user(email, password, True, True,
                                 **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email__iexact=email)


class User(AbstractBaseUser, PermissionsMixin):
    """
    model for create user which extends AbstractBaseUser and Permissions
    """
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, unique=True)
    dob = models.DateField(auto_now_add=True, null=True, blank=True)
    gender_type = enum.EnumField(enums.GenderType, default=enums.GenderType.NOT_MENTIONED)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False,
                                   help_text=('Designates whether\
                                   the user can log into this admin site.'))
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        "Returns the first name for the user."
        return self.name
    
    def get_full_name(self):
        "Returns the first name for the user."
        return self.name

    def __unicode__(self):
        return self.email
    
class UserAddress(models.Model):
    """
    model for User Addresses
    """
    user = models.ForeignKey(User, related_name='user_address')
    contact_name = models.CharField(max_length=200)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.IntegerField()
    zip = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    address_type = models.IntegerField()
    
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id


class UserDevice(models.Model):
    """
    model for App User Device
    """
    user = models.ForeignKey(User, related_name='user_device')
    device_token = models.CharField(max_length=200, blank=True)
    device_id = models.CharField(max_length=500)
    device_type = enum.EnumField(
        enums.DeviceType, default=enums.DeviceType.IOS)
    is_active = models.BooleanField(default=False,
                                    help_text=('Designates whether the App '
                                               'User Device is active or '
                                               'not '))
    is_device_token_valid = models.BooleanField(default=True,
                                                help_text=('Designates whether the'
                                                           'User Device token is valid or'
                                                           ' not '))
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.email
    
class UserTemplate(models.Model):
    """
    model for App User Templates
    """
    user_id = models.IntegerField()
    product_template_id = models.IntegerField()
    is_active = models.BooleanField(default=False,
                                    help_text=('Designates whether the App '
                                               'User Device is active or '
                                               'not '))
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
    
class UserTemplateData(models.Model):
    """
    model for App User Templates
    """
    user_template_id = models.IntegerField()
    text = models.CharField(max_length=500)
    image_name = models.ImageField(upload_to='user_template_data_images/',
                                      null=True, blank=True,
                                      help_text=('Image Size\
                                      should not more than 300kb.'),
                                      validators=[validate_product_image])
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
    
class Order(models.Model):
    """
    model for App User Templates
    """
    user = models.ForeignKey(User, related_name='user_order')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=100)
    user_shipping_address_id = models.IntegerField()
    user_billing_address_id = models.IntegerField()
    order_status = models.IntegerField()
    payment_status = models.IntegerField()
    image_name = models.ImageField(upload_to='user_template_data_images/',
                                      null=True, blank=True,
                                      help_text=('Image Size\
                                      should not more than 300kb.'),
                                      validators=[validate_product_image])           
    payment_details = models.CharField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
    
class OrderDetail(models.Model):
    """
    model for App User Templates
    """
    order = models.ForeignKey(Order, related_name='order_detail')
    product_id = models.ForeignKey(Product, related_name='product_id')
    qty = models.IntegerField()
    amount = models.CharField(max_length=200)
    template_id = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
    
class EngravingTemplate(models.Model):
    """
    model for App User Templates
    """
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.id
    
class OrderEngraving(models.Model):
    """
    model for App User Templates
    """
    order_detail_id = models.IntegerField()
    engraving_template_id = models.IntegerField()
    text = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
