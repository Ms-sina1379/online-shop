class Cart:
    def __init__(self, request):
        self.session = request.session

        self.cart = self.session.get('product_id',)
        if "session_key" not in request.session:
            self.cart = self.session['product_id']={}
        self.cart = self.cart

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True


