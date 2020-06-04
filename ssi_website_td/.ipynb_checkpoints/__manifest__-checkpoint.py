# -*- coding: utf-8 -*-
{
    'name': "SSI Website - Teacher Direct",


    'author': "Christian - SSI",
    'website': "http://ssibtr.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'SSI',
    'version': '13.0.0.1',
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': [
        'website',
        'website_sale',
    ],

    # always loaded
    'data': [
        'views/ssi_main_frontend_layout.xml',
        'views/ssi_search_box.xml',
        'views/ssi_main_layout.xml',
        'views/ssi_address_management.xml',
        'views/ssi_category_list.xml',
        'views/ssi_my_portal.xml',
        'views/ssi_payment.xml',
        'views/ssi_payment_tokens_list.xml',
        'views/ssi_portal_my_purchase_order.xml',
        'views/ssi_product.xml',
        'views/ssi_header_shop_my_cart_link.xml',
    ],
}