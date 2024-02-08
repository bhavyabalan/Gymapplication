from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Attendance

# Create your views here.
def Home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    selectTrainer=Trainer.objects.all()
    context={"SelectTrainer":selectTrainer}
    if request.method=="POST":
        PhoneNumber = request.POST.get('PhoneNUmber')
        Login=request.POST.get('logintime')
        Logout = request.POST.get('loginout')
        SelectWorkout= request.POST.get('workout')
        TrainedBy= request.POST.get('trainer')
        query=Attendance(PhoneNumber=PhoneNumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,
                         TrainedBy=TrainedBy)
        query.save()
        messages.warning(request, "Attendance Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)
def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_name=request.user
    posts=Enrollment.objects.filter(FullName=user_name)
    context={"posts":posts}
    return render(request,"profile.html",context)
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.info(request,"Your password and conform password are not same")
            return redirect('/signup')
        try:
            if User.objects.get(uname=username):
                messages.warning(request,"UserName is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
               messages.warning(request, "Email is Taken")
               return redirect('/signup')

        except Exception as identifier:
            pass

        myuser=User.objects.create_user(uname,email,pass1)
        myuser.save()
        messages.success(request,"User is created please Login")
        return redirect('/login')

    return render(request,"signup.html")


#def handlelogin(request):
 #   if request.method=="POST":
  #      username = request.POST.get('uname')
   #     password1 = request.POST.get('password1')
    #    myuser = authenticate(username=username,password1=password1)
     #   if myuser is not None:
      #      login(request,myuser)
       #     messages.success(request,"Login Successful")
        #    return redirect('/')
        #else:
         #    messages.error(request,"invalid credentials")
          #   return redirect('/login')

    #return render(request,"handlelogin.html")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        upass = request.POST.get('password')
        print("Username:", username)
        print("Password:", upass)

        myuser = authenticate(username=username, password=upass)
        print("Authenticated user:", myuser)


        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/login')

    return render(request, "handlelogin.html")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()
        messages.info(request,"Thanks for contacting us we will get back you soon")
        return redirect('/contact')
    return render(request, "contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method == "POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName= FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB= DOB,
                         SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For The Enrollment")
        return redirect('/join')

    return render(request,"enroll.html",context)