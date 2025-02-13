from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product,Stock,Reg,Login,cart,order_child,order_master
import datetime
# Create your views here.


def listview(request):
    d=Product.objects.all()
    template=loader.get_template("listview.html")
    context={'data':d}
    return HttpResponse(template.render(context,request))
def list(request,id):
    request.session["pid"]=id
    d=Product.objects.get(id=id)
    template=loader.get_template("list.html")
    context={'data':d}
    return HttpResponse(template.render(context,request))
def addcart(request):
    if request.method=="POST":
        c=cart()
        data=Product.objects.get(id=request.session["pid"])
        c.date=datetime.datetime.today()
        c.qty=request.POST.get("qty")
        c.total=request.POST.get("total")
        c.pid_id=data.id
        c.uid_id=request.session["uid"]
        c.save()
        return HttpResponse("<script>alert('item added to cart');window.location='/listview';</script>")

def viewcart(request):
    if request.method=="POST":
        c=cart.objects.all()
        om=order_master()
        om.date=datetime.datetime.today()
        om.uid_id=request.session["uid"]
        om.gtotal=request.POST.get("gtotal")
        om.save()
        oid=order_master.objects.latest("id").id
        for i in c:
            oc=order_child()
            oc.oid_id=oid
            oc.pid_id=i.pid_id
            oc.qty=i.qty
            oc.total=i.total
            oc.status='completed'
            oc.save()
        c.delete()
        return HttpResponse("<script>alert('order placed successfully');window.location='/listview';</script>")

    else:
        d=cart.objects.raw("select myapp_cart.*,myapp_product.pname,myapp_product.rate from myapp_cart,myapp_product where myapp_cart.pid_id=myapp_product.id and myapp_cart.uid_id=%s",[request.session["uid"]])
        gtotal=0
        for i in d:
            gtotal+=i.total
        template=loader.get_template("cart.html")
        context={'data':d,'gt':gtotal}
        return HttpResponse(template.render(context,request))




def reg(request):
    if request.method=="POST":
        r=Reg()
        r.name=request.POST.get("name")
        r.gender=request.POST.get("gender")
        r.email=request.POST.get("email")
        r.addr=request.POST.get("address")
        r.phno=request.POST.get("phno")
        r.loc=request.POST.get("loc")
        
        r.save()
        id=Reg.objects.latest("id").id
        l=Login()
        l.uname=request.POST.get("uname")
        l.pwd=request.POST.get("pwd")
        l.utype='user'
        l.uid_id=id
        l.save()
        return HttpResponse("<script>alert('inserted');window.location='/reg';</script>")
    else:
        
        template=loader.get_template("Form.html")
        context={}
        return HttpResponse(template.render(context,request))
    
def login(request):
    if request.method=='POST':
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd") 
        if Login.objects.filter(uname=uname,pwd=pwd):
            l=Login.objects.get(uname=uname,pwd=pwd)  
            if l.utype=="user":
                request.session["uid"]=l.uid_id
                return HttpResponse("<script>alert('welcome user');window.location='/userhome';</script>")
            elif l.utype=="admin":
                return HttpResponse("<script>alert('welcome admin');window.location='/adminhome';</script>")
            else:
                return HttpResponse("<script>alert('invalid user');window.location='/login';</script>")


        else:
            return HttpResponse("<script>alert('invalid user');window.location='/login';</script>")

    else:

        template=loader.get_template("login.html")
        context={}
        return HttpResponse(template.render(context,request))
    
def userhome(request):
    template=loader.get_template("userhome.html")
    context={}
    return HttpResponse(template.render(context,request))

def adminhome(request):
    template=loader.get_template("adminhome.html")
    context={}
    return HttpResponse(template.render(context,request))
def home(request):
    template=loader.get_template("Home.html")
    context={}
    return HttpResponse(template.render(context,request))
def delete(request,id):
    c=cart.objects.get(id=id)
    c.delete()
    return HttpResponse("<script>alert('deleted');window.location='/viewcart';</script>")
def vieworder(request):
    d=order_master.objects.raw("select * from myapp_order_master,myapp_order_child,myapp_product where myapp_product.id=myapp_order_child.pid_id and myapp_order_child.oid_id=myapp_order_master.id and myapp_order_master.uid_id=%s",[request.session["uid"]])
   
    template=loader.get_template("vieworder.html")
    context={'d':d}
    return HttpResponse(template.render(context,request))
def cancel_order(request,id):
    c=order_child.objects.get(id=id)
    c.status='cancel'
    c.save()
    return HttpResponse("<script>alert('canceled');window.location='/vieworder';</script>")