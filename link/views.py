from django.shortcuts import render,HttpResponse

from link.models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import JsonResponse

from django.db.models import Q


from datetime import *



def home(request):
    return render(request,'home.html')


def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        
        try:
            lg=log.objects.get(username=uname,password=psw)
            print(lg,"///////////////")
            
            request.session['login_id']=lg.pk
            lid=request.session['login_id']
            
            if lg.usertype=='admin':
                return HttpResponse("<script>alert('Login Successfully');window.location='adm';</script>")
            
            
            elif lg.usertype=='company':
                q=company.objects.get(login_id=lid)
                if q:
                    
                    request.session['cid']=q.pk
                    
                    return HttpResponse("<script>alert('Login Successfully');window.location='chome';</script>")
                
            elif lg.usertype=='student':
                q=student.objects.get(login_id=lid)
                if q:
                    
                    request.session['sid']=q.pk
                   
                    
                    
                    return HttpResponse("<script>alert('Login Successfully');window.location='shome';</script>")
                
            
            
            
            
        except:
            return HttpResponse("<script>alert('Login Failed...!!!!');window.location='login';</script>")
    

    return render(request,'login.html')



def chome(request):
    return render(request,'company.html')


def adm(request):
    return render(request,'admin.html')


def shome(request):
    return render(request,'student.html')



def adm_companies(request):
    a=company.objects.all()
    return render(request,'adm_companies.html',{'a':a})

def adm_vaccancy(request,id):
    a=job_vaccany.objects.filter(company_id=id)
    return render(request,'adm_vaccany.html',{'a':a})

def adm_request(request,id):
    a=application_request.objects.filter(job_id=id)
    return render(request,'adm_request.html',{'a':a})


def accept_com(request,id):
    a=log.objects.get(login_id=id)
    a.usertype='company'
    a.save()
    return HttpResponse("<script>alert('Accepted successfully');window.location='/adm_companies';</script>")

def reject_com(request,id):
    a=log.objects.get(login_id=id)
    a.usertype='rejected'
    a.save()
    return HttpResponse("<script>alert('Rejected successfully');window.location='/adm_companies';</script>")


def accept_stu(request,id):
    a=log.objects.get(login_id=id)
    a.usertype='student'
    a.save()
    return HttpResponse("<script>alert('Accepted successfully');window.location='/adm_student';</script>")

def reject_stu(request,id):
    a=log.objects.get(login_id=id)
    a.usertype='rejected'
    a.save()
    return HttpResponse("<script>alert('Rejected successfully');window.location='/adm_student';</script>")





def adm_student(request):
    a=student.objects.all()
    return render(request,'adm_student.html',{'a':a})



def adm_department(request):
    a=department.objects.all()
    if request.method=='POST':
        dep=request.POST['dep']
        
        z=department(department_name=dep)
        z.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/adm_department';</script>")
        
    return render(request,'adm_depatment.html',{'a':a})


def adm_complaint(request):
    a=Complaint.objects.all()
    return render(request,'adm_complaint.html',{'a':a})

def adm_reply(request,id):
    a=Complaint.objects.get(pk=id)
    if request.method=='POST':
        rep=request.POST['rep']
        
        a.reply=rep
        a.save()
        return HttpResponse("<script>alert('Replied successfully');window.location='/adm_complaint';</script>")
        
    return render(request,'adm_reply.html')


def company_reg(request):
    
    if request.method=='POST':
        cname=request.POST['cname']
        email=request.POST['email']
        phone=request.POST['phone']
        place=request.POST['place']
        location=request.POST['location']
        itype=request.POST['itype']
        cdes=request.POST['cdes']
        uname=request.POST['uname']
        psw=request.POST['psw']
        
        tp=log.objects.filter(username=uname)
        
        if tp:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/company_reg'</script>")
        else:
            z=log(username=uname,password=psw,usertype='pending')
            z.save()
            
            t=company(company_name=cname,phone=phone,email=email,place=place,location_details=location,industry_type=itype,company_description=cdes,login=z)
            t.save()
            return HttpResponse("<script>alert('Registered successfully');window.location='/login';</script>")
 
    
   
    return render(request,'company_reg.html')



def company_profile(request):
    a=company.objects.filter(pk=request.session['cid'])
    return render(request,'company_profile.html',{'a':a})

def add_vaccancy(request):
    a=job_vaccany.objects.filter(company_id=request.session['cid'])
    
    if request.method=='POST':
        title=request.POST['title']
        des=request.POST['des']
        skill=request.POST['skill']
     
     
        
        tp=job_vaccany.objects.filter(job_title=title)
        
        if tp:
            return HttpResponse("<script>alert('Title Already Exist');window.location='/add_vaccancy'</script>")
        else:
           
            
            t=job_vaccany(job_title=title,job_description=des,required_skill=skill,status='pending',company_id=request.session['cid'])
            t.save()
            return HttpResponse("<script>alert('Added successfully');window.location='/add_vaccancy';</script>")
 
    return render(request,'add_vaccancy.html',{'a':a})


def job_request(request,id):
    a=application_request.objects.filter(job_id=id)
    return render(request,'job_request.html',{'a':a})


def com_complaint(request):
    a=Complaint.objects.filter(login_id=request.session['login_id'])
    return render(request,'com_complaint.html',{'a':a})



def student_reg(request):
    a=department.objects.all()
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        resume=request.FILES['resume']
        fs=FileSystemStorage()
        file=fs.save(resume.name,resume)
        dep=request.POST['dep']
        uname=request.POST['uname']
        psw=request.POST['psw']
        
        tp=log.objects.filter(username=uname)
        
        if tp:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/student_reg'</script>")
        else:
            z=log(username=uname,password=psw,usertype='pending')
            z.save()
            
            t=student(fname=fname,lname=lname,phone=phone,email=email,resume_upload=file,department_id=dep,login=z)
            t.save()
            return HttpResponse("<script>alert('Registered successfully');window.location='/login';</script>")
 
  
    return render(request,'student_register.html',{'a':a})



def stu_profile(request):
    
    a=student.objects.filter(pk=request.session['sid'])
    
    b=department.objects.all()

    return render(request,'student_profile.html',{'a':a,'b':b})


def stu_companies(request):
    a=company.objects.all()

    return render(request,'student_companies.html',{'a':a})

def stu_complaint(request):
    a=Complaint.objects.filter(login_id=request.session['login_id'])
    if request.method=='POST':
        com=request.POST['com']
        
        z=Complaint(complaint=com,reply='pending',date=datetime.now().date(),login_id=request.session['login_id'])
        z.save()
        return HttpResponse("<script>alert('Submitted');window.location='/stu_complaint';</script>")
        

    return render(request,'student_complaint.html',{'a':a})



import PyPDF2
import docx
import spacy
import re
from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_sm')

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract keywords/skills from the resume text
def extract_skills(text):
    # Tokenize the resume text into words
    words = set(re.findall(r'\b\w+\b', text.lower()))  # Using regex to extract words
    return words

# Function to calculate similarity between resume words and job details
def calculate_similarity(resume_words, job_title, required_skills):
    job_combined = job_title + " " + required_skills  # Combine job title and required skills
    vectorizer = CountVectorizer().fit_transform([resume_words, job_combined])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0][1]  # Return the similarity score

# Your Django view
def std_vaccancy(request, id):
    student_obj = student.objects.get(student_id=request.session['sid'])
    
    # Path to the uploaded resume file
    resume_file = student_obj.resume_upload.path
    
    # Extract resume text based on the file type
    if resume_file.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_file)
    else:
        resume_text = ""  # Handle other file types accordingly
    
    # Extract words/skills from the resume
    resume_words = extract_skills(resume_text)
    
    # Fetch job vacancies for the company
    job_vacancies = job_vaccany.objects.filter(company_id=id)
    matched_jobs = []
    threshold = 0.2  # Set your similarity threshold here

    for job in job_vacancies:
        # Get job title and required skills as a set of words
        job_title = job.job_title.lower()
        required_skills = job.required_skill.lower()
        
        print(job_title,"///jt")
        print(required_skills,"///rs")
        
        print(resume_words,"///rw")
        
        # Calculate similarity score
        similarity_score = calculate_similarity(" ".join(resume_words), job_title, required_skills)
        
        print(similarity_score,"///")
        
        print(threshold,"///")
        
        # Check if similarity score is above the threshold
        if similarity_score >= threshold:
            matched_jobs.append(job)
            print(similarity_score,"///////")

    # Render the template with matched jobs
    return render(request, 'std_vaccancy.html', {'a': matched_jobs})



# def std_vaccancy(request,id):
#     m=student.objects.get(student_id=request.session['sid'])
#     a=job_vaccany.objects.filter(company_id=id)

#     return render(request,'std_vaccancy.html',{'a':a})


def std_request(request,id):
    try:
        
        z=application_request.objects.filter(job_id=id,application_status='pending')
        if z:
            return HttpResponse("<script>alert('Already Applied');window.location='/stu_companies';</script>")
        else:
            a=application_request(application_status='pending',job_id=id,student_id=request.session['sid'])
            a.save()
            return HttpResponse("<script>alert('Applied successfully');window.location='/stu_companies';</script>")
            
            
    except:
            return HttpResponse("<script>alert('Invalid Request');window.location='/stu_companies';</script>")
        
        
    

def accept_req(request,id):
    a=application_request.objects.get(pk=id)
    a.application_status='selected'
    a.save()
    return HttpResponse("<script>alert('Accepted successfully');window.location='/add_vaccancy';</script>")

def reject_req(request,id):
    a=application_request.objects.get(pk=id)
    a.application_status='rejected'
    a.save()
    return HttpResponse("<script>alert('Rejected successfully');window.location='/add_vaccancy';</script>")







   
