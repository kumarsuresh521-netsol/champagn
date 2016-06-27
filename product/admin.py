from django.contrib import admin
from product.models import Product, ProductCategory, ProductImages, ProductTemplate, ProductTemplateData, ProductTemplateDataText, ProductTemplateDataImage, EngraveMessage
from django.conf import settings
from django.contrib.admin import AdminSite
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.db.models.fields.files import FileField
from django import forms
from product import models
from tinymce.widgets import TinyMCE

AdminSite.site_header = 'The ChampagnFizz Administration'
AdminSite.site_title = 'The ChampagnFizz'


class AdminOccasionShowImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        flag = False
        if value and getattr(value, "url", None):
            image_url = value.url
            image_url = '/static/' + image_url
            output.append(u' <a href="%s" target="_blank"><img style="width:280px;" src="%s"/></a> ' % \
                (image_url, image_url))
            file_field = FileField()
            file_field.name = image_url
            file_field.path = value.path
            file_field.url = '/static/' + value.name
            file_field.model = ProductCategory
            flag = True

        if flag:
            output.append(super(AdminFileWidget, self).render(name,
                                                              file_field,
                                                              attrs))
        else:
            output.append(super(AdminFileWidget, self).render(name,
                                                              value,
                                                              attrs))
        return mark_safe(u''.join(output))


class CategoryCustomForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    def clean(self):
        start_date = self.cleaned_data.get("occasion_start_date")
        end_date = self.cleaned_data.get("occasion_end_date")

        if start_date:
            if end_date:
                msg = u""
            else:
                msg = u"Enter Occasion end date."
                self._errors["occasion_end_date"] = self.error_class([msg])
            
        if end_date:
            if start_date:
                msg = u""
            else:
                msg = u"Enter Occasion start date."
                self._errors["occasion_start_date"] = self.error_class([msg])
        
        if start_date and start_date != None and end_date and end_date != None and end_date < start_date:
            msg = u"Occasion end date should be greater than start date."
            self._errors["occasion_end_date"] = self.error_class([msg])
            
class OccasionsAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Business Rating model
    """
    form = CategoryCustomForm
    list_display = ['name','thumbnail','occasion_start_date', 'occasion_end_date',  'sort_order', 'is_active']
    search_fields = ['name', 'short_description']
    list_per_page = settings.ADMIN_PAGE_SIZE

#    Default Select Options in Action
    BLANK_CHOICE_DASH = [("", "Select options")]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'logo_image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminOccasionShowImageWidget
            return db_field.formfield(**kwargs)
        return super(OccasionsAdmin,self).formfield_for_dbfield(db_field, **kwargs)
            
class ProductMultipleImagesInline(admin.TabularInline):
    model = ProductImages
    fields = ("is_active", "sort_order", "image_name","thumbnail")
    verbose_name = "Image"
    verbose_name_plural = "Product Images"
    extra = 0
    show_change_link = False
    readonly_fields = ('thumbnail',)
    
 
 
class ProductImageShowImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        flag = False
        if value and getattr(value, "url", None):
            image_url = value.url
            image_url = '/static/' + image_url
            output.append(u' <a href="%s" target="_blank"><img style="width:280px;" src="%s"/></a> ' % \
                (image_url, image_url))
            file_field = FileField()
            file_field.name = image_url
            file_field.path = value.path
            file_field.url = '/static/' + value.name
            file_field.model = Product
            flag = True

        if flag:
            output.append(super(AdminFileWidget, self).render(name,
                                                              file_field,
                                                              attrs))
        else:
            output.append(super(AdminFileWidget, self).render(name,
                                                              value,
                                                              attrs))
        return mark_safe(u''.join(output))

      
class ProductAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Products model
    """
    list_display = ['name', 'amount', 'capacity', 'is_active']
    search_fields = ['name', 'desc']
    list_per_page = settings.ADMIN_PAGE_SIZE
    inlines = [ProductMultipleImagesInline]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image_name':
            request = kwargs.pop("request", None)
            kwargs['widget'] = ProductImageShowImageWidget
            return db_field.formfield(**kwargs)
        return super(ProductAdmin,self).formfield_for_dbfield(db_field, **kwargs)

    
class AdminImageShowImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        flag = False
        if value and getattr(value, "url", None):
            image_url = value.url
            image_url = '/static/' + image_url
            output.append(u' <a href="%s" target="_blank"><img style="width:280px;" src="%s"/></a> ' % \
                (image_url, image_url))
            file_field = FileField()
            file_field.name = image_url
            file_field.path = value.path
            file_field.url = '/static/' + value.name
            file_field.model = ProductImages
            flag = True

        if flag:
            output.append(super(AdminFileWidget, self).render(name,
                                                              file_field,
                                                              attrs))
        else:
            output.append(super(AdminFileWidget, self).render(name,
                                                              value,
                                                              attrs))
        return mark_safe(u''.join(output))


class ProductImagesAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Products Images
    """
#    Default Select Options in Action
    BLANK_CHOICE_DASH = [("", "Select options")]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image_name':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageShowImageWidget
            return db_field.formfield(**kwargs)
        return super(ProductImagesAdmin,self).formfield_for_dbfield(db_field, **kwargs)
    
class ProductTemplateTextDataInline(admin.TabularInline):
    model = ProductTemplateDataText
    verbose_name = "Template Text"
    verbose_name_plural = "Template Text"
    show_change_link = False
    min_num = 1
    extra = 0
    
class ProductTemplateImageDataInline(admin.TabularInline):
    model = ProductTemplateDataImage
    verbose_name = "Template Image"
    verbose_name_plural = "Template Image"
    extra = 0
    show_change_link = False
    max_num = 1
    min_num = 1
    can_delete = False
    readonly_fields = ('thumbnail',)
    
class ProductImagesTemplateAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Products Images
    """
    list_display = ['template_name', 'thumbnail', 'sort_order', 'is_active']
    search_fields = ['template_name']
    list_per_page = settings.ADMIN_PAGE_SIZE
#    Default Select Options in Action
    BLANK_CHOICE_DASH = [("", "Select options")]
    inlines = [ProductTemplateImageDataInline, ProductTemplateTextDataInline]


class AdminProductTemplateDataShowImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        flag = False
        if value and getattr(value, "url", None):
            image_url = value.url
            image_url = '/static/' + image_url
            output.append(u' <a href="%s" target="_blank"><img style="width:280px;" src="%s"/></a> ' % \
                (image_url, image_url))
            file_field = FileField()
            file_field.name = image_url
            file_field.path = value.path
            file_field.url = '/static/' + value.name
            file_field.model = ProductTemplateData
            flag = True

        if flag:
            output.append(super(AdminFileWidget, self).render(name,
                                                              file_field,
                                                              attrs))
        else:
            output.append(super(AdminFileWidget, self).render(name,
                                                              value,
                                                              attrs))
        return mark_safe(u''.join(output))
    
    
class ProductImagesTemplateDataAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Products Images
    """
#    Default Select Options in Action
    BLANK_CHOICE_DASH = [("", "Select options")]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'default_image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminProductTemplateDataShowImageWidget
            return db_field.formfield(**kwargs)
        return super(ProductImagesTemplateDataAdmin,self).formfield_for_dbfield(db_field, **kwargs)
    
class EngraveMessagesAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Privacy model
    """
    list_display = ['engrave_message', 'create_date']
    search_fields = ['engrave_message']
    list_per_page = settings.ADMIN_PAGE_SIZE
    formfield_overrides = {
        models.HTMLField: {'widget': TinyMCE(
                        attrs={'rows': 0,
                            'cols': 36,
                            'style': 'height: 3em;'},
                        #mce_attrs={'external_link_list_url': reverse('someapp.views.someview')}
                    )},
    }
    actions = None
       
admin.site.register(ProductCategory, OccasionsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(ProductTemplate, ProductImagesTemplateAdmin)
admin.site.register(ProductTemplateData, ProductImagesTemplateDataAdmin)
admin.site.register(EngraveMessage, EngraveMessagesAdmin)