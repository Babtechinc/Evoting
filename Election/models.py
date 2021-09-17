from django.db import models
from Account.models import Party,UserAccount
import  os
status = [('open','Open'),('closed','Closed')]
def create_path(self, filename):
    url = "party/%s/%s" % (self.NameofOrganisation, filename)
    return os.path.join(
        'party',
        self.NameofOrganisation,
        filename
    )
# Create your models here.
class ElectionPosition(models.Model):
    Position = models.CharField(null=True, max_length=255, blank=True)
    Status = models.CharField(choices=status,default='closed',max_length=255)
class ElectionCandidate(models.Model):
    ElectionPositionID = models.ForeignKey(ElectionPosition,null=True, blank=True,on_delete=models.CASCADE)
    Election_Candidate = models.ForeignKey(UserAccount,null=True, blank=True,on_delete=models.CASCADE)
    ElectionState = models.CharField(null=True, max_length=255, blank=True)
    ElectionParty = models.ForeignKey(Party, null=True, blank=True, on_delete=models.CASCADE)
    ElectionYear    = models.CharField(null=True, max_length=255, blank=True)
    Electionmanifestoes = models.FileField(null=True, upload_to=create_path, blank=True, max_length=255)
class Electionvote(models.Model):
    ElectionCandidateID = models.ForeignKey(ElectionCandidate,null=True, blank=True,on_delete=models.CASCADE)
    ElectionUser = models.ForeignKey(UserAccount, null=True, blank=True, on_delete=models.CASCADE)
    ElectionYear = models.CharField(null=True, max_length=255, blank=True)

