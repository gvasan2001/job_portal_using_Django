from django import forms
from .models import Company,addJob,userApply,company_schedule

class CompanyForm(forms.ModelForm):  # Corrected `Model.form` to `ModelForm`
    class Meta:
        model = Company
        fields = ['username','companyname','email','number','address','password']  # Specify the fields to include in the form

class CompanyAddJob(forms.ModelForm):
    class Meta:
        model = addJob
        fields = ['title','description','company','location','salary','experience']

class viewApplication(forms.ModelForm):
    class Meta:
        model = userApply
        fields = ['name','company','email','phonenumber','qualification','address','jobrole','resume','time','date','place']

class Company_Schedule(forms.ModelForm):
    class Meta:
        model = company_schedule
        fields = ['username','jobrole','company','status','time','date','place']