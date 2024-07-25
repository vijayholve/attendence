from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login ,authenticate,logout
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template.defaulttags import register 
from .forms import studuntform ,subjectform  ,CustomUserCreationForm ,TeacherForm,AdminForm
from django.db.models import Q  
def login_page(request):
    page="login"
    username=request.POST.get("username")
    password=request.POST.get("password")
    if request.method == "POST":
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            messages.error(request,f"error is {e}")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            messages.error(request,"incorect username and password ")
    context={"page":page}
    return render(request,"base/login_page.html",context)
# def register(request):
#     page="resister"
#     if request.method =="POST":
#         return _extracted_from_register_4(request)
#     context={"page":page}
#     return render(request,"base/login_page.html",context)
# TODO Rename this here and in `register`
def _extracted_from_register_4(request):
    fullname=request.POST.get("fullname")
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    confirm_password=request.POST.get("confirm-password")
    print(fullname," ",email," ",username," ",password," ",confirm_password)
    if password != confirm_password :
        messages.error(request,"Password Does Not Matching")
        return redirect("register")
    if username is None or len(username) <  3 :
        messages.error(request,"please enter username")
        return redirect("register")
    if fullname is None or len(fullname) <= 5:
        messages.error(request,"please enter fullname")
        return redirect("register")
    if email is None or len(email) <= 5:
        messages.error(request,"please enter email")
        return redirect("register")
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        if picture:=request.FILES.get("profilePicture"):
            print("Pictrure issaved")
        else:
            picture="images/default.avif"
        # profile = UserProfile.objects.create(user=user, profilePicture=picture, dateOfBirth=None)
        # profile.save()
        login(request, user)
        # send_mail_task.delay(email, fullname)
        return redirect("home")
    except Exception as e:
        print(e)
        messages.error(request, f"error is {e}")
        context = {"page": "register"}
        return render(request, "base/login_page.html", context)

# @login_required(login_url="login-page")
def logout_page(request):
    # user=User.objects.get(id=pk)
    logout(request)
    return redirect("login-page")




def register_page(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_type = user_form.cleaned_data.get('user_type')
            print("user type is",user_type)
            login(request, user) 
            
            return redirect('user-type',user_id=user.id) 
    else:
        user_form = CustomUserCreationForm()
        # student_form = studuntform()
        # teacher_form = TeacherForm()
        # admin_form = AdminForm()
    context= {
        # 'user_form': user_form,
        # 'student_form': student_form,
        # 'teacher_form': teacher_form,
        # 'admin_form': admin_form
    }
    return render(request, 'base/register.html',context)


def user_panel(request,user_id):
    user=User.objects.get(id=user_id) 
    user_type=user.user_type.values
    if user_type == 1 :
        student_form = studuntform()
        if request.method == "POST":
            student_form = studuntform(request.POST)
            if student_form.is_valid():
                student = student_form.save(commit=False)
                student.user = user 
                student.save()
    elif user_type == 2:
        
        teacher_form = TeacherForm(request.POST)
        if request.method == "POST":
            teacher_form=TeacherForm(request.POST)
            if teacher_form.is_valid():
                teacher = teacher_form.save(commit=False)
                teacher.user = user
                teacher.save()  
                return redirect
    elif user_type == 3:
        admin_form = AdminForm(request.POST)
        if admin_form.is_valid():
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()