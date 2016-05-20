
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def show_products(self):
        show_query = "SELECT * FROM products"
        return self.db.query_db(show_query)

    def add_new_product(self, new_info):
        add_query = "INSERT INTO products (product_name, product_description, product_price, created_at) VALUES(:product_name, :product_description, :product_price, NOW())"
        add_data = {
            'product_name': new_info['name'],
            'product_description': new_info['description'],
            'product_price': new_info['price'],
        }
        return self.db.query_db(add_query, add_data)

    def show_products_id(self, id):
        show_id_query = "SELECT * FROM products WHERE id= :id"
        data = {
            'id':id
        }
        return self.db.query_db(show_id_query, data)

    def remove_product(self,id):
        remove_query = "DELETE FROM products WHERE id= :id"
        data = {'id': id}
        return self.db.query_db(remove_query, data)

    def update_product(self,info, id):
        update_query = "UPDATE products SET product_name=:name, product_description=:description, product_price=:price WHERE id= :id"
        update_data = {
            'name': info['name'],
            'description': info['description'],
            'price': info['price'],
            'id': id
        }
        return self.db.query_db(update_query, update_data)
