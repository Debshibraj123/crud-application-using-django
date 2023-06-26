from django.shortcuts import render, HttpResponseRedirect
from .models import User, School
from .forms import StudentRegistration, SchoolForm

# Create your views here.

#this will add school

def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            #form = SchoolForm()
            #new
            return HttpResponseRedirect('schools')
    else:
        form = SchoolForm()
    schools = School.objects.all()
    return render(request, 'enroll/add_school.html', {'form': form, 'schools': schools})

#new
def show_schools(request):
    schools = School.objects.all()
    return render(request, 'enroll/show_schools.html', {'schools': schools})


#this will add item
def add_show(request):

    fm = StudentRegistration(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            school = fm.cleaned_data['school']
            if school.is_active:
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']

                if User.objects.filter(email=em).exists():
                    return render(request, 'enroll/addandshow.html', {'form': fm, 'error_message': 'User with this email already exists.'})

                if User.objects.filter(name=nm).exists():
                    return render(request, 'enroll/addandshow.html', {'form': fm, 'error_message': 'User with this email already exists.'})

                reg = User(name=nm, email=em, password=pw,school=school)
                reg.save()
                fm = StudentRegistration()
                
            else:
                
                return render(request, 'enroll/addandshow.html', {'form': fm, 'error_message': 'The selected school is not active now'})
    
    
    else:
        fm = StudentRegistration()

    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu':stud})


#this will update and edit

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


# this will delete

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')








#now make a inputfield where only some schools will be added by admin and if the students are from this school then only they can register