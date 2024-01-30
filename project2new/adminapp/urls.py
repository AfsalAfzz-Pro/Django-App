
from django.urls import path
from adminapp import views

urlpatterns = [
    path('',views.AdminPage, name = 'Admin'),
    path('add_record/',views.Add, name = 'add_record'),
    path('record/<id>',views.customer_record, name = 'customer_record'),
    path('delete_record/<id>',views.delete_record, name = 'Delete'),
    path('update_record/<id>',views.update_record, name = 'Edit'),
    # path('search/>',views.search, name = 'Search'),
    
    
]
