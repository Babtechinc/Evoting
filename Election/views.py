from django.contrib import messages
from django.contrib.auth.models import User, Permission
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from Account.models import Party,UserAccount
from .models import ElectionPosition,status,ElectionCandidate,Electionvote

electionPosition=[
"PRESIDENTIAL CANDIDATES",
"GOVERNORSHIP CANDIDATES",
"STATE HOUSE OF ASSEMBLY CANDIDATES",
"HOUSE OF REPRESENTATIVES CANDIDATES",
"SENATORIAL CANDIDATES"
"CHAIRMANSHIP CANDIDATES"
"COUNCILLORSHIP CANDIDATES"]

# Create your views here.
def AddParty(request):
    if request.POST:
        PartyName = request.POST['PartyName']
        uploadPath = 'media/membership/' + PartyName + '/'
        uploadPathModel = 'membership/' + PartyName+ '/'
        print(request.POST)
        logo =''
        if request.FILES['Logo']:
            logo = request.FILES['Logo']
            fs = FileSystemStorage(location=uploadPath)
            filename = fs.save(logo.name, logo)
            logo = uploadPathModel + logo.name  # saves the file to `media` folde
        PartyName =  request.POST['PartyName']
        PartyAcronym =  request.POST['PartyAcronym']
        PartyEmail =  request.POST['Email']
        Username =   request.POST['PartyAcronym']
        Password =  request.POST['Password']
        if not Party.objects.filter(Username=Username):
            user = User.objects.create_user(PartyAcronym, PartyEmail, Password)
            Party.objects.create(PartyName=PartyName,PartyAcronym=PartyAcronym,
                                 PartyEmail=PartyEmail
                                 ,Username=Username,Password=Password,Logo=logo,UserId=user)
            permission = Permission.objects.get(codename='party')
            user.user_permissions.add(permission)
            messages.success(request, "This Party "+str(PartyName)+'('+str(PartyAcronym)+') has been created')
        else:
            messages.error(request, "Party Exist")


    return render(request,'AddParty.html',context={})


def PickCandidates(request):
    partyID = Party.objects.get(UserId=request.user.id)
    uploadPath = 'media/membership/' + partyID.PartyName + '/'
    uploadPathModel = 'membership/' + partyID.PartyName + '/'
    Position = ElectionPosition.objects.all()
    UserAccountDB = UserAccount.objects.all()
    if request.POST:
        Candidate = request.POST['Candidate']
        if UserAccount.objects.filter(id=Candidate):
            Candidate = UserAccount.objects.get(id=Candidate)
        PositionPicked = request.POST['Position']
        if ElectionPosition.objects.filter(id=PositionPicked):
            PositionPicked = ElectionPosition.objects.get(id=PositionPicked)
        Year = request.POST['year']
        Manifesto  = ''
        if request.FILES['Manifesto']:
            Manifesto = request.FILES['Manifesto']
            fs = FileSystemStorage(location=uploadPath)
            filename = fs.save(Manifesto.name, Manifesto)
            Manifesto = uploadPathModel + Manifesto.name  # saves the file to `media` folde
        if not ElectionCandidate.objects.filter(ElectionParty=partyID,ElectionYear=Year,
                                                Election_Candidate=Candidate,ElectionPositionID=PositionPicked):
            ElectionCandidate.objects.create(ElectionParty=partyID, ElectionYear=Year,Electionmanifestoes=Manifesto,
                                             Election_Candidate=Candidate, ElectionPositionID=PositionPicked,ElectionState=Candidate.state)
            messages.success(request, "This User " + str(Candidate.Lastname) + '(' + str(Candidate.NIN) + ') has been Addded '
                                                                            +'As A '+PositionPicked.Position)

    return render(request,'AddPosition.html',context={'Position':Position,'UserAccountDB':UserAccountDB})


def VoteforCandidates (request,id):
    ElectionCandidateDB=ElectionCandidate.objects.filter(ElectionPositionID__id=id,ElectionYear='2021')
    if request.POST:
        Userid = UserAccount.objects.get(UserID=request.user.id)
        ElectionCandidatevote = request.POST['vote']
        if ElectionCandidate.objects.filter(id=ElectionCandidatevote):
            ElectionCandidatevote = ElectionCandidate.objects.get(id=ElectionCandidatevote)
        Electionvote.objects.create(ElectionYear='2020',ElectionUser=Userid,ElectionCandidateID=ElectionCandidatevote)
        return redirect('Analysis',ElectionCandidatevote.ElectionPositionID_id)
    return render(request,'VotingPage.html',context={'ElectionCandidateDB':ElectionCandidateDB})

def Analysis(request,id):
    Resultdict = {}
    for foo in ElectionCandidate.objects.filter(ElectionPositionID__id=id,ElectionYear='2021'):
        count=Electionvote.objects.filter(ElectionCandidateID=foo).count()
        userCount= UserAccount.objects.all().count()
        userCount = int(count)/int(userCount) * 100
        Resultdict[foo.ElectionParty.PartyAcronym]={'count':count,'userCount':userCount}

    return render(request,'VotingAnaliysis.html',context={'Resultdict':Resultdict})