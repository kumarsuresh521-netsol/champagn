from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse
from product.models import ProductTemplate, ProductTemplateData
from app.mybarcode import MyBarcodeDrawing

def view_site(request):
    return render_to_response('index.html',)

def preview_tempate(request, preview_id):
    '''
        Preview Template Data
    '''
    product_template = ProductTemplate.objects.filter(id=preview_id).first()
    product_template_data = ProductTemplateData.objects.filter(product_template_id=preview_id)
    
    
    template = loader.get_template('admin/review_template.html')
    
    context = {
        'product_template': product_template,
        'product_template_data': product_template_data,
    }
    return HttpResponse(template.render(context, request))

def barcode(request):
    #instantiate a drawing object
    
    d = MyBarcodeDrawing("HELLO WORLD")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')