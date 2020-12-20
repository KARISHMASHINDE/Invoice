from django.urls import path
from . import views



urlpatterns = [

    path('invoice/data/<int:page>/', views.Invoice_list.as_view()),
    path('invoice/details/<int:pk>/', views.InvoicesDetail.as_view()),
    path('invoice/search/<str:invoice_number>/', views.SearchInvoice.as_view()),
    path('invoice/status/<int:pk>/', views.InvoiceStatus.as_view()),
]