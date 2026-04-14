from .models import Product
def get_product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return None