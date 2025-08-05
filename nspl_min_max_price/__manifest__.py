{
    'name': 'Lowest and Highest Price of Product',
    'version': '16.0',
    'summary': """Restrict sale price between min and max product price""",
    'description': """
This module ensures the sale price of products stays within defined minimum and maximum price limits. Useful for pricing control and validation on sales.

✔ Define minimum and maximum sale prices on products  
✔ Show warning if price is out of range on sale order lines  
✔ Allow saving but restrict confirmation without access rights  
✔ Grant override permission to specific user group  
✔ Helpful for enforcing pricing rules across sales team  
✔ Supports visibility of min/max near unit price field  

Perfect for businesses that want to maintain consistent pricing boundaries and approval-based overrides.
    """,
    'category': 'Sales',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'contributors': ['Khanak Hathi'],
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'price': 24.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'depends': ['sale_management', 'product'],
    'data': [
        'security/nspl_min_max_security.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/sale_order_view.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
