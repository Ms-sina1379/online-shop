class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('session_key', {})  # Initialize cart from session
        if "session_key" in self.session:
            self.cart = self.session['session_key']

    def add(self, product):
        product_id = str(product['id'])
        if product_id not in self.cart:
            # Add new product to cart if it doesn't exist
            self.cart[product_id] = {'price': str(product['price'])}  # Assuming 'price' is a key in product
        else:
            # Update existing product's price
            self.cart[product_id]['price'] = str(product['price'])
        self.session.modified = True  # Save session changes


