from django.db import models

# Create your models here.
class Company(models.Model):
    user_id = models.AutoField(primary_key=True)  # Custom primary key
    username = models.CharField(max_length=50)
    companyname = models.CharField(max_length=100, default='SOME STRING')
    email = models.CharField(max_length=100, default='SOME STRING')
    number = models.CharField(max_length=100, default='SOME STRING')
    address = models.CharField(max_length=100, default='SOME STRING')
    password = models.CharField(max_length=100, default='SOME STRING')
      # Adjust the max_length as needed
    
    def __str__(self):
        return self.username
    
class addJob(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=225)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    # posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class userApply(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    jobrole = models.CharField(max_length=100)
    resume = models.FileField(upload_to='uploads/')
    time = models.CharField(max_length=100, default='SOME STRING')
    date = models.CharField(max_length=100, default='SOME STRING')
    place = models.CharField(max_length=100, default='SOME STRING')
    def __str__(self):
        return self.name
    
class company_schedule(models.Model):
    username = models.CharField(max_length=100, default='SOME STRING')
    jobrole = models.CharField(max_length=100, default='SOME STRING')
    company = models.CharField(max_length=100, default='SOME STRING')
    status = models.CharField(max_length=100, default='SOME STRING')
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.username

    