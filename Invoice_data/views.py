from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from Invoice_data.models import Item, Invoices
from Invoice_data.serializers import ItemSerializer, InvoicesSerializer, InvoicesStatusSerializer
from django.conf import settings
from Invoice_data.function import make_pages


class Invoice_list(APIView):
    '''To get list of all pdf content with pagination function (make_pages). each page contain 3 pdf data '''
    
    def get(self, request, page, format=None):
        obj = Invoices.objects.all()
        '''pagination to show 3 invoice data on one page'''
        
        pageQuery,pageData=make_pages(obj, 3, request.GET, request.build_absolute_uri())
        data = InvoicesSerializer(pageQuery,many=True)       
        return Response({"page":pageData,"data":data.data})


    '''  mock data for upload pdf , data={"invoice_number":"INV123","seller":"Rohan","buyer":"Shamal","digitized":true,"items":[{"item_name":"Saree","amount":2000}]}'''
    def post(self, request,format=None):
        serializer = InvoicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class InvoicesDetail(APIView):
    def get_object(self, pk):
        try:
            return Invoices.objects.get(pk=pk)
        except Invoices.DoesNotExist:
            raise Http404
        
    '''To get Particular pdf data details by passing id to it'''
    
    def get(self, request, pk, format=None):
        Invoice = self.get_object(pk)
        obj = Invoices.objects.get(pk=pk)
        serializer = InvoicesSerializer(obj)
        return Response(serializer.data)
    

    '''to staff member edit data of pdf with status'''
    
    def put(self, request, pk, format=None):
        Invoice = self.get_object(pk)
        serializer = InvoicesSerializer(Invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
'''Search perticular  pdf Data by passing  invoice_number''' 

class SearchInvoice(APIView):
    
    def get_object(self, invoice_number):
        try:
            return Invoices.objects.get(invoice_number=invoice_number)
        except Invoices.DoesNotExist:
            raise Http404

    def get(self, request, invoice_number, format=None):
        Invoice = self.get_object(invoice_number)
        obj = Invoices.objects.get(invoice_number=invoice_number)
        serializer = InvoicesSerializer(obj)
        return Response(serializer.data)
    

''' To get Specific pdf status digitized or non digitized. If digitized user can able to see data with it. If status
    is non digitized it show only status'''   
class InvoiceStatus(APIView):
    
    def get_object(self, pk):
        try:
            return Invoices.objects.filter(pk=pk,status='digitized')
        except Invoices.DoesNotExist:
            raise Http404
        
        
    def get(self, request, pk, format=None):
        Invoice = self.get_object(pk)
        obj = Invoices.objects.get(pk=pk)
        if obj:
            serializer = InvoicesSerializer(obj)
            return Response(serializer.data)
        return Response({"status":"undigitized"})