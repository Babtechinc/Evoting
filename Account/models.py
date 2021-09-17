from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os
def create_path(self, filename):
    url = "party/%s/%s" % (self.NameofOrganisation, filename)
    return os.path.join(
        'party',
        self.NameofOrganisation,
        filename
    )
class Party(models.Model):
    PartyName = models.CharField(null=True, max_length=255, blank=True)
    PartyAcronym = models.CharField(null=True, max_length=255, blank=True)
    PartyEmail = models.CharField(null=True, max_length=255, blank=True)
    Username = models.CharField(null=True, max_length=255, blank=True)
    Password = models.CharField(null=True, blank=True, max_length=255)
    Logo = models.FileField(null=True, upload_to=create_path,blank=True,max_length=255)
    UserId = models.ForeignKey(User,models.CASCADE)

    class Meta:
        permissions =  [
            ("voter", "Voter"),



        ]


class UserAccount(models.Model):
    UserID  = models.ForeignKey(User,models.CASCADE)
    Password = models.CharField(null=True,blank=True,max_length=255)
    NIN = models.CharField(null=True,blank=True,max_length=255)
    Email = models.CharField(null=True,blank=True,max_length=255)
    DateIssued = models.DateField(null=True,blank=True)
    VoteId = models.CharField(null=True,blank=True,max_length=255)
    Lastname = models.CharField(null=True,blank=True,max_length=255)
    Middlename = models.CharField(null=True,blank=True,max_length=255)
    Firstname = models.CharField(null=True,blank=True,max_length=255)
    DOB = models.DateField(null=True,blank=True)
    LocalGovernment = models.CharField(null=True,blank=True,max_length=255)
    state = models.CharField(null=True,blank=True,max_length=255)
    PicPofile = models.FileField(null=True, upload_to=create_path,blank=True,max_length=255)
    Party = models.ForeignKey(Party,models.CASCADE,null=True,blank=True,)

    class Meta:
        permissions =  [
            ("party", "Party"),
        ]
