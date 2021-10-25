from django.db import models
from django.utils.timezone import now

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

TITLE = (
    ('Mr.', 'Mr.'),
    ('Miss', 'Miss.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Khun.', 'Khun.'),
    ('Dr.', 'Dr.'),
)
class People(models.Model):
    firstname = models.CharField(max_length=150, null=True,  blank=True)
    lastname = models.CharField(max_length=150, null=True,  blank=True)
    nickname = models.CharField(max_length=100, null=True,  blank=True)
    gender = models.CharField(max_length=15, choices=GENDER, null=True,  blank=True)
    title = models.CharField(max_length=25,choices=TITLE, null=True,  blank=True)
    dob = models.DateField(null=True, blank=True) 
    import_key = models.CharField(max_length=150, blank=True, null=True)
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.firstname +  ' ' + str(self.lastname) + ' (' +str(self.id) + ')'
    
    class Meta:
       ordering = ('firstname',)
       verbose_name_plural = "People"

class Family(models.Model):
    family = models.CharField(max_length=150, null=True, blank=True)
    father = models.ForeignKey(People, on_delete=models.CASCADE,related_name='father', null=True, blank=True)
    mother = models.ForeignKey(People, on_delete=models.CASCADE, related_name='mother', null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateField(default=now)

    def __str__(self):
        return self.family
    
    class Meta:
        ordering = ['family']
        verbose_name_plural = "Families"

FAMILY_ROLE = (
    ('Father','Father'),
    ('Mother','Mother'),
    ('Son','Son'),
    ('Daughter','Daughter'),
    ('Guardian', 'Guardian')
)
class LinkFamilyMember(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)   
    role = models.CharField(max_length=80, blank=True, null=True, choices=FAMILY_ROLE)
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    emergency = models.BooleanField(default=False)     
    active = models.BooleanField(default=True)   
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)


    
