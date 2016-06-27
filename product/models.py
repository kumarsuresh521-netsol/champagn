from django.db import models
from django_enumfield import enum
from champagn.enums import DataType
from champagn.validators import validate_category_image, validate_product_image
from django.core.files.storage import default_storage
from tinymce.models import HTMLField

# Create your models here.
class ProductCategory(models.Model):
    """
    model for Products Category
    """
    name = models.CharField(max_length=30)
    short_description = models.CharField(null=True, blank=True, max_length=250)
    logo_image = models.ImageField(upload_to='category_images/',
                                      help_text=('Image Size\
                                      should not more than 100kb.'),
                                      validators=[validate_category_image])
    sort_order = models.IntegerField(default=1, blank=True, null=True)
    occasion_start_date = models.DateField(null=True, blank=True)
    occasion_end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return self.name
    def thumbnail(self):
        if default_storage.exists(self.logo_image.name) and self.logo_image.name and self.logo_image.name != 'None':
            return """<img border="0"
            alt="Error" src="/static/%s" height="50" />
            """ % ((self.logo_image.name))
        else:
            return 'Image Not Uploaded'
    
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Occasion Image'
       
    class Meta:
        """inner class"""
        verbose_name = 'Occasion'
        verbose_name_plural = 'Occasions'
     

class Product(models.Model):
    """
    model for Products
    """
    category = models.ManyToManyField(ProductCategory)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    amount = models.FloatField()
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
     
    def __unicode__(self):
        return self.name
    
    def thumbnail(self):
        product_id = self.id
        product_image = ProductImages.objects.filter(product_id=product_id,
                                                  is_active=True).first()
                                                  
        if default_storage.exists(product_image) and product_image and product_image != 'None':
            return """<a href="/static/%s"><img border="0"
            alt="Error" src="/static/%s" height="50" />
            </a>""" % ((product_image, product_image))
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Product Image'

class ProductImages(models.Model):
    """
    model for Products
    """
    product = models.ForeignKey(Product, related_name='product')
    image_name = models.ImageField(upload_to='product_images/',
                                      help_text=('Image Size\
                                      should not more than 300kb.'),
                                      validators=[validate_product_image])
    sort_order = models.IntegerField()
    is_active = models.BooleanField(default=False,
                                   )
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """inner class"""
        verbose_name = 'product-image'
        verbose_name_plural = 'Product Images'
        
    def thumbnail(self):

        if default_storage.exists(self.image_name.name) and self.image_name.name and self.image_name.name != 'None':
            return """<img border="0"
            alt="Error" src="/static/%s" height="50" />
            """ % ((self.image_name.name))
        else:
            return 'Image Not Uploaded'
      
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Product Image'

    def __unicode__(self):
        return ''


class ProductTemplate(models.Model):
    """
    model for Products
    """
    category = models.ForeignKey(ProductCategory, related_name = 'product_category_template')
    product = models.ForeignKey(Product, related_name='product1', blank=True, null=True)
    template_name = models.CharField(max_length=50)
    image_name = models.ImageField(upload_to='product_template_images/',
                                      help_text=('Image Size\
                                      should not more than 300kb.'),
                                      validators=[validate_product_image])
    sort_order = models.IntegerField()
    is_active = models.BooleanField(default=False,
                                    )
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """inner class"""
        verbose_name = 'product-template'
        verbose_name_plural = 'Product Templates'
    
    def thumbnail(self):

        if default_storage.exists(self.image_name.name) and self.image_name.name and self.image_name.name != 'None':
            return """<img border="0"
            alt="Error" src="/static/%s" height="50" />
            """ % ((self.image_name.name))
        else:
            return 'Image Not Uploaded'
      
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Template Image'

    def __unicode__(self):
        return self.template_name


class ProductTemplateData(models.Model):
    """
    model for Products
    """
    product_template = models.ForeignKey(ProductTemplate, related_name='template_data')
    device_type = enum.EnumField(
        DataType, default=DataType.TEXT)
    left = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    default_text = models.CharField(max_length=30, null=True, blank=True)
    default_image = models.ImageField(upload_to='product_template_data/',
                                      help_text=('Image Size\
                                      should not more than 300kb.'),
                                      validators=[validate_product_image], null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """inner class"""
        verbose_name = 'product-template-data'
        verbose_name_plural = 'Product Templates Data'

    def __unicode__(self):
        return "Product Template %d" %(self.id)
    
    def thumbnail(self):
        if default_storage.exists(self.default_image.name) and self.default_image.name and self.default_image.name != 'None':
            return """<img border="0"
            alt="Error" src="/static/%s" height="50" />
            """ % ((self.default_image.name))
        else:
            return 'Image Not Uploaded'
     
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'
    
class ProductTemplateDataText(models.Model):
    """
    model for Products
    """
    product_template = models.ForeignKey(ProductTemplate, related_name='template_data_text')
    left = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    text = models.CharField(max_length=30, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """inner class"""
        verbose_name = 'product-template-data'
        verbose_name_plural = 'Product Templates Data'

    def __unicode__(self):
        return "Product Template %d" %(self.id)

class ProductTemplateDataImage(models.Model):
    """
    model for Products
    """
    product_template = models.ForeignKey(ProductTemplate, related_name='template_data_image')
    left = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_template_data/',
                                      help_text=('Image Size\
                                      should not more than 300kb.'),
                                      validators=[validate_product_image], null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """inner class"""
        verbose_name = 'product-template-data'
        verbose_name_plural = 'Product Templates Data'

    def __unicode__(self):
        return "Product Template %d" %(self.id)
    
    def thumbnail(self):
        if default_storage.exists(self.default_image.name) and self.default_image.name and self.default_image.name != 'None':
            return """<img border="0"
            alt="Error" src="/static/%s" height="50" />
            """ % ((self.default_image.name))
        else:
            return 'Image Not Uploaded'
     
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'
    
class EngraveMessage(models.Model):
    """
    model for Products
    """
    category = models.ForeignKey(ProductCategory, related_name = 'engrave_category')
    product = models.ForeignKey(Product, related_name='engrave_product')
    engrave_message = HTMLField()
    sort_order = models.IntegerField()
    is_active = models.BooleanField(default=False,
                                    )
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """inner class"""
        verbose_name = 'Engrave Message'
        verbose_name_plural = 'Engrave Message'

    def __unicode__(self):
        return self.engrave_message
    
