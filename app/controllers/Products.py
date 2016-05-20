
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)

        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        products = self.models['Product'].show_products()
        return self.load_view('index.html', products=products)

    def new_product(self):
        return self.load_view('newproduct.html')

    def add_new(self):
        new_product = {
            "name": request.form['name'],
            "description": request.form['description'],
            "price": request.form['price'],
        }
        self.models['Product'].add_new_product(new_product)
        return redirect('/')

    def show(self,id):
        products = self.models['Product'].show_products_id(id)
        # print "RIGHT HERE"
        # print products
        return self.load_view('productinfo.html', products = products[0])

    def edit(self,id):
        products = self.models['Product'].show_products_id(id)
        return self.load_view('editproduct.html', products = products[0])

    def remove(self,id):
        product = self.models['Product'].remove_product(id)
        return redirect('/')

    def update(self,id):
        update_info = {
            "name": request.form['name'],
            "description": request.form['description'],
            "price": request.form['price'],
        }
        product = self.models['Product'].update_product(update_info, id)
        print product
        return redirect('/')
