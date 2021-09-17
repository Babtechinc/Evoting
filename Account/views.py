from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .StateLCG import stateLCG
from .models import UserAccount,Party
from Election.models import ElectionPosition
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def dashboard(request):
    PartyAll = Party.objects.order_by('-id')[:3]
    Position = ElectionPosition.objects.all()
    return render(request,'index.html',context={'PartyAll':PartyAll,'Position':Position})

def login(request):
    if request.POST:
        VoterID = request.POST['VoterID']
        Password = request.POST['Password']
        user = authenticate(username=VoterID, password=Password)
        if user is not None:
            return redirect('Dash')
        else:
            messages.error(request, "Voter does not Exist ")
    return render(request, 'Login_Page.html', context={})

def state(request):
    statedict={}
    ref = request.GET['ref']
    statedict['data']= stateLCG[ref]

    return JsonResponse(statedict)

def Register(request):


     if request.POST:

        NIN = request.POST['NIN']
        VoterID = request.POST['VoterID']
        Confirmed = request.POST['ConfirmedPassword']
        Password = request.POST['Password']
        DateIssued = request.POST['DateIssued']
        Lname = request.POST['Lname']
        Mname = request.POST['Mname']
        Fname = request.POST['Fname']
        DOB = request.POST['DOB']
        Email = request.POST['Email']
        LocalGovernment = request.POST['LocalGovernment']
        state = request.POST['state']
        if Password  == Confirmed:
            user = User.objects.create_user(VoterID, Email, Password)
            voter = UserAccount.objects.create(NIN=NIN, VoteId=VoterID, Password=Password, UserID=user,Email=Email,
                                               DateIssued=DateIssued, Lastname=Lname, Firstname=Fname, DOB=DOB,
                                               Middlename=Mname, LocalGovernment=LocalGovernment, state=state
                                               )
            return redirect('login')
        else:
            pass
     return render(request,'Register.html',context={'stateLCG':stateLCG})