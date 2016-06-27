'''
app serializers
'''
from rest_framework import serializers
from product.models import ProductCategory, Product, ProductImages, ProductTemplate, ProductTemplateData, ProductTemplateDataText, ProductTemplateDataImage



class ProductCategorySerializer(serializers.ModelSerializer):
    '''
    serializer for categories
    '''
    class Meta:
        '''
        meta for categories
        '''
        model = ProductCategory
        fields = ('id', 'name', 'logo_image', 'short_description', 'sort_order',
                  'occasion_start_date', 'occasion_end_date', 'create_date',)


class ProductSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    class Meta:
        '''
        meta for Products
        '''
        model = Product
        fields = ('id', 'name', 'desc', 'amount',
                  'capacity',)
        
class ProductImagesSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    class Meta:
        '''
        meta for Products
        '''
        model = ProductImages
        fields = ('id', 'image_name', 'sort_order',)


class ProductTemplateSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    class Meta:
        '''
        meta for Products
        '''
        model = ProductTemplate
        fields = ('id', 'category', 'product','template_name','image_name','sort_order',)

class ProductTemplateDataSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    class Meta:
        '''
        meta for Products
        '''
        model = ProductTemplateData
        fields = ('id', 'device_type', 'left','top','height','width','default_text','default_image',)
        
class ProductTemplateTextDataSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    class Meta:
        '''
        meta for Products
        '''
        model = ProductTemplateDataText
        fields = ('id', 'left','top','height','width','text',)
        
class ProductTemplateImageDataSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    class Meta:
        '''
        meta for Products
        '''
        model = ProductTemplateDataImage
        fields = ('id', 'left','top','height','width','image',)
        
class ProductTemplateWithDataSerializer(serializers.ModelSerializer):
    '''
    serializer for Products
    '''
    template_data_text = ProductTemplateTextDataSerializer(many=True)
    template_data_image = ProductTemplateImageDataSerializer(many=True)
    
    class Meta:
        '''
        meta for Products
        '''
        model = ProductTemplate
        fields = ('id', 'category', 'product','template_name','image_name','sort_order','template_data_text','template_data_image',)