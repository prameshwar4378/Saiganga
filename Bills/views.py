from urllib import response
from django.shortcuts import render
from django.db.models import Max,Sum
from urllib import response

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from Bills.models import DB_Bills,DB_Enquiry, DB_orders
from .forms import Form_Manage_Customer,Form_Invoice,Form_Quotation,Form_Delivery_Challan,Form_Margin_Money,Form_calculator,Form_Profile,login_form
from django.contrib import messages
from .filters import Data_Filter
from .resources import Quotation_Resource,Invoice_Resource,Delivery_Challan_Resource,Margin_Money_Resource
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/bills/login/')
def Home(request):
    return render(request,"bills/Home.html")
    

@login_required(login_url='/bills/login/')
def update_profile(request,id):
    fm=Form_Profile(request.POST)
    if request.method=="POST":
        fm=Form_Profile(request.POST)
        pi=User.objects.get(pk=id)
        fm=Form_Profile(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('/login')
            
        else:
            pi=User.objects.get(pk=id)
            fm=Form_Profile(request.POST, instance=pi)
    else:
        pi=User.objects.get(pk=id)
        fm=Form_Profile(instance=pi)
    return render(request,'bills/update_profile.html',{'fm':fm,'id':id})


@login_required(login_url='/bills/login/')
def all_bills(request):
    list=DB_Bills.objects.all()
    rec=DB_Bills.objects.order_by('-id')
    Filter=Data_Filter(request.GET, queryset=rec)
    rec2=Filter.qs
    count=rec2.count()
    data={'rec':rec2,'count':count,'filter':Filter,'show_cust_list':list}
    return render(request,"bills/All_Bills.html",data)
    
@login_required(login_url='/bills/login/')
def customer_dashboard(request,id):
    dt=get_object_or_404(DB_Bills,id=id)
    fm=Form_Manage_Customer()
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Manage_Customer(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Updated Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Manage_Customer(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Manage_Customer(instance=pi)
    return render(request,"bills/customer_dashboard.html",{'id':id,'data':dt,'fm':fm})


@login_required(login_url='/bills/login/')
def add_customer(request):
    fm=Form_Manage_Customer()
    if request.method=="POST":
        fm=Form_Manage_Customer(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Customer Addedd Successfully...!')
            fm=Form_Manage_Customer()
    rec=DB_Bills.objects.order_by('-id')
    return render(request,"bills/add_customer.html",{'fm':fm,'rec':rec})

@login_required(login_url='/bills/login/')
def delete_customer(request,id):
    pi=DB_Bills.objects.get(pk=id)
    pi.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('/bills/all_bills/')

def update_customer(request,id):
    
    return render(request,"bills/customer_dashboard.html",{'id':id,})


@login_required(login_url='/bills/login/')
def invoice_form(request,id):
    inv_no= DB_Bills.objects.aggregate(max=Max('inv_no'))["max"] + int(1) 
    initialize_inv_No={
        'inv_no':inv_no
    }
    calulator=Form_calculator()
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Invoice(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Invoice Generated Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Invoice(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Invoice(instance=pi,initial=initialize_inv_No)
    return render(request,"bills/invoice_form.html",{'fm':fm,'id':id,'calculator':calulator})


@login_required(login_url='/bills/login/')
def quotation_form(request,id):
    qtn_no= DB_Bills.objects.aggregate(max=Max('qtn_no'))["max"] + int(1) 
    initialize_Quotation_No={
        'qtn_no':qtn_no
    }
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Quotation(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Quotation Generated Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Quotation(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Quotation(instance=pi,initial=initialize_Quotation_No)
    return render(request,"bills/quotation_form.html",{'fm':fm,'id':id})

    
@login_required(login_url='/bills/login/')
def delivery_challan_form(request,id):
    del_num= DB_Bills.objects.aggregate(max=Max('del_num'))["max"] + int(1) 
    initialize_del_No={
        'del_num':del_num
    }
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Delivery_Challan(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Update Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Delivery_Challan(request.POST)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Delivery_Challan(instance=pi,initial=initialize_del_No)
    return render(request,"bills/delivery_challan_form.html",{'fm':fm,'id':id})

    
@login_required(login_url='/bills/login/')
def margin_money_form(request,id):
    mrm_no= DB_Bills.objects.aggregate(max=Max('mrm_no'))["max"] + int(1) 
    initialize_mrm_No={
        'mrm_no':mrm_no
    }
    dt=get_object_or_404(DB_Bills,id=id)
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Margin_Money(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Update Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Margin_Money(request.POST)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Margin_Money(instance=pi,initial=initialize_mrm_No)
    return render(request,"bills/margin_money_form.html",{'fm':fm,'data':dt,'id':id})





# <!--Update Records-->


def update_invoice_form(request,id):

    calulator=Form_calculator()
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Invoice(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Invoice Generated Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Invoice(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Invoice(instance=pi)
    return render(request,"bills/invoice_form.html",{'fm':fm,'id':id,'calculator':calulator})


def update_quotation_form(request,id):

    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Quotation(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Quotation Generated Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Quotation(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Quotation(instance=pi)
    return render(request,"bills/quotation_form.html",{'fm':fm,'id':id})

    
def update_delivery_challan_form(request,id):

    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Delivery_Challan(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Update Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Delivery_Challan(request.POST)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Delivery_Challan(instance=pi)
    return render(request,"bills/delivery_challan_form.html",{'fm':fm,'id':id})

    
def update_margin_money_form(request,id):

    dt=get_object_or_404(DB_Bills,id=id)
    if request.method=="POST":
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Margin_Money(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Update Successfully..!")
        else:
            pi=DB_Bills.objects.get(pk=id)
            fm=Form_Margin_Money(request.POST)
    else:
        pi=DB_Bills.objects.get(pk=id)
        fm=Form_Margin_Money(instance=pi)
    return render(request,"bills/margin_money_form.html",{'fm':fm,'data':dt,'id':id})




def export_excel_quotation(request):
    record_resource = Quotation_Resource()
    dataset = record_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Quotation.xls"'
    return response


def export_excel_invoice(request):
    record_resource = Invoice_Resource()
    dataset = record_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Invoice.xls"'
    return response


def export_excel_delivery_challan(request):
    record_resource = Delivery_Challan_Resource()
    dataset = record_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Delivery Challan.xls"'
    return response


def export_excel_margin_money(request):
    record_resource = Margin_Money_Resource()
    dataset = record_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Margin Money.xls"'
    return response








def print_invoice(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/invoice_print.html",{'data':dt})

def print_quotation(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/quotation_print.html",{'data':dt,'id':id})
    
def print_delivery_challan(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/delivery_challan_print.html",{'data':dt,'id':id})


def print_margin_money1(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print1.html",{'data':dt,'id':id})
def print_margin_money2(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print2.html",{'data':dt,'id':id})
def print_margin_money3(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print3.html",{'data':dt,'id':id})
def print_margin_money4(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print4.html",{'data':dt,'id':id})
def print_margin_money5(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print5.html",{'data':dt,'id':id})
def print_margin_money6(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print6.html",{'data':dt,'id':id})
def print_margin_money7(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print7.html",{'data':dt,'id':id})
def print_margin_money8(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print8.html",{'data':dt,'id':id})
def print_margin_money9(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print9.html",{'data':dt,'id':id})
def print_margin_money10(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print10.html",{'data':dt,'id':id})
def print_margin_money11(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print11.html",{'data':dt,'id':id})
def print_margin_money12(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print12.html",{'data':dt,'id':id})
def print_margin_money13(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print13.html",{'data':dt,'id':id})
def print_margin_money14(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print14.html",{'data':dt,'id':id})
def print_margin_money15(request,id):
    dt=DB_Bills.objects.get(pk=id)
    return render(request,"bills/margin_money_templates/margin_money_print15.html",{'data':dt,'id':id})
    



def user_login(request):

    form=login_form()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/bills',{'user',user})
        else:
            form=login_form()
            messages.error(request,'Opps...! User does not exist... Please try again..!')

    return render(request,"bills/user_login.html",{'form':form})


def user_logout(request):
    logout(request)
    return redirect('/')

def order_list(request):
    rec=DB_orders.objects.order_by('-id')
    return render(request,"bills/order_list.html",{'rec':rec})
    
def enquiry_list(request):
    rec=DB_Enquiry.objects.order_by('-id')
    return render(request,"bills/enquiry_list.html",{'rec':rec})
    