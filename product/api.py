'''
for handling all the action redirected from urls
'''
import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from champagn.utility import FizzUtility
from product.models import ProductCategory,Product, ProductImages, ProductTemplate
from champagn import settings
from django.db import connection


class GetProductCategories(generics.ListAPIView):
    '''
    API to return All Product Active Categories
    '''
    @classmethod
    def get(self, request, *args):
#         category_list = ProductCategory.objects.filter(is_active=True).order_by('sort_order', 'occasion_start_date',  'name')
#         cursor = connection.cursor()
   
#         cursor.execute("SELECT *,case when occasion_start_date > now() or now() < occasion_end_date then 1 else 2 end as order_ FROM public.product_productcategory WHERE is_active=True order by order_,occasion_start_date asc")
#         category_list = cursor.fetchall()
        
#         if category_list.count() > 0:
#             status_code = status.HTTP_200_OK
#         else:
#             status_code = settings.HTTP_USER_ERROR
        category_list = ProductCategory.objects.raw("SELECT *,case when occasion_start_date > now() or now() < occasion_end_date then 1 else 2 end as order_ FROM public.product_productcategory WHERE is_active=True order by order_,occasion_start_date asc")
        
        status_code = status.HTTP_200_OK
              
        response_data = {}
        serializer = serializers.ProductCategorySerializer(category_list, many=True)
        response_data['Categories'] = serializer.data
#         response_data['Categories'] = category_list
        response = FizzUtility.data_wrapper(response_data, status_code=status_code)
        return Response(response, status=status.HTTP_200_OK)


class GetProductsByCategoryId(generics.ListAPIView): 
    '''
    API to return Product By Category Id Filter is active True / return only 5 products / Order By sort_order or image_name
    '''
    @classmethod
    def get(self, request, category_id):
        response_data = {}
        serializer_data = []
        
        cursor = connection.cursor()

        cursor.execute("Select product_id FROM public.product_product_category WHERE productcategory_id = %s", [category_id])
    
        category_product = cursor.fetchall()
         
        for productCat in category_product:
            product_data = Product.objects.filter(id = productCat[0], is_active=True)
            serializer = serializers.ProductSerializer(product_data, many=True)
             
            for product in serializer.data:
                product_images = ProductImages.objects.filter(product_id = product.get('id'), is_active=True).order_by('sort_order')[:5]
                serializer_image = serializers.ProductImagesSerializer(product_images, many=True)
                product_data = product
                product_data['images'] = serializer_image.data
             
            serializer_data.append(product_data)
        
        if len(category_product) > 0:
            status_code = status.HTTP_200_OK
        else:
            status_code = settings.HTTP_USER_ERROR
             
        response_data['products'] = serializer_data
        response = FizzUtility.data_wrapper(response_data, status_code=status_code)
        return Response(response, status=status.HTTP_200_OK)


class GetProductTemplates(generics.ListAPIView):
    '''
    API to return All Product Active Categories
    '''
    @classmethod
    def get(self, request, category_id):
        template_list = ProductTemplate.objects.filter(category_id = category_id, is_active=True).order_by('sort_order')[:5]
        
        if template_list.count() > 0:
            status_code = status.HTTP_200_OK
        else:
            status_code = settings.HTTP_USER_ERROR
            
        response_data = {}
        serializer = serializers.ProductTemplateSerializer(template_list, many=True)
        response_data['Templates'] = serializer.data
        response = FizzUtility.data_wrapper(response_data, status_code=status_code)
        return Response(response, status=status.HTTP_200_OK)
    
class GetProductTemplateDataById(generics.ListAPIView):
    '''
    API to return All Product Active Categories
    '''
    @classmethod
    def get(self, request, template_id):
        template = ProductTemplate.objects.filter(id = template_id, is_active=True)
        
        if template:
            status_code = status.HTTP_200_OK
        else:
            status_code = settings.HTTP_USER_ERROR
            
        response_data = {}
        serializer = serializers.ProductTemplateWithDataSerializer(template, many=True)
        response_data['TemplatesData'] = serializer.data
        response = FizzUtility.data_wrapper(response_data, status_code=status_code)
        return Response(response, status=status.HTTP_200_OK)
