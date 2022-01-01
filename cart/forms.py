from django import forms
from django.utils.translation import override
from wheely.models import Size

PRODUCT_QTY_CHOICE = [(i,str(i)) for i in range(1,21) ]
sizes = Size.objects.all()
PRODUCT_SIZE_CHOICE = [(s,str(s)) for s in sizes ]

class CartAddProductForm(forms.Form):
    qty = forms.TypedChoiceField(choices=PRODUCT_QTY_CHOICE)
    size = forms.TypedChoiceField(choices=PRODUCT_SIZE_CHOICE)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
 