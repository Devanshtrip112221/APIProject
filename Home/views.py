from django.views.generic import View
from django.http import HttpResponse
from Home.models import Product
from Home.serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class ProductCRUDCBV(View):

    
    def get(self, request, *args, **kwargs):
        json_data = request.body
        
        if json_data:
           
            stream = io.BytesIO(json_data)
            pdata = JSONParser().parse(stream)
            product_id = pdata.get('id')
            
            if product_id:
                try:
                    product = Product.objects.get(id=product_id)
                    serializer = ProductSerializer(product)
                    json_data = JSONRenderer().render(serializer.data)
                    return HttpResponse(json_data, content_type='application/json')
                except Product.DoesNotExist:
                    return HttpResponse(
                        json.dumps({'error': 'Product not found'}),
                        content_type='application/json',
                        status=404
                    )
        
      
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


    def post(self, request, *args, **kwargs):
        stream = io.BytesIO(request.body)
        pdata = JSONParser().parse(stream)
        
        serializer = ProductSerializer(data=pdata)
        
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(
                json.dumps({'msg': 'Product Created Successfully', 'product': serializer.data}),
                content_type='application/json',
                status=201
            )
        
        return HttpResponse(
            json.dumps({'errors': serializer.errors}),
            content_type='application/json',
            status=400
        )


    def put(self, request, *args, **kwargs):
        stream = io.BytesIO(request.body)
        pdata = JSONParser().parse(stream)
        
        product_id = pdata.get('id')
        if not product_id:
            return HttpResponse(
                json.dumps({'error': 'Product ID is required for update'}),
                content_type='application/json',
                status=400
            )
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return HttpResponse(
                json.dumps({'error': 'Product not found'}),
                content_type='application/json',
                status=404
            )
        
      
        serializer = ProductSerializer(product, data=pdata, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(
                json.dumps({'msg': 'Product Updated Successfully', 'product': serializer.data}),
                content_type='application/json'
            )
        
        return HttpResponse(
            json.dumps({'errors': serializer.errors}),
            content_type='application/json',
            status=400
        )


    def delete(self, request, *args, **kwargs):
        stream = io.BytesIO(request.body)
        pdata = JSONParser().parse(stream)
        
        product_id = pdata.get('id')
        if not product_id:
            return HttpResponse(
                json.dumps({'error': 'Product ID is required for deletion'}),
                content_type='application/json',
                status=400
            )
        
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return HttpResponse(
                json.dumps({'msg': f'Product "{product.product_name}" Deleted Successfully'}),
                content_type='application/json'
            )
        except Product.DoesNotExist:
            return HttpResponse(
                json.dumps({'error': 'Product not found'}),
                content_type='application/json',
                status=404
            )