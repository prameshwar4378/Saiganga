from operator import mod
from string import digits
from django.db import models
from django.forms import DateField

# Create your models here.



BRANCH=(
    ('Vaijapur','Vaijapur'),
    ('Gangapur','Gangapur')
)

DISTRICT=(
    ('Aurangabad','Aurangabad'),
    ('Nashik','Nashik'),
    ('Ahmednagar','Ahmednagar'),
    ('Beed','Beed'),
    ('Dhule','Dhule'),
    ('Jalgaon','Jalgaon'),
    ('Jalna','Jalna'),
    ('Latur','Latur'),
    ('Osmanabad','Osmanabad'),
)

PAYMENT_MODE=(
    ('CASH','CASH'),
    ('ONLINE','ONLINE'),
    ('PART_PAY CASH','PART_PAY CASH'),
    ('PART_PAY ONLINE','PART_PAY ONLINE'),
)

HYP=(
    ('Indusind Bank Ltd.','Indusind Bank Ltd.'),
    ('L&T Finance Ltd.','L&T Finance Ltd.'),
    ('HDB Finance Service Ltd.','HDB Finance Service Ltd.'),
)

PRODUCTS=(
        ('Adjustable Locking Bolt (Front Weight)','Adjustable Locking Bolt (Front Weight)'),
        ('Alternator 7.5 KVA','Alternator 7.5 KVA'),
        ('Bumper','Bumper'),
        ('Bumper 4WD ( C-Channel Type)','Bumper 4WD ( C-Channel Type)'),
        ('Bumper 4WD Heavy (40 kg)','Bumper 4WD Heavy (40 kg)'),
        ('Bumper 4WD Heavy (60 kg)','Bumper 4WD Heavy (60 kg)'),
        ('CAPTAIN 280-DI 4WD OIB','CAPTAIN 280-DI 4WD OIB'),
        ('CAPTAIN 283-DI 4WD OIB','CAPTAIN 283-DI 4WD OIB'),
        ('CAPTAIN  200 DI 4WD - PS','CAPTAIN  200 DI 4WD - PS'),
        ('CAPTAIN 200 DI 4WD-OIB','CAPTAIN 200 DI 4WD-OIB'),
        ('CAPTAIN 200 DI 4WD- NT','CAPTAIN 200 DI 4WD- NT'),
        ('CAPTAIN 200 DI 4WD- NT-PS','CAPTAIN 200 DI 4WD- NT-PS'),
        ('CAPTAIN 200 DI 4WD-HO-PS','CAPTAIN 200 DI 4WD-HO-PS'),
        ('CAPTAIN 200DI -HS','CAPTAIN 200DI -HS'),
        ('CAPTAIN 200DI -NT','CAPTAIN 200DI -NT'),
        ('CAPTAIN 250 4WD -PS-FT- 6.00 X 12 ,RT- 8.3x20','CAPTAIN 250 4WD -PS-FT- 6.00 X 12 ,RT- 8.3x20'),
        ('CAPTAIN 250 DI 4WD - FT- 6.00 X 12 ,RT- 8.3x20- OIB-HO','CAPTAIN 250 DI 4WD - FT- 6.00 X 12 ,RT- 8.3x20- OIB-HO'),
        ('CAPTAIN 250 DI 4WD -NT-OIB','CAPTAIN 250 DI 4WD -NT-OIB'),
        ('CAPTAIN 250 DI 4WD -NT-PS-OIB','CAPTAIN 250 DI 4WD -NT-PS-OIB'),
        ('CAPTAIN 250 DI 4WD -PS- FT- 6.00 X 12 ,RT- 8.3x20- OIB-HO','CAPTAIN 250 DI 4WD -PS- FT- 6.00 X 12 ,RT- 8.3x20- OIB-HO'),
        ('CAPTAIN 250 DI 4WD-OIB','CAPTAIN 250 DI 4WD-OIB'),
        ('CAPTAIN 250 DI 4WD-OIB-FT- 6.00 X 12 ,RT- 8.3x20-','CAPTAIN 250 DI 4WD-OIB-FT- 6.00 X 12 ,RT- 8.3x20-'),
        ('CAPTAIN 250 DI 4WD-PS-OIB','CAPTAIN 250 DI 4WD-PS-OIB'),
        ('CAPTAIN 250 DI FT- 5.25x14 ,RT 8.3X20-PS-OIB-LD','CAPTAIN 250 DI FT- 5.25x14 ,RT 8.3X20-PS-OIB-LD'),
        ('CAPTAIN 250 DI FT-5.00X15 ,9.5X24-OIB','CAPTAIN 250 DI FT-5.00X15 ,9.5X24-OIB'),
        ('CAPTAIN 250 DI FT-5.00X15 ,9.5X24-PS-OIB','CAPTAIN 250 DI FT-5.00X15 ,9.5X24-PS-OIB'),
        ('CAPTAIN 250 DI FT-5.25x14 ,RT 8.3X20  -OIB','CAPTAIN 250 DI FT-5.25x14 ,RT 8.3X20  -OIB'),
        ('CAPTAIN 250 DI FT-5.25x14 ,RT 8.3X20  PS-OIB','CAPTAIN 250 DI FT-5.25x14 ,RT 8.3X20  PS-OIB'),
        ('CAPTAIN 250 DI-HS-PS-O','CAPTAIN 250 DI-HS-PS-O'),
        ('CAPTAIN 250 DI-OIB','CAPTAIN 250 DI-OIB'),
        ('CAPTAIN 280-DI 4WD-NT-PS-OB-BI','CAPTAIN 280-DI 4WD-NT-PS-OB-BI'),
        ('CAPTAIN 280-DI 4WD-OIB-FT- 6.00 X 12 ,RT- 8.3x20-','CAPTAIN 280-DI 4WD-OIB-FT- 6.00 X 12 ,RT- 8.3x20-'),
        ('CAPTAIN 280-DI 4WD-OIB-FT- 6.00 X 12 ,RT- 8.3x20-HO','CAPTAIN 280-DI 4WD-OIB-FT- 6.00 X 12 ,RT- 8.3x20-HO'),
        ('CAPTAIN 280-DI 4WD-PS-OIB-FT- 6.00 X 12 ,RT- 8.3x20-','CAPTAIN 280-DI 4WD-PS-OIB-FT- 6.00 X 12 ,RT- 8.3x20-'),
        ('CAPTAIN 280-DI 4WD-PS-OIB','CAPTAIN 280-DI 4WD-PS-OIB'),
        ('CAPTAIN 280 DX- FT.5.00X15 RT-9.5X24-OIB','CAPTAIN 280 DX- FT.5.00X15 RT-9.5X24-OIB'),
        ('CAPTAIN 280 DX- FT.5.00X15 RT-9.5X24-PS-OIB','CAPTAIN 280 DX- FT.5.00X15 RT-9.5X24-PS-OIB'),
        ('CAPTAIN 280DI -PS-OB-LD','CAPTAIN 280DI -PS-OB-LD'),
        ('Centrifugal Pump (3”x 2.5”)','Centrifugal Pump (3”x 2.5”)'),
        ('CENTRIFUGAL PUMP (4”X4”)','CENTRIFUGAL PUMP (4”X4”)'),
        ('CHAFF CUTTER - 24"','CHAFF CUTTER - 24"'),
        ('Cultivator - 3 Chisel','Cultivator - 3 Chisel'),
        ('CULTIVATOR - 7 SPRING TYN','CULTIVATOR - 7 SPRING TYN'),
        ('Cultivator -5 Duck foot','Cultivator -5 Duck foot'),
        ('Cultivator -5 Duck foot (Set)','Cultivator -5 Duck foot (Set)'),
        ('Cultivator -5 Tine','Cultivator -5 Tine'),
        ('Cultivator -5 Tine (Set)','Cultivator -5 Tine (Set)'),
        ('CULTIVATOR 5-SPRING TYNE','CULTIVATOR 5-SPRING TYNE'),
        ('Cultivator -7 Duck foot','Cultivator -7 Duck foot'),
        ('Cultivator 7 Tine','Cultivator 7 Tine'),
        ('Cultivator Blade type (2-Row','Cultivator Blade type (2-Row'),
        ('Cultivator Bracket Bullock Drawn','Cultivator Bracket Bullock Drawn'),
        ('Cultivator Height Attachmen','Cultivator Height Attachmen'),
        ('Disc Harrow (14 Disc) 18"','Disc Harrow (14 Disc) 18"'),
        ('Disc Harrow (16 Disc) 18"','Disc Harrow (16 Disc) 18"'),
        ('DISC PLOUGH - 22" (2-Ballota DISC)','DISC PLOUGH - 22" (2-Ballota DISC)'),
        ('DISC PLOUGH REVERSIBLE - 22" (2- Ballota DISC','DISC PLOUGH REVERSIBLE - 22" (2- Ballota DISC'),
        ('Frame, Front Weight','Frame, Front Weight'),
        ('Frame,Canopy Mounting','Frame,Canopy Mounting'),
        ('Front Weight , (20KG)','Front Weight , (20KG)'),
        ('Furrow Attachment','Furrow Attachment'),
        ('Half Cage wheel - LH & RH','Half Cage wheel - LH & RH'),
        ('Height Attachement -60"(4WD)','Height Attachement -60"(4WD)'),
        ('Height Attachment - 48" (2WD)','Height Attachment - 48" (2WD)'),
        ('HEIGHT ATTACHMENT – 48” (2WD) (2 FT. G.C.)','HEIGHT ATTACHMENT – 48” (2WD) (2 FT. G.C.)'),
        ('HEIGHT ATTACHMENT – 48” (4WD) (2 FT. G.C.)','HEIGHT ATTACHMENT – 48” (4WD) (2 FT. G.C.)'),
        ('Height Attachment - 48”(4WD)','Height Attachment - 48”(4WD)'),
        ('Height attachment - 60" (2WD)','Height attachment - 60" (2WD)'),
        ('Hood (Rajwadi)','Hood (Rajwadi)'),
        ('Land Leveler','Land Leveler'),
        ('MOULD BOARD PLOUGH - 2 FARROW (HEAVY)','MOULD BOARD PLOUGH - 2 FARROW (HEAVY)'),
        ('Mould Board Plough 2 Farrow','Mould Board Plough 2 Farrow'),
        ('Mould Board Plough 3 Farrow','Mould Board Plough 3 Farrow'),
        ('Mould Board Plough Reversible','Mould Board Plough Reversible'),
        ('Mould Board Plough Reversible (Heavy)','Mould Board Plough Reversible (Heavy)'),
        ('Post Hole Digger 9 inch','Post Hole Digger 9 inch'),
        ('POTATO DIGGER','POTATO DIGGER'),
        ('POTATO PLANTER','POTATO PLANTER'),
        ('Puddler','Puddler'),
        ('Ridger (1 Row)','Ridger (1 Row)'),
        ('Ridger (2 Row)','Ridger (2 Row)'),
        ('Rod, Locking (Front Weight)','Rod, Locking (Front Weight)'),
        ('ROPS','ROPS'),
        ('Rotary Tiller (RF) 0.7M','Rotary Tiller (RF) 0.7M'),
        ('Rotary Tiller 0.8m (L Type )','Rotary Tiller 0.8m (L Type )'),
        ('Rotary Tiller 1.2m (L Type )','Rotary Tiller 1.2m (L Type )'),
        ('Rotary Tiller 1m. (L Type )','Rotary Tiller 1m. (L Type )'),
        ('Roto Seed Drill (Attachment)','Roto Seed Drill (Attachment)'),
        ('Seed cum Fertilizer Drill 5×10','Seed cum Fertilizer Drill 5×10'),
        ('Seed cum Fertilizer Drill 5×10 (Without cultivato','Seed cum Fertilizer Drill 5×10 (Without cultivato'),
        ('Seed cum Fertilizer Drill 7×14','Seed cum Fertilizer Drill 7×14'),
        ('Seed cum Fertilizer Drill 7×14 (Without cultivato','Seed cum Fertilizer Drill 7×14 (Without cultivato'),
        ('Sprayer Pump (Horticulture)','Sprayer Pump (Horticulture)'),
        ('SPRAYER PUMP 8 NOZZLE (VERTICAL- 500 Ltr.)','SPRAYER PUMP 8 NOZZLE (VERTICAL- 500 Ltr.)'),
        ('Sprayer Pump 8 nozzle (Vertical)','Sprayer Pump 8 nozzle (Vertical)'),
        ('Sprayer Pump 8 Nozzle (Vertical-300 Ltr.)','Sprayer Pump 8 Nozzle (Vertical-300 Ltr.)'),
        ('Sprayer Pump 9 nozzle (Boom)','Sprayer Pump 9 nozzle (Boom)'),
        ('Sprayer Pump 9 Nozzle (Boom-300 Ltr.)','Sprayer Pump 9 Nozzle (Boom-300 Ltr.)'),
        ('Sub Soiler','Sub Soiler'),
        ('Sugarcane Cage','Sugarcane Cage'),
        ('Tanker (2000 Ltr.)','Tanker (2000 Ltr.)'),
        ('Thresher-2.5 feet','Thresher-2.5 feet'),
        ('Tractor Dozer','Tractor Dozer'),
        ('Tractor Front Mounted Reaper 1.2m','Tractor Front Mounted Reaper 1.2m'),
        ('Tractor Front Mounted Reaper 1.5m','Tractor Front Mounted Reaper 1.5m'),
        ('Tractor Mounted Front end loader','Tractor Mounted Front end loader'),
        ('TRACTOR MOUNTED FRONT END LOADER WITH','TRACTOR MOUNTED FRONT END LOADER WITH'),
        ('Tractor Road Sweeper','Tractor Road Sweeper'),
        ('TRAILER – 60 Feet (7.50 X 16)','TRAILER – 60 Feet (7.50 X 16)'),
        ('Trailer (40 Feet - 6.00x16 tyre)','Trailer (40 Feet - 6.00x16 tyre)'),
        ('Trailer (60 Feet- 6.00x16 tyre)','Trailer (60 Feet- 6.00x16 tyre)'),
        ('Wheel weight - Rear Wheel ( 25 KG)','Wheel weight - Rear Wheel ( 25 KG)'),
        ('Wheel Weight -Front Wheel ( 20 KG )','Wheel Weight -Front Wheel ( 20 KG )'),
        ('Zero Till Seed cum Fertilizer Drill (2 Row)','Zero Till Seed cum Fertilizer Drill (2 Row)'),
        ('Zero Till Seed cum Fertilizer Drill (3 Row)','Zero Till Seed cum Fertilizer Drill (3 Row)'),
        ('Zero Till Seed cum Fertilizer Drill (5 Row)','Zero Till Seed cum Fertilizer Drill (5 Row)'),
        )

class DB_Bills(models.Model):
    branch=models.CharField(max_length=50,null=True,choices=BRANCH)
    cust_name=models.CharField(max_length=50)
    cust_village=models.CharField(max_length=50)
    cust_taluka=models.CharField(max_length=50)
    cust_dist=models.CharField(max_length=50,choices=DISTRICT)
    cust_pin_code=models.IntegerField(null=True)
    cust_mobile=models.BigIntegerField()

    other_reference=models.CharField(max_length=50,null=True,choices=HYP)
# Start Model For Tax Invoice Bill
    inv_no=models.IntegerField(null=True)
    inv_date=models.DateField(max_length=50,null=True)
    inv_amt_in_word=models.CharField(max_length=500,null=True)

    inv_description_1=models.CharField(max_length=100,null=True,choices=PRODUCTS)
    inv_chessis_1=models.CharField(max_length=50,null=True)
    inv_engine_1=models.CharField(max_length=50,null=True)
    inv_qty_1=models.IntegerField(default='1')
    inv_rate_1=models.FloatField(default='0')
    inv_amount_1=models.FloatField(default='0')
    
    inv_description_2=models.CharField(max_length=100,blank=True, null=True,choices=PRODUCTS)
    inv_chessis_2=models.CharField(max_length=50,blank=True, null=True)
    inv_engine_2=models.CharField(max_length=50,blank=True, null=True)
    inv_qty_2=models.IntegerField(blank=True, null=True)
    inv_rate_2=models.FloatField(blank=True, null=True)
    inv_amount_2=models.FloatField(blank=True, null=True)
    
    inv_description_3=models.CharField(max_length=100,blank=True, null=True,choices=PRODUCTS)
    inv_chessis_3=models.CharField(max_length=50,blank=True, null=True)
    inv_engine_3=models.CharField(max_length=50,blank=True, null=True)
    inv_qty_3=models.IntegerField(blank=True, null=True)
    inv_rate_3=models.FloatField(blank=True, null=True)
    inv_amount_3=models.FloatField(blank=True, null=True)
    
    inv_description_4=models.CharField(max_length=100,blank=True, null=True,choices=PRODUCTS)
    inv_chessis_4=models.CharField(max_length=50,blank=True, null=True)
    inv_engine_4=models.CharField(max_length=50,blank=True, null=True)
    inv_qty_4=models.IntegerField(blank=True, null=True)
    inv_rate_4=models.FloatField(blank=True, null=True)
    inv_amount_4=models.FloatField(blank=True, null=True)
    
    inv_description_5=models.CharField(max_length=100,blank=True, null=True,choices=PRODUCTS)
    inv_chessis_5=models.CharField(max_length=50,blank=True, null=True)
    inv_engine_5=models.CharField(max_length=50,blank=True, null=True)
    inv_qty_5=models.IntegerField(blank=True, null=True)
    inv_rate_5=models.FloatField(blank=True, null=True)
    inv_amount_5=models.FloatField(blank=True, null=True)
    
    inv_description_6=models.CharField(max_length=100,blank=True, null=True,choices=PRODUCTS)
    inv_chessis_6=models.CharField(max_length=50,blank=True, null=True)
    inv_engine_6=models.CharField(max_length=50,blank=True, null=True)
    inv_qty_6=models.IntegerField(blank=True, null=True)
    inv_rate_6=models.FloatField(blank=True, null=True)
    inv_amount_6=models.FloatField(blank=True, null=True)

    inv_sub_total =models.FloatField(null=True)
    inv_grand_total =models.FloatField(null=True)
    inv_sgst =models.FloatField(default='0')
    inv_cgst =models.FloatField(default='0')
    inv_rto=models.FloatField(default='0')

# End Model For Tax Invoice Bill

# Start Model For Quotation
    qtn_no=models.IntegerField(null=True)
    qtn_date=models.DateField(max_length=20,null=True)
    qtn_total_amount=models.FloatField(null=True)
    qtn_amt_in_word=models.CharField(max_length=200,null=True)

    qtn_description1=models.CharField(max_length=400,null=True,choices=PRODUCTS)
    qtn_description2=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description3=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description4=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description5=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description6=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description7=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description8=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description9=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)
    qtn_description10=models.CharField(max_length=400,null=True,blank=True,choices=PRODUCTS)

    qtn_qty1=models.IntegerField(null=True)
    qtn_qty2=models.IntegerField(null=True,blank=True)
    qtn_qty3=models.IntegerField(null=True,blank=True)
    qtn_qty4=models.IntegerField(null=True,blank=True)
    qtn_qty5=models.IntegerField(null=True,blank=True)
    qtn_qty6=models.IntegerField(null=True,blank=True)
    qtn_qty7=models.IntegerField(null=True,blank=True)
    qtn_qty8=models.IntegerField(null=True,blank=True)
    qtn_qty9=models.IntegerField(null=True,blank=True)
    qtn_qty10=models.IntegerField(null=True,blank=True)

    qtn_rate1=models.FloatField(null=True)
    qtn_rate2=models.FloatField(null=True,blank=True)
    qtn_rate3=models.FloatField(null=True,blank=True)
    qtn_rate4=models.FloatField(null=True,blank=True)
    qtn_rate5=models.FloatField(null=True,blank=True)
    qtn_rate6=models.FloatField(null=True,blank=True)
    qtn_rate7=models.FloatField(null=True,blank=True)
    qtn_rate8=models.FloatField(null=True,blank=True)
    qtn_rate9=models.FloatField(null=True,blank=True)
    qtn_rate10=models.FloatField(null=True,blank=True)

    qtn_amt1=models.FloatField(null=True,default=0)
    qtn_amt2=models.FloatField(null=True,blank=True)
    qtn_amt3=models.FloatField(null=True,blank=True)
    qtn_amt4=models.FloatField(null=True,blank=True)
    qtn_amt5=models.FloatField(null=True,blank=True)
    qtn_amt6=models.FloatField(null=True,blank=True)
    qtn_amt7=models.FloatField(null=True,blank=True)
    qtn_amt8=models.FloatField(null=True,blank=True)
    qtn_amt9=models.FloatField(null=True,blank=True)
    qtn_amt10=models.FloatField(null=True,blank=True)

# End Model For Quotation



# Start Model For Delivery Challan

    del_date=models.DateField(max_length=50, null=True)
    del_num=models.IntegerField(null=True)
    del_total_amount=models.FloatField(null=True)
    del_amt_in_word=models.CharField(max_length=200,null=True)

    del_descrtiption1=models.CharField(max_length=400, null=True,choices=PRODUCTS)
    del_descrtiption2=models.CharField(max_length=400, null=True,blank=True,choices=PRODUCTS)
    del_descrtiption3=models.CharField(max_length=400, null=True,blank=True,choices=PRODUCTS)
    del_descrtiption4=models.CharField(max_length=400, null=True,blank=True,choices=PRODUCTS)
    del_descrtiption5=models.CharField(max_length=400, null=True,blank=True,choices=PRODUCTS)

    del_chessis1=models.CharField(max_length=15, null=True)
    del_chessis2=models.CharField(max_length=15, null=True,blank=True)
    del_chessis3=models.CharField(max_length=15, null=True,blank=True)
    del_chessis4=models.CharField(max_length=15, null=True,blank=True)
    del_chessis5=models.CharField(max_length=15, null=True,blank=True)

    del_engine1=models.CharField(max_length=15, null=True)
    del_engine2=models.CharField(max_length=15, null=True,blank=True)
    del_engine3=models.CharField(max_length=15, null=True,blank=True)
    del_engine4=models.CharField(max_length=15, null=True,blank=True)
    del_engine5=models.CharField(max_length=15, null=True,blank=True)

    del_qty1=models.IntegerField(null=True)
    del_qty2=models.IntegerField(null=True,blank=True)
    del_qty3=models.IntegerField(null=True,blank=True)
    del_qty4=models.IntegerField(null=True,blank=True)
    del_qty5=models.IntegerField(null=True,blank=True)

    del_amount1=models.FloatField(null=True)
    del_amount2=models.FloatField(null=True,blank=True)
    del_amount3=models.FloatField(null=True,blank=True)
    del_amount4=models.FloatField(null=True,blank=True)
    del_amount5=models.FloatField(null=True,blank=True)


# End Model For Delivery Challan

    mrm_no =models.IntegerField(null=True)
    mrm_total_amt =models.IntegerField(null=True,blank=True)
    
    mrm_date1=models.DateField(max_length=20,null=True)
    mrm_amount1=models.CharField(max_length=20,null=True)
    mrm_amt_in_word1=models.CharField(max_length=150,null=True)
    mrm_region1=models.CharField(max_length=400,null=True,choices=PRODUCTS)
    mrm_payment_mode1=models.CharField(max_length=50,null=True,choices=PAYMENT_MODE)
    mrm_hyp1=models.CharField(max_length=50,null=True,choices=HYP)
    mrm_remark1=models.CharField(max_length=50,null=True,blank=True)

    mrm_date2=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount2=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word2=models.CharField(max_length=150,null=True,blank=True)
    mrm_region2=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode2=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp2=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark2=models.CharField(max_length=50,null=True,blank=True)

    mrm_date3=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount3=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word3=models.CharField(max_length=150,null=True,blank=True)
    mrm_region3=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode3=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp3=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark3=models.CharField(max_length=50,null=True,blank=True)

    mrm_date4=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount4=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word4=models.CharField(max_length=150,null=True,blank=True)
    mrm_region4=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode4=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp4=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark4=models.CharField(max_length=50,null=True,blank=True)

    mrm_date5=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount5=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word5=models.CharField(max_length=150,null=True,blank=True)
    mrm_region5=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode5=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp5=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark5=models.CharField(max_length=50,null=True,blank=True)

    mrm_date6=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount6=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word6=models.CharField(max_length=150,null=True,blank=True)
    mrm_region6=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode6=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp6=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark6=models.CharField(max_length=50,null=True,blank=True)

    mrm_date7=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount7=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word7=models.CharField(max_length=150,null=True,blank=True)
    mrm_region7=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode7=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp7=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark7=models.CharField(max_length=50,null=True,blank=True)

    mrm_date8=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount8=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word8=models.CharField(max_length=150,null=True,blank=True)
    mrm_region8=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode8=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp8=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark8=models.CharField(max_length=50,null=True,blank=True)

    mrm_date9=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount9=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word9=models.CharField(max_length=150,null=True,blank=True)
    mrm_region9=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode9=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp9=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark9=models.CharField(max_length=50,null=True,blank=True)

    mrm_date10=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount10=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word10=models.CharField(max_length=150,null=True,blank=True)
    mrm_region10=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode10=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp10=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark10=models.CharField(max_length=50,null=True,blank=True)

    mrm_date11=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount11=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word11=models.CharField(max_length=150,null=True,blank=True)
    mrm_region11=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode11=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp11=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark11=models.CharField(max_length=50,null=True,blank=True)

    mrm_date12=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount12=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word12=models.CharField(max_length=150,null=True,blank=True)
    mrm_region12=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode12=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp12=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark12=models.CharField(max_length=50,null=True,blank=True)

    mrm_date13=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount13=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word13=models.CharField(max_length=150,null=True,blank=True)
    mrm_region13=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode13=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp13=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark13=models.CharField(max_length=50,null=True,blank=True)

    mrm_date14=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount14=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word14=models.CharField(max_length=150,null=True,blank=True)
    mrm_region14=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode14=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp14=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark14=models.CharField(max_length=50,null=True,blank=True)

    mrm_date15=models.DateField(max_length=20,null=True,blank=True)
    mrm_amount15=models.CharField(max_length=20,null=True,blank=True)
    mrm_amt_in_word15=models.CharField(max_length=150,null=True,blank=True)
    mrm_region15=models.CharField(max_length=500,null=True,blank=True,choices=PRODUCTS)
    mrm_payment_mode15=models.CharField(max_length=50,null=True,blank=True,choices=PAYMENT_MODE)
    mrm_hyp15=models.CharField(max_length=50,null=True,blank=True,choices=HYP)
    mrm_remark15=models.CharField(max_length=50,null=True,blank=True)



    def __str__(self):
            return self.cust_name

    



# Create your models here.
class DB_orders(models.Model):
    cust_name=models.CharField( max_length=100)
    cust_mobile=models.IntegerField()
    cust_adress=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now=True, auto_now_add=False,editable=True)


class DB_Enquiry(models.Model):
    full_name=models.CharField(max_length=200)
    mobile=models.BigIntegerField()
    adress=models.TextField()
    message=models.TextField()
    date=models.DateTimeField(auto_now=True, auto_now_add=False,editable=True)