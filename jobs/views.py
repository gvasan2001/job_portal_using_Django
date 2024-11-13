from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, addJob, userApply,company_schedule
from .form import CompanyForm, CompanyAddJob, viewApplication,Company_Schedule

# Create your views here.
def index(request):
    return render(request,'index.html')

    
def company_login(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        data= Company.objects.filter(username=username,password=password)

        if data.exists():
            return render(request, 'company_home.html')
        else:
            error_message = "invalid username or password"
            return render(request, 'company_login.html',{'error_message':error_message})
    else:
        return render(request, 'company_login.html')
    
def company_home(request):
    return render(request, 'company_home.html')
    
def company_register(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'company_login.html') # Redirect to a success page after saving
    else:
        form = CompanyForm()  # Instantiate an empty form for GET request

    return render(request, 'company_register.html', {'form': form})  

def user_login(request):
    if request.method == 'POST':

        username =request.POST.get('username')
        password = request.POST.get('password')

        data= Company.objects.filter(companyname=username,password=password)
       

        if data.exists():
            
            global name
            global phonenumber
            for i in data:
                name = i.username
                phonenumber = i.number
            # print(name,phonenumber)
            return render(request, 'user_home.html')
            
        else:
            error_message = "invalid username or password"
            return render(request, 'user_login.html',{'error_message':error_message})
    else:
        return render(request, 'user_login.html')
    
def user_register(request):
    if request.method == 'POST':
        
        form = CompanyForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save() # Save the form data to the database
            return render(request, 'user_login.html') # Redirect to a success page after saving
        else:
            print("valga")
    else:
        form = CompanyForm() # Instantiate an empty form for GET request

    return render(request, 'user_register.html', {'form': form}) 

def add_job(request):
    if request.method == 'POST':
        form = CompanyAddJob(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'company_add_job.html')
    else:
        return render(request, 'company_add_job.html')
    
def user_home(request):
    return render(request, 'user_home.html')


def view_job(request):
    data = addJob.objects.all
    if data:
        return render(request, 'user_view_job.html' , {'data':data})
    else:
        return render(request, 'user_view_job.html')
    
def apply_job(request):
    from django.shortcuts import render, redirect
from .models import userApply, company_schedule, addJob

def apply_job(request):

    if request.method == 'POST':
        application = userApply(
            name=request.POST['name'],
            company=request.POST['company'],
            email=request.POST['email'],
            phonenumber=request.POST['phonenumber'],
            qualification=request.POST['qualification'],
            address=request.POST['address'],
            jobrole=request.POST['jobrole'],
            resume=request.FILES['resume'],  # Initial status of the application
            time='-',  # Set default time or retrieve from request if needed
            date='-',  # Set default date or retrieve from request if needed
            place='-'
        )
        application.save()  # Save user application

        # Now create a corresponding company_schedule entry
        schedule = company_schedule(
            username=application.name,  # Store the applicant's name
            jobrole=application.company ,  # Use the job title
            company=application.jobrole,  # Use the company associated with the job
            status='Applied',  # Initial status of the application
            time='-',  # Set default time or retrieve from request if needed
            date='-',  # Set default date or retrieve from request if needed
            place='-'  # Set appropriate place or retrieve from request
        )
        schedule.save()  # Save the schedule entry

        return render(request, 'apply_job.html', {})  # Redirect to a success page to prevent resubmission

    else:
        form = userApply()  # This line is incorrect; you should use a form class instead

    # In both cases, render the form (with or without errors)
    return render(request, 'apply_job.html', {})  # Include job info in the context


def view_application(request):
    data = userApply.objects.all
    if data:
        return render(request, 'company_view_apply.html' , {'data':data})
    else:
        return render(request, 'company_view_apply.html')
    
    
def shedule(request):
        if request.method == 'post':
            form = Company_Schedule(request.post)
            if form.is_valid():
                form.save()
                return render(request,'comapny_schedule.html')
        else:
            return render(request, 'company_schedule.html', {})

def view_status(request):
    data = userApply.objects.all
    if data:  # Use exists() to check for matches
            return render(request, 'user_view_status.html', {'data': data})
    else:
         return render(request, 'user_view_status.html')
   


