from Invoice_data.models import Item,Invoices
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['item_name', 'amount']

class InvoicesSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Invoices
        fields = ['id','invoice_number','seller','buyer','status','items']
        
    def create(self,validated_data):
        item_obj = validated_data.pop("items",[])
        invoice = Invoices.objects.create(**validated_data)
        for i in item_obj:
            obj = Item.objects.create(**i)
            invoice.items.add(obj)
        return invoice
    
class InvoicesStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoices
        fields = ['status',]
        
        
