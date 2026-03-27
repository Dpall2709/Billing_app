from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('add_mill/', views.add_mill, name='add_mill'),
    path('mills/', views.mill_list, name='mill_list'),
    path('mills/edit/<int:mill_id>/', views.edit_mill, name='edit_mill'),
    path('mills/delete/<int:mill_id>/', views.delete_mill, name='delete_mill'),
    
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path("products/report/<int:product_id>/", views.product_report, name="product_report"),



    path("purchase/add/", views.add_purchase, name="add_purchase"),
    path("purchase/list/", views.purchase_list, name="purchase_list"),
    path("purchase/<int:purchase_id>/", views.purchase_detail, name="purchase_detail"),
    path("purchase/edit/<int:purchase_id>/", views.edit_purchase, name="edit_purchase"),
    path("purchase/delete/<int:purchase_id>/", views.delete_purchase, name="delete_purchase"),
    path("payment/purchase/add/<int:purchase_id>/", views.add_purchase_payment, name="add_purchase_payment"),


    path("mills/report/<int:mill_id>/", views.mill_report_detail, name="mill_report_detail"),
    path("payment/mill/add/<int:mill_id>/", views.add_mill_payment, name="add_mill_payment"),
    path("mills/<int:mill_id>/export/excel/", views.mill_report_excel, name="mill_report_excel"),
    path("mills/<int:mill_id>/export/pdf/", views.mill_report_pdf, name="mill_report_pdf"),

    path("sales/", views.sale_list, name="sale_list"),
    path("sales/add/", views.add_sale, name="add_sale"),
    path("sales/review/", views.sale_review, name="sale_review"),
    path("sales/confirm-save/", views.sale_confirm_save, name="sale_confirm_save"),
    path("sales/<int:sale_id>/", views.sale_detail, name="sale_detail"),
    path("sales/<int:sale_id>/print/", views.sale_print, name="sale_print"),
    path("sales/<int:sale_id>/payment/add/", views.add_sale_payment, name="add_sale_payment"),


    path("brokers/", views.broker_list, name="broker_list"),
    path("brokers/add/", views.add_broker, name="add_broker"),
    path("brokers/report/<int:broker_id>/", views.broker_report_detail, name="broker_report_detail"),
    path("sales/<int:sale_id>/invoice.pdf", views.sale_invoice_pdf, name="sale_invoice_pdf"),





]