from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Home, name='home'),
    path("add_customer/",views.add_customer, name='add_customer'),
    path("all_bills/",views.all_bills, name='all_bills'),  
    path("customer_dashboard/<int:id>",views.customer_dashboard, name='customer_dashboard'),  

    path("generate_invoice/<int:id>",views.invoice_form, name='generate_invoice'),
    path("generate_quotation/<int:id>",views.quotation_form, name='generate_quotation'),
    path("delivery_challan/<int:id>",views.delivery_challan_form, name='delivery_challan'),
    path("margin_money/<int:id>",views.margin_money_form, name='margin_money'),

    path("update_generate_invoice/<int:id>",views.update_invoice_form, name='update_generate_invoice'),
    path("update_generate_quotation/<int:id>",views.update_quotation_form, name='update_generate_quotation'),
    path("update_delivery_challan/<int:id>",views.update_delivery_challan_form, name='update_delivery_challan'),
    path("update_margin_money/<int:id>",views.update_margin_money_form, name='update_margin_money'),

    path("print_invoice/<int:id>",views.print_invoice, name='print_invoice'),
    path("print_quotation/<int:id>",views.print_quotation, name='print_quotation'), 
    path("print_delivery_challan/<int:id>",views.print_delivery_challan, name='print_delivery_challan'),  

    path("quotation_export/",views.export_excel_quotation, name='quotation_export'),  
    path("invoice_export/",views.export_excel_invoice, name='invoice_export'),  
    path("delivery_challan_export/",views.export_excel_delivery_challan, name='delivery_challan_export'),  
    path("margin_money_export/",views.export_excel_margin_money, name='margin_money_export'),  
    
    path("delete_customer/<int:id>",views.delete_customer, name='delete_customer'),  
    path("update_customer/<int:id>",views.update_customer, name='update_customer'),  

    path("order_list/",views.order_list, name='order_list'),    
    path("enquiry_list/",views.enquiry_list, name='enquiry_list'),     

    path("update_profile/<int:id>",views.update_profile, name='update_profile'),  
    path("login/",views.user_login, name='login'),   
    path("logout/",views.user_logout, name='logout'),  

    path("print_margin_money1/<int:id>",views.print_margin_money1, name='print_margin_money1'),   
    path("print_margin_money2/<int:id>",views.print_margin_money2, name='print_margin_money2'),   
    path("print_margin_money3/<int:id>",views.print_margin_money3, name='print_margin_money3'),    
    path("print_margin_money4/<int:id>",views.print_margin_money4, name='print_margin_money4'),   
    path("print_margin_money5/<int:id>",views.print_margin_money5, name='print_margin_money5'),   
    path("print_margin_money6/<int:id>",views.print_margin_money6, name='print_margin_money6'),   
    path("print_margin_money7/<int:id>",views.print_margin_money7, name='print_margin_money7'),    
    path("print_margin_money8/<int:id>",views.print_margin_money8, name='print_margin_money8'),   
    path("print_margin_money9/<int:id>",views.print_margin_money9, name='print_margin_money9'),   
    path("print_margin_money10/<int:id>",views.print_margin_money10, name='print_margin_money10'),   
    path("print_margin_money11/<int:id>",views.print_margin_money11, name='print_margin_money11'),   
    path("print_margin_money12/<int:id>",views.print_margin_money12, name='print_margin_money12'),   
    path("print_margin_money13/<int:id>",views.print_margin_money13, name='print_margin_money13'),   
    path("print_margin_money14/<int:id>",views.print_margin_money14, name='print_margin_money14'),   
    path("print_margin_money15/<int:id>",views.print_margin_money15, name='print_margin_money15'),    
    

]
