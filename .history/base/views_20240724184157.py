from django.shortcuts import render
from django.con
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
def register(request):
    page="resister"
    if request.method =="POST":
        return _extracted_from_register_4(request)
    context={"page":page}
    return render(request,"base/login_page.html",context)
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
        profile = UserProfile.objects.create(user=user, profilePicture=picture, dateOfBirth=None)
        profile.save()
        login(request, user)
        send_mail_task.delay(email, fullname)
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

