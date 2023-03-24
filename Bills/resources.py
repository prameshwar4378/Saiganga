
from dataclasses import fields
from lib2to3.pgen2.driver import Driver
from import_export import resources
from .models import DB_Bills

class Quotation_Resource(resources.ModelResource):
    class Meta:
        model = DB_Bills
        fields=['id','branch','cust_name','cust_village','cust_taluka','cust_dist','cust_mobile','qtn_total_amount','qtn_description1','qtn_description2','qtn_description3','qtn_description4','qtn_description5','qtn_description6','qtn_description7','qtn_description8','qtn_description9','qtn_description10']

        
class Invoice_Resource(resources.ModelResource):
    class Meta:
        model = DB_Bills
        fields=['id','branch','cust_name','cust_village','cust_taluka','cust_dist','cust_mobile','inv_no','inv_date',
            'inv_description_1','inv_chessis_1','inv_engine_1','inv_qty_1','inv_rate_1','inv_amount_1',
            'inv_description_2','inv_chessis_2','inv_engine_2','inv_qty_2','inv_rate_2','inv_amount_2',
            'inv_description_3','inv_chessis_3','inv_engine_3','inv_qty_3','inv_rate_3','inv_amount_3',
            'inv_description_4','inv_chessis_4','inv_engine_4','inv_qty_4','inv_rate_4','inv_amount_4',
            'inv_description_5','inv_chessis_5','inv_engine_5','inv_qty_5','inv_rate_5','inv_amount_5',
            'inv_description_6','inv_chessis_6','inv_engine_6','inv_qty_6','inv_rate_6','inv_amount_6',
            'inv_sub_total','inv_cgst','inv_sgst','inv_rto','inv_grand_total'
        ]

        
class Delivery_Challan_Resource(resources.ModelResource):
    class Meta:
        model = DB_Bills
        fields=['id','branch','cust_name','cust_village','cust_taluka','cust_dist','cust_mobile',
                'del_num','del_date','del_descrtiption1','del_chessis1','del_engine1','del_qty1','del_amount1',''
            ]

        
class Margin_Money_Resource(resources.ModelResource):
    class Meta:
        model = DB_Bills
        fields=['id','branch','cust_name','cust_village','cust_taluka','cust_dist','cust_mobile','mrm_no',
                'mrm_date1','mrm_amount1','mrm_amt_in_word1','mrm_region1','mrm_payment_mode1','mrm_hyp1','mrm_remark1',
                'mrm_date2','mrm_amount2','mrm_amt_in_word1','mrm_region2','mrm_payment_mode2','mrm_hyp2','mrm_remark2',
                'mrm_date3','mrm_amount3','mrm_amt_in_word1','mrm_region3','mrm_payment_mode3','mrm_hyp3','mrm_remark3',
                'mrm_date4','mrm_amount4','mrm_amt_in_word1','mrm_region4','mrm_payment_mode4','mrm_hyp4','mrm_remark4',
                'mrm_date5','mrm_amount5','mrm_amt_in_word1','mrm_region5','mrm_payment_mode5','mrm_hyp5','mrm_remark5',
                'mrm_date6','mrm_amount6','mrm_amt_in_word1','mrm_region6','mrm_payment_mode6','mrm_hyp6','mrm_remark6',
                'mrm_date7','mrm_amount7','mrm_amt_in_word1','mrm_region7','mrm_payment_mode7','mrm_hyp7','mrm_remark7',
                'mrm_date8','mrm_amount8','mrm_amt_in_word1','mrm_region8','mrm_payment_mode8','mrm_hyp8','mrm_remark8',
                'mrm_date9','mrm_amount9','mrm_amt_in_word1','mrm_region9','mrm_payment_mode9','mrm_hyp9','mrm_remark9',
                'mrm_date10','mrm_amount10','mrm_amt_in_word1','mrm_region10','mrm_payment_mode10','mrm_hyp10','mrm_remark10',
                'mrm_date11','mrm_amount11','mrm_amt_in_word11','mrm_region11','mrm_payment_mode11','mrm_hyp11','mrm_remark11',
                'mrm_date12','mrm_amount12','mrm_amt_in_word12','mrm_region12','mrm_payment_mode12','mrm_hyp12','mrm_remark12',
                'mrm_date13','mrm_amount13','mrm_amt_in_word13','mrm_region13','mrm_payment_mode13','mrm_hyp13','mrm_remark13',
                'mrm_date14','mrm_amount14','mrm_amt_in_word14','mrm_region14','mrm_payment_mode14','mrm_hyp14','mrm_remark14',
                'mrm_date15','mrm_amount15','mrm_amt_in_word15','mrm_region15','mrm_payment_mode15','mrm_hyp15','mrm_remark15',

        ]