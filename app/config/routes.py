
from system.core.router import routes

routes['default_controller'] = 'Products'
routes['GET']['/products/new_product'] = 'Products#new_product'
routes['POST']['/products/add_new'] = 'Products#add_new'
routes['GET']['/products/show/<id>'] = 'Products#show'
routes['GET']['/products/edit/<id>'] = 'Products#edit'
routes['POST']['/products/destroy/<id>'] = 'Products#remove'
routes['POST']['/products/update/<id>'] = 'Products#update'
