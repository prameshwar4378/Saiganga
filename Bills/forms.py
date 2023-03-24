from cProfile import label
from xml.dom.minidom import Attr
from django import forms
from .models import DB_Bills
from django.contrib.auth.forms  import AuthenticationForm


class Form_calculator(forms.Form):
   

    Before_Amount=forms.IntegerField(required=False,widget= forms.NumberInput(attrs={'placeholder':'GST Amount','onkeyup':'gst_calculator(this.value);'}))
    CGST_Amount=forms.IntegerField(required=False,widget= forms.NumberInput (attrs={'placeholder':'CGST Amount','onkeyup':'gst_calculator(this.value);'}))
    SGST_Amount=forms.IntegerField(required=False,widget= forms.NumberInput (attrs={'placeholder':'SGST Amount','onkeyup':'gst_calculator(this.value);'}))
    After_Amount=forms.IntegerField(required=False,widget= forms.NumberInput(attrs={'placeholder':'Actual Amount','onkeyup':'gst_calculator(this.value);'}))
    
    def __init__(self, *args, **kwargs):
            super(Form_calculator, self).__init__(*args, **kwargs)
            self.fields['Before_Amount'].label = "GST Amount"
            self.fields['CGST_Amount'].label = "CGST_Amount"
            self.fields['SGST_Amount'].label = "SGST_Amount"
            self.fields['After_Amount'].label = "Actual Amount"
    


class Form_Manage_Customer(forms.ModelForm):
    class Meta:
        model = DB_Bills
        fields = ('cust_name','cust_mobile','cust_village','cust_taluka','cust_dist','cust_pin_code','branch')


class Form_Invoice(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form_Invoice, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['inv_amount_1'].widget.attrs['readonly'] = True
            self.fields['inv_amount_2'].widget.attrs['readonly'] = True
            self.fields['inv_amount_3'].widget.attrs['readonly'] = True
            self.fields['inv_amount_4'].widget.attrs['readonly'] = True
            self.fields['inv_amount_5'].widget.attrs['readonly'] = True
            self.fields['inv_amount_6'].widget.attrs['readonly'] = True

            self.fields['inv_sub_total'].widget.attrs['readonly'] = True
            self.fields['cust_name'].widget.attrs['readonly'] = True
            self.fields['inv_grand_total'].widget.attrs['readonly'] = True
            self.fields['inv_sgst'].widget.attrs['readonly'] = True
            self.fields['inv_cgst'].widget.attrs['readonly'] = True


    class Meta:
        model = DB_Bills
        fields = ('cust_name','cust_mobile','cust_village','cust_taluka','cust_dist',
                   'other_reference','inv_no','inv_date','inv_amt_in_word',
                   'inv_description_1','inv_chessis_1','inv_engine_1','inv_qty_1','inv_rate_1','inv_amount_1',
                   'inv_description_2','inv_chessis_2','inv_engine_2','inv_qty_2','inv_rate_2','inv_amount_2',
                   'inv_description_3','inv_chessis_3','inv_engine_3','inv_qty_3','inv_rate_3','inv_amount_3',
                   'inv_description_4','inv_chessis_4','inv_engine_4','inv_qty_4','inv_rate_4','inv_amount_4',
                   'inv_description_5','inv_chessis_5','inv_engine_5','inv_qty_5','inv_rate_5','inv_amount_5',
                   'inv_description_6','inv_chessis_6','inv_engine_6','inv_qty_6','inv_rate_6','inv_amount_6',
                   'inv_sub_total','inv_grand_total','inv_sgst','inv_cgst','inv_rto',
                   )

        widgets={
                'inv_date':forms.NumberInput(attrs={'type':'date'}) ,
                'inv_qty_1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords();'}),
                'inv_qty_2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_qty_3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_qty_4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_qty_5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_qty_6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                
                'inv_rate_1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords(); '}),
                'inv_rate_2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_rate_3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_rate_4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_rate_5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'inv_rate_6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                
                'inv_amount_1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); '}),
                'inv_amount_2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); '}),
                'inv_amount_3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); '}),
                'inv_amount_4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); '}),
                'inv_amount_5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); '}),
                'inv_amount_6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); '}),
               
                'inv_sub_total':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'inv_grand_total':forms.NumberInput(attrs={'class':'form-control'}),
                'inv_sgst':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'inv_cgst':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'inv_rto':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),

        }

        labels = {
        "cust_name": "Customer Name",'cust_village':'Village','cust_taluka':'Taluka','cust_dist':'Dist','cust_mobile':'Mobile',
        'other_reference':'Other Reference','inv_no':'Invoice No','inv_date':'Date','inv_sub_total':'Sub Total','inv_grand_total':'Grand Total',
        'inv_sgst':'SGST 6%','inv_cgst':'IGST 6%','inv_rto':'RTO',
        'inv_description_1':'Description','inv_chessis_1':'Chessis No','inv_engine_1':'Engine No','inv_qty_1':'Qty','inv_rate_1':'Rate','inv_amount_1':'Amount',
        'inv_description_2':'Description','inv_chessis_2':'Chessis No','inv_engine_2':'Engine No','inv_qty_2':'Qty','inv_rate_2':'Rate','inv_amount_2':'Amount',
        'inv_description_3':'Description','inv_chessis_3':'Chessis No','inv_engine_3':'Engine No','inv_qty_3':'Qty','inv_rate_3':'Rate','inv_amount_3':'Amount',
        'inv_description_4':'Description','inv_chessis_4':'Chessis No','inv_engine_4':'Engine No','inv_qty_4':'Qty','inv_rate_4':'Rate','inv_amount_4':'Amount',
        'inv_description_5':'Description','inv_chessis_5':'Chessis No','inv_engine_5':'Engine No','inv_qty_5':'Qty','inv_rate_5':'Rate','inv_amount_5':'Amount',
        'inv_description_6':'Description','inv_chessis_6':'Chessis No','inv_engine_6':'Engine No','inv_qty_6':'Qty','inv_rate_6':'Rate','inv_amount_6':'Amount',
    }


    
class Form_Quotation(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form_Quotation, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['qtn_amt1'].widget.attrs['readonly'] = True
            self.fields['qtn_amt2'].widget.attrs['readonly'] = True
            self.fields['qtn_amt3'].widget.attrs['readonly'] = True
            self.fields['qtn_amt4'].widget.attrs['readonly'] = True
            self.fields['qtn_amt5'].widget.attrs['readonly'] = True
            self.fields['qtn_amt6'].widget.attrs['readonly'] = True
            self.fields['qtn_amt7'].widget.attrs['readonly'] = True
            self.fields['qtn_amt8'].widget.attrs['readonly'] = True
            self.fields['qtn_amt9'].widget.attrs['readonly'] = True
            self.fields['qtn_amt10'].widget.attrs['readonly'] = True

            self.fields['qtn_total_amount'].widget.attrs['readonly'] = True
            self.fields['cust_name'].widget.attrs['readonly'] = True

    class Meta:
        model = DB_Bills
        fields = ('qtn_total_amount','qtn_no','qtn_date','qtn_amt_in_word',
        'cust_name','cust_mobile','cust_village','cust_taluka','cust_dist',
        'qtn_description1','qtn_qty1','qtn_rate1','qtn_amt1',
        'qtn_description2','qtn_qty2','qtn_rate2','qtn_amt2',
        'qtn_description3','qtn_qty3','qtn_rate3','qtn_amt3',
        'qtn_description4','qtn_qty4','qtn_rate4','qtn_amt4',
        'qtn_description5','qtn_qty5','qtn_rate5','qtn_amt5',
        'qtn_description6','qtn_qty6','qtn_rate6','qtn_amt6',
        'qtn_description7','qtn_qty7','qtn_rate7','qtn_amt7',
        'qtn_description8','qtn_qty8','qtn_rate8','qtn_amt8',
        'qtn_description9','qtn_qty9','qtn_rate9','qtn_amt9',
        'qtn_description10','qtn_qty10','qtn_rate10','qtn_amt10',
        )
        labels = {
            'qtn_total_amount':'Total Amount','qtn_no':'Quotation No','qtn_date':'Date',
        "cust_name": "Customer Name",'cust_village':'Village','cust_taluka':'Taluka','cust_dist':'Dist','cust_mobile':'Mobile',
        'qtn_description1':'Description','qtn_qty1':'Qty','qtn_rate1':'Rate','qtn_amt1':'Amount',
        'qtn_description2':'Description','qtn_qty2':'Qty','qtn_rate2':'Rate','qtn_amt2':'Amount',
        'qtn_description3':'Description','qtn_qty3':'Qty','qtn_rate3':'Rate','qtn_amt3':'Amount',
        'qtn_description4':'Description','qtn_qty4':'Qty','qtn_rate4':'Rate','qtn_amt4':'Amount',
        'qtn_description5':'Description','qtn_qty5':'Qty','qtn_rate5':'Rate','qtn_amt5':'Amount',
        'qtn_description6':'Description','qtn_qty6':'Qty','qtn_rate6':'Rate','qtn_amt6':'Amount',
        'qtn_description7':'Description','qtn_qty7':'Qty','qtn_rate7':'Rate','qtn_amt7':'Amount',
        'qtn_description8':'Description','qtn_qty8':'Qty','qtn_rate8':'Rate','qtn_amt8':'Amount',
        'qtn_description9':'Description','qtn_qty9':'Qty','qtn_rate9':'Rate','qtn_amt9':'Amount',
        'qtn_description10':'Description','qtn_qty10':'Qty','qtn_rate10':'Rate','qtn_amt10':'Amount',
        }
        
        widgets={
                'qtn_date':forms.NumberInput(attrs={'type':'date'}) ,
                'qtn_qty1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty7':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty8':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty9':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_qty10':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
               
                'qtn_rate1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate7':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate8':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate9':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'qtn_rate10':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),

                'qtn_amt1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt7':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt8':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt9':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'qtn_amt10':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
        }


class Form_Delivery_Challan(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form_Delivery_Challan, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['cust_name'].widget.attrs['readonly'] = True
            self.fields['del_total_amount'].widget.attrs['readonly'] = True

    class Meta:
        model = DB_Bills
        fields = ('cust_name','cust_mobile','cust_village','cust_taluka','cust_dist',
        'del_date','del_num','del_total_amount','del_amt_in_word',
        'del_descrtiption1','del_chessis1','del_engine1','del_qty1','del_amount1',
        'del_descrtiption2','del_chessis2','del_engine2','del_qty2','del_amount2',
        'del_descrtiption3','del_chessis3','del_engine3','del_qty3','del_amount3',
        'del_descrtiption4','del_chessis4','del_engine4','del_qty4','del_amount4',
        'del_descrtiption5','del_chessis5','del_engine5','del_qty5','del_amount5',
        )
        labels = {'del_date':'Date','del_num':'Delivery No','del_total_amount':'Total Amount',
        "cust_name": "Customer Name",'cust_village':'Village','cust_taluka':'Taluka','cust_dist':'Dist','cust_mobile':'Mobile',
        'del_descrtiption1':'Description','del_chessis1':'Chessis No','del_engine1':'Engine No','del_qty1':'Qty','del_amount1':'Amount',
        'del_descrtiption2':'Description','del_chessis2':'Chessis No','del_engine2':'Engine No','del_qty2':'Qty','del_amount2':'Amount',
        'del_descrtiption3':'Description','del_chessis3':'Chessis No','del_engine3':'Engine No','del_qty3':'Qty','del_amount3':'Amount',
        'del_descrtiption4':'Description','del_chessis4':'Chessis No','del_engine4':'Engine No','del_qty4':'Qty','del_amount4':'Amount',
        'del_descrtiption5':'Description','del_chessis5':'Chessis No','del_engine5':'Engine No','del_qty5':'Qty','del_amount5':'Amount',
        
        }

        widgets={
                'del_date':forms.NumberInput(attrs={'type':'date'}),
                'del_qty1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_qty2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_qty3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_qty4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_qty5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),

                'del_amount1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_amount2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_amount3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_amount4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),
                'del_amount5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);  ConvertNumberToWords();'}),

        }


class Form_Margin_Money(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form_Margin_Money, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['cust_name'].widget.attrs['readonly'] = True
            self.fields['mrm_total_amt'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word1'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word2'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word3'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word4'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word5'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word6'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word7'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word8'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word9'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word10'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word11'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word12'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word13'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word14'].widget.attrs['readonly'] = True
            self.fields['mrm_amt_in_word15'].widget.attrs['readonly'] = True

    class Meta:
        model = DB_Bills
        fields = ('cust_name','cust_mobile','cust_village','cust_taluka','cust_dist','mrm_no','mrm_total_amt',
        'mrm_date1','mrm_amount1','mrm_amt_in_word1','mrm_region1','mrm_payment_mode1','mrm_hyp1','mrm_remark1',
        'mrm_date2','mrm_amount2','mrm_amt_in_word2','mrm_region2','mrm_payment_mode2','mrm_hyp2','mrm_remark2',
        'mrm_date3','mrm_amount3','mrm_amt_in_word3','mrm_region3','mrm_payment_mode3','mrm_hyp3','mrm_remark3',
        'mrm_date4','mrm_amount4','mrm_amt_in_word4','mrm_region4','mrm_payment_mode4','mrm_hyp4','mrm_remark4',
        'mrm_date5','mrm_amount5','mrm_amt_in_word5','mrm_region5','mrm_payment_mode5','mrm_hyp5','mrm_remark5',
        'mrm_date6','mrm_amount6','mrm_amt_in_word6','mrm_region6','mrm_payment_mode6','mrm_hyp6','mrm_remark6',
        'mrm_date7','mrm_amount7','mrm_amt_in_word7','mrm_region7','mrm_payment_mode7','mrm_hyp7','mrm_remark7',
        'mrm_date8','mrm_amount8','mrm_amt_in_word8','mrm_region8','mrm_payment_mode8','mrm_hyp8','mrm_remark8',
        'mrm_date9','mrm_amount9','mrm_amt_in_word9','mrm_region9','mrm_payment_mode9','mrm_hyp9','mrm_remark9',
        'mrm_date10','mrm_amount10','mrm_amt_in_word10','mrm_region10','mrm_payment_mode10','mrm_hyp10','mrm_remark10',
        'mrm_date11','mrm_amount11','mrm_amt_in_word11','mrm_region11','mrm_payment_mode11','mrm_hyp11','mrm_remark11',
        'mrm_date12','mrm_amount12','mrm_amt_in_word12','mrm_region12','mrm_payment_mode12','mrm_hyp12','mrm_remark12',
        'mrm_date13','mrm_amount13','mrm_amt_in_word13','mrm_region13','mrm_payment_mode13','mrm_hyp13','mrm_remark13',
        'mrm_date14','mrm_amount14','mrm_amt_in_word14','mrm_region14','mrm_payment_mode14','mrm_hyp14','mrm_remark14',
        'mrm_date15','mrm_amount15','mrm_amt_in_word15','mrm_region15','mrm_payment_mode15','mrm_hyp15','mrm_remark15',
 
        )

        widgets={
                'mrm_date1':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date2':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date3':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date4':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date5':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date6':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date7':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date8':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date9':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date10':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date11':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date12':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date13':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date14':forms.NumberInput(attrs={'type':'date'}) ,
                'mrm_date15':forms.NumberInput(attrs={'type':'date'}) ,
                
                'mrm_total_amt':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value);'}),
                'mrm_amount1':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords1(this.value);'}),
                'mrm_amount2':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords2(this.value);'}),
                'mrm_amount3':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords3(this.value);'}),
                'mrm_amount4':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords4(this.value);'}),
                'mrm_amount5':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords5(this.value);'}),
                'mrm_amount6':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords6(this.value);'}),
                'mrm_amount7':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords7(this.value);'}),
                'mrm_amount8':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords8(this.value);'}),
                'mrm_amount9':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords9(this.value);'}),
                'mrm_amount10':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords10(this.value);'}),
                'mrm_amount11':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords11(this.value);'}),
                'mrm_amount12':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords12(this.value);'}),
                'mrm_amount13':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords13(this.value);'}),
                'mrm_amount14':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords14(this.value);'}),
                'mrm_amount15':forms.NumberInput(attrs={'class':'form-control','onkeyup':'auto_calculations(this.value); ConvertNumberToWords15(this.value);'}),
               
        }

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Form_Profile(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(label='Co-Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter first Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
        }
        labels={
            'username':'Username',
            'first_name':'Driver Name',
            'last_name':'License No',
            'email':'Email Adress',
            'password2':'Confirm Password'
        }


class login_form(AuthenticationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control radius','placeholder':'Enter Username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control radius','placeholder':'Enter Password'}))
