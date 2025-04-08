from django.shortcuts import render, redirect, get_object_or_404
from app import views
from .models import Doctor
from .models import Appoiment
from .models import Patient
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def landing(request):
    adminemail="pragati@gmail.com"
    adminpassword="pragati"
    email=request.POST.get('email')
    password=request.POST.get('password')
    if (email==adminemail and password==adminpassword):
        # return HttpResponse("Welcome Admin")
        return render(request, 'base.html')
    else:
        druser = Doctor.objects.filter(email=email)
        ptuser = Patient.objects.filter(email=email)
        if druser.exists():
            data=Doctor.objects.get(email=email)
            pass1=data.password
            if password==pass1:
                # return HttpResponse("Welcome User")
                return render(request, 'drbase.html',{'id':data.id,'name':data.name,'email':data.email,'password':data.password})
            else:
                    return render(request, 'landing.html',{'message':'Invalid email and Password'})
        elif ptuser.exists():
            data=Patient.objects.get(email=email)
            pass1=data.password
            if password==pass1:
                # return HttpResponse("Welcome User")
                return render(request, 'patientbase.html',{'id':data.id,'name':data.name,'email':data.email,'password':data.password})
            else:
                    return render(request, 'landing.html',{'message':'Invalid email and Password'})
    return render(request,'landing.html')


   

def base(request):
    return render(request,'base.html')
def drbase(request):
    return render(request,'drbase.html')
 
def booking(request):
     if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        Specilastion=request.POST.get('specilastion')
        image=request.FILES.get('image')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(name,email,phone,address,Specilastion,image,password,cpassword)
        user = Doctor.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'booking.html', {'msg': x})
        else:
            pass
        if password==cpassword:
            Doctor.objects.create(name=name,email=email,phone=phone,address=address,Specilastion=Specilastion,image=image,password=password,)
            x = "Resgistration succesfully"
            return render(request,'booking.html',{'msg':x})
        else:
            x = "password and cpassword not match"
            return render(request,'booking.html',{'msg':x,'name':name,'email':email,'phone':phone,'address':address,'Specilastion':Specilastion,'image':image})
     else:
        return render(request, 'booking.html')  
     return render(request,'booking.html')

def booking_table(request):
    dr = Doctor.objects.all()
    print(dr)
    return render(request,'booking_table.html',{'data':dr})

def update(request,pk):
    print(pk)
    if request.method=="POST":
         x = Doctor.objects.get(id=pk)
         p = request.POST.get('name')
         q = request.POST.get('email')
         r = request.POST.get('phone')
         s = request.POST.get('address')
         t = request.POST.get('Specilastion')
         u = request.FILES.get('image')
         
         print(u)
         v = request.POST.get('password')
         x.name = p
         x.email = q
         x.phone = r
         x.address = s
         x.Specilastion = t
         x.image = u
         x.password = v
         x.save()
         dr=Doctor.objects.all()
    x=Doctor.objects.get(id=pk)
    print(x)
    
    return render(request,'update.html',{'data4':x})

def delete(request,pk):
    data = Doctor.objects.get(id=pk)
    data.delete()
    dr = Doctor.objects.all()
    return render(request, 'booking_table.html',{'data':dr})


def edit(request,pk):
    print(pk)
    if request.method=="POST":
         x = Doctor.objects.get(id=pk)
         p = request.POST.get('name')
         q = request.POST.get('email')
         r = request.POST.get('phone')
         s = request.POST.get('address')
         t = request.POST.get('Specilastion')
         u = request.FILES.get('image')
         
         print(u)
         v = request.POST.get('password')
         x.name = p
         x.email = q
         x.phone = r
         x.address = s
         x.Specilastion = t
         x.image = u
         x.password = v
         x.save()
         dr=Doctor.objects.all()
    x=Doctor.objects.get(id=pk)
    print(x)
    
    return render(request,'update.html',{'data4':x})


def patient_record(request):
     pt = Patient.objects.all()
     print(pt)
     return render(request,'patient_record.html',{'data':pt})



def patient_record2(request):
    pt2 = Patient.objects.all()
    print(pt2)
    return render(request,'patient_record2.html',{'data':pt2})


# def delete(request,pk):
#     data = Patient.objects.get(id=pk)
#     data.delete()
#     pt2 = Patient.objects.all()
#     return render(request, 'patient_record2.html',{'data':pt2})

def patient_list(request):
    return render(request,'patient_list.html')
 
def drtable(request):

    dr = Doctor.objects.all()
    return render(request,'drtable.html',{'data':dr})
 
def patientbase(request):
    return render(request,'patientbase.html')

def appoiment(request,pk):
    return render(request,'appoiment.html',{'id':pk})

def appoiment_data(request,pk):
    if request.method=="POST":    
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        symptoms = request.POST.get('symptoms')
        date = request.POST.get('date')
        department = request.POST.get('department')
        gender = request.POST.get('gender')
        time = request.POST.get('time')
        
        appoiment = Appoiment(
            name=name,
            phone=phone,
            email=email,
            symptoms=symptoms,
            date=date,
            department=department,
            gender=gender,
            time=time
        )
        appoiment.save()
        id=pk
        return redirect(f'/success/?id={id}')

    
def success(request):
    iddd = request.GET.get('id')
    print(iddd)
    try:
        patient = Patient.objects.get(id=iddd)
        return render(request, 'success.html', {'patient': patient})
    except Patient.DoesNotExist:
        return HttpResponse("Patient not found", status=404)


    #  return HttpResponse("<h2>Appointment booked successfully!</h2>")

def patient_registration(request,pk):
    if request.method == 'POST':
         print(request.POST)
         print(request.FILES)
         name = request.POST.get('name')
         phone = request.POST.get('phone')
         email = request.POST.get('email')
         address = request.POST.get('address')
         gender = request.POST.get('gender')
         image=request.FILES.get('image')
         occupation=request.POST.get('occupation')
         password=request.POST.get('password')
         cpassword=request.POST.get('cpassword')
         print(name,email,phone,address,occupation,image,password,cpassword)
         user = Patient.objects.filter(email=email)
        
         if user:
            x = "Email already exist"
            return render(request, 'patient_registration.html', {'msg': x})
         else:
            pass
         if password==cpassword:
            Patient.objects.create(name=name,email=email,phone=phone,address=address,occupation=occupation,gender=gender,image=image,password=password,)
            x = "Resgistration succesfully"
           
            return render(request,'landing.html',{'msg':x})
         else:
            x = "password and cpassword not match"
            return render(request,'patient_registration.html',{'msg':x,'name':name,'email':email,'phone':phone,'address':address,'occupation':occupation,'gender':gender,'image':image})
    else:
        return render(request, 'patient_registration.html')  
    return render(request,'patient_registration.html', pk=patient.id)

    #form = patient_registration(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('landing')
    #     else:
    #         return render(request, 'patient_registration.html', {'form': form})
    # else:
    #    form = patient_registration()
    # return render(request,'patient_registration.html')


def appoiment_list(request):
    pt = Patient.objects.all()
    print(pt)
    return render(request,'appoiment_list.html',{'data':pt})
