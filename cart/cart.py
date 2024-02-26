
from shop.models import Products

CART_SESSION_ID = 'cart'
class Cart(object):
    def __init__(self, request):
        self.products = None
        self.session = request.session
        print(dict(self.session))
        self.cart = self.session.get('product_id', {})
        if "product_id" not in request.session:
            self.cart = self.session['product_id'] = {}

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = product_qty
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)
        return products

    def get_quantity(self):
        quantity = self.cart
        return quantity

    def remove_item(self, itemid):
        itemid = str(itemid)
        if itemid in self.cart:
            del self.cart[itemid]
            self.session.modified = True

def global_product_counts(request):
    cart = request.session.get('product_id', {})
    product_ids = cart.keys()
    products = Products.objects.filter(id__in=product_ids)
    return {"products_count": products.count()}