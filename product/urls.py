'''
for handling urls of master app
'''
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from product.api import GetProductCategories, GetProductsByCategoryId, GetProductTemplates, GetProductTemplateDataById


urlpatterns = [
    url(r'^api/getcategories/$', GetProductCategories.as_view()),
    url(r'^api/getproductbyid/(?P<category_id>[0-9]+)/$', GetProductsByCategoryId.as_view()),
    url(r'^api/getproducttemplate/(?P<category_id>[0-9]+)/$', GetProductTemplates.as_view()),
    url(r'^api/getproducttemplatebyid/(?P<template_id>[0-9]+)/$', GetProductTemplateDataById.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
