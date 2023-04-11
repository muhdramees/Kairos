
from django.urls import path
from .import views


urlpatterns = [
        path('', views.admin_login , name="admin_login"),
        path('dashboard/', views.admin_dashboard, name="admin_dashboard"),
        path('admin-logout/', views.admin_logout , name="admin_logout"),
        path('user-view/', views.user_view , name="user_view"),
        path('admin-registration/', views.admin_registration , name="admin_registration"),
        path('blockuser/<int:id>', views.block_user , name="block_user"),
        path('category/', views.product_category, name="product_category"),
        path('category/<str:slug>', views.category_view, name="category_view"),
        path('addproduct/', views.add_product, name="add_product"),
        path('edit-user/<int:id>', views.edit_user , name="edit_user"),
        path('deleteproduct/<product_id>', views.delete_product, name="delete_product"),
#        _deleteuser/<int:pk>/delete/', views.delete_user, name="delete_user"),


        path('edit-category/<category_id>', views.edit_category, name="edit_category"),



        path('edit-product/<product_id>', views.edit_product, name="edit_product"),



       
        path('add-category/', views.add_category, name="add_category"),
        path('delete-category/<category_id>', views.delete_category, name="delete_category"),
        path('add-category-offer/',views.add_category_offer,name='add_category_offer'),
        path('add-product-offer/',views.add_product_offer,name='add_product_offer'),


        path('category-offer/',views.category_offer,name='category_offer'),
        path('edit-category-offer/<category_id>',views.edit_category_offer,name='edit_category_offer'),
        path('delete-category-offer/<int:id>',views.delete_category_offer,name='delete_category_offer'),
        





        path('product-offer/',views.product_offers,name='product_offers'),
        path('delete-product-offer/<int:id>',views.delete_product_offer,name='delete_product_offer'),
        path('edit-product-offer/<product_id>',views.edit_product_offer,name='edit_product_offer'),
        


        # report
        # path('product-offer/',views.product_offers,name='product_offers'),
        # path('product-csv/',views.product_csv,name='product_csv'),
        # path('generate-product-pdf/',views.generateProductPdf,name='generateProductPdf'),
        # path('product-excel/',views.product_excel,name='product_excel'),
        


        # sales report
        path('sales-report/',views.sales_report,name='sales_report'),
        path('by-date/',views.by_date,name='by_date'),
        path('generates-sales-report/',views.generates_sales_report.as_view(),name='generates_sales_report'),
        path('by-month/',views.by_month,name='by_month'),
        path('by-year/',views.by_year,name='by_year'),
        path('download-docx/',views.download_docx,name='download_docx'),






]