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
    ser_form = CustomUserCreationForm()
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_type = user_form.cleaned_data.get('user_type')
            print("user type is",user_type)
            login(request, user) python manage.py makemigrations
Traceback (most recent call last):
  File "C:\Users\Vijay\python pro\attendance\attendance\manage.py", line 22, in <module>
    main()
  File "C:\Users\Vijay\python pro\attendance\attendance\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\Users\Vijay\python pro\attendance\attendance\myenv\Lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "C:\Users\Vijay\python pro\attendance\attendance\myenv\Lib\site-packages\django\core\management\__init__.py", line 416, in execute
    django.setup()
  File "C:\Users\Vijay\python pro\attendance\attendance\myenv\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Users\Vijay\python pro\attendance\attendance\myenv\Lib\site-packages\django\apps\registry.py", line 116, in populate
    app_config.import_models()
  File "C:\Users\Vijay\python pro\attendance\attendance\myenv\Lib\site-packages\django\apps\config.py", line 269, in import_models
    self.models_module = import_module(models_module_name)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Vijay\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\Vijay\python pro\attendance\attendance\students\models.py", line 16
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
IndentationError: unexpected indent
(myenv) PS C:\Users\Vijay\python pro\attendance\attendance> python manage.py makemigrations
It is impossible to add a non-nullable field 'password' to customuser without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:











            
            return redirect('user-type',user_id=user.id) 
    else:
        user_form = CustomUserCreationForm()
        # student_form = studuntform()
        # teacher_form = TeacherForm()
        # admin_form = AdminForm()
    context= {
        'user_form': user_form,
        # 'student_form': student_form,
        # 'teacher_form': teacher_form,
        # 'admin_form': admin_form
    }
    return render(request, 'base/register.html',context)


def user_panel(request,user_id):
    user=User.objects.get(id=user_id) 
    user_type=user.user_type.values
    print(user_type ," and ",user_id)
    if user_type == 1 :
        student_form = studuntform()
        if request.method == "POST":
            student_form = studuntform(request.POST)
            if student_form.is_valid():
                student = student_form.save(commit=False)
                student.user = user 
                student.save()
                return redirect('home') 
    elif user_type == 2:
        teacher_form = TeacherForm(request.POST)
        if request.method == "POST":
            teacher_form=TeacherForm(request.POST)
            if teacher_form.is_valid():
                teacher = teacher_form.save(commit=False)
                teacher.user = user
                teacher.save()  
                return redirect('home')
    elif user_type == 3:
        admin_form = AdminForm()
        if request.method == "POST":
            admin_form = AdminForm(request.POST)
            if admin_form.is_valid():
                admin = admin_form.save(commit=False)
                admin.user = user
                admin.save()
                return redirect('home')
    content={}
    return render(request,'base/user_type.html',content)