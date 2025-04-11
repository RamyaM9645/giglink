from django.db import models

# Create your models here.
class log(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)

    def __str__(self):
        return f"{self.username} - {self.password} - {self.usertype}"
    
    
class department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=225)
   

class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(log,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    location_details=models.CharField(max_length=225)
    industry_type=models.CharField(max_length=225)
    company_description=models.CharField(max_length=225)


class student(models.Model):
    student_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(log,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    resume_upload=models.FileField(max_length=225)
    department=models.ForeignKey(department,on_delete=models.CASCADE)




class Freelance(models.Model):
    class Meta:
        verbose_name_plural = 'freelance User Registeration'

    def __str__(self):
        return self.name
    
    login=models.ForeignKey(log,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    location = models.CharField(max_length=225)



class FreelanceJobs(models.Model):
    class Meta:
        verbose_name_plural = 'freelance Jobs'

    job_title = models.CharField(max_length=225)
    job_description = models.CharField(max_length=225)
    required_skill = models.CharField(max_length=225)
    expected_duration = models.CharField(max_length=225)
    payment = models.CharField(max_length=225)
    payment_type = models.CharField(max_length=225,choices = (

        ("One Time", "One Time"),
        ("Milestone Based", "Milestone Based"),
        ("Hourly", "Hourly"),
    
    ))
    freelance = models.ForeignKey(Freelance, on_delete=models.CASCADE)






class Parttime(models.Model):
    class Meta:
        verbose_name_plural = 'Partime User Registeration'

    def __str__(self):
        return self.name
    
    login=models.ForeignKey(log,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    location = models.CharField(max_length=225)



class ParttimeJobs(models.Model):
    class Meta:
        verbose_name_plural = 'Parttime Jobs'

    job_title = models.CharField(max_length=225)
    job_description = models.CharField(max_length=225)
    working_hours = models.CharField(max_length=225)
    payment = models.CharField(max_length=225)
    shift_timing = models.CharField(max_length=225,choices = (

        ("Morning", "Morning"),
        ("Evening", "Evening"),
        ("Night", "Night"),
        ("Flexible", "Flexible"),
    
    ))
    parttime = models.ForeignKey(Parttime, on_delete=models.CASCADE)





  


class job_vaccany(models.Model):
    job_id=models.AutoField(primary_key=True)
    company=models.ForeignKey(company,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=225)
    job_description=models.CharField(max_length=225)
    required_skill=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    

class application_request(models.Model):
    application_id=models.AutoField(primary_key=True)
    job=models.ForeignKey(job_vaccany,on_delete=models.CASCADE)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    application_status=models.CharField(max_length=225)



class Freelance_application_request(models.Model):
    application_id=models.AutoField(primary_key=True)
    job=models.ForeignKey(FreelanceJobs,on_delete=models.CASCADE)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    application_status=models.CharField(max_length=225)





class Parttime_application_request(models.Model):
    application_id=models.AutoField(primary_key=True)
    job=models.ForeignKey(ParttimeJobs,on_delete=models.CASCADE)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    application_status=models.CharField(max_length=225)






class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    login= models.ForeignKey(log,on_delete=models.CASCADE)  
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
