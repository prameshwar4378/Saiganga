import django_filters
from django_filters import DateFilter
from .models import DB_Bills
from django import forms
from django.forms.widgets import TextInput

class Data_Filter(django_filters.FilterSet):
    cust_name=django_filters.CharFilter(widget=TextInput(attrs={'list':'cust_list'}))

    def __init__(self, *args, **kwargs):
        super(Data_Filter, self).__init__(*args, **kwargs)
        self.filters['cust_name'].label="Customer Name"
        self.filters['cust_mobile'].label="Mobile"
        self.filters['inv_chessis_1'].label="Chessis No"
        self.filters['inv_engine_1'].label="Engine No"

    class Meta:
        model = DB_Bills
        fields = ['branch','cust_name','cust_mobile','inv_chessis_1','inv_engine_1']
        widgets={
                'branch':django_filters.ChoiceFilter(attrs={'onkeyup':'auto_calculations(this.value);','placeholder':'Enter Customer Name'}),
                'cust_name':django_filters.CharFilter(attrs={'onkeyup':'auto_calculations(this.value);','placeholder':'Enter Customer Name'}),
        }