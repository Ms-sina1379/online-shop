from shop.models import Products
class Cart:
    def __init__(self, request):
        self.session = request.session
        print(dict(self.session))
        self.cart = self.session.get('product_id',)
        if "product_id" not in request.session:
            self.cart = self.session['product_id']={}

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True

    def __len__(self):
            return len(self.cart)


    def get_prods(self):
        product_ids=self.cart.keys()
        products=Products.objects.filter(id__in=product_ids)
        return products



def global_product_counts(request):
    cart = request.session.get('product_id', {})
    product_ids = cart.keys()
    products = Products.objects.filter(id__in=product_ids)
    return {"products_count": products.count()}