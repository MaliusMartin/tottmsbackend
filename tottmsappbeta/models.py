from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import timezone 
from django.utils.timezone import timedelta 

# Create your models here.


# the EducationLevel model
class EducationLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# # the SchoolLevel model
class SchoolLevel(models.Model): 
    levelName = models.CharField(max_length=100,null=True)
    subvote = models.IntegerField(null=True)
    def __str__(self):
        return self.levelName
    
# the Region model
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# the District model
class District(models.Model):
    name = models.CharField(max_length=100)
    votecode = models.CharField(max_length=20, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}, {self.region}"

# the School model
class School(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    School_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name},{self.School_level},{self.region} {self.district}"
    
# the Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    subjectcode=models.IntegerField( unique=True,null=True)

    def __str__(self):
        return self.name
    
# the WorkerGrade model
    
class WorkerGrade(models.Model):
    grade = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.grade

# the SalaryScale model
    
class SalaryScale(models.Model):
    scale= models.CharField(max_length=50,null=True)
    amount = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.scale

#the gender model

class Gender(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

#the position model
    
class Position(models.Model):
    name = models.CharField(max_length=110)
    def __str__(self) -> str:
        return self.name

# the Teacher model
class Teacher(models.Model):
    fname = models.CharField(max_length=100,null=True)
    mname = models.CharField(max_length=100,null=True)
    sname = models.CharField(max_length=100, null=True)
    check_number = models.CharField(max_length=20, unique=True,null=True) 
    grade = models.ForeignKey(WorkerGrade, on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    date_of_birth = models.DateField(null=True)
    expected_retirement_date = models.DateField(null=True, blank=True) #
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    school_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, null=True)
    subjects_taught = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    image= models.ImageField(upload_to='images/',null=True, blank=True)

    password = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
            if self.password:
                self.password = make_password(self.password)
            super().save(*args, **kwargs)
    password = models.CharField(max_length=100, null=True, blank=True)  # You should hash and salt passwords
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

 

    def save(self, *args, **kwargs):
        if self.date_of_birth and self.start_date:
            # Calculate the expected retirement date
            years_of_service = (self.start_date - self.date_of_birth).days / 365
            retirement_age = 60  
            retirement_date = self.start_date + timezone.timedelta(days=int((retirement_age - years_of_service) * 365))
        
            self.expected_retirement_date = retirement_date

        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.sname

class TransferReasons(models.Model):
    reason = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return self.reason
    
    
class TransferApplication(models.Model):
    APPLICATION_TYPE_CHOICES = [
        ('Exchange', 'Exchange'),
        ('Request', 'Request'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    APPROVAL_STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Not Approved', 'Not Approved'),
    ]

   
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    ApplicationType = models.CharField(max_length=20, choices=APPLICATION_TYPE_CHOICES)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    Reasons_type=models.ForeignKey(TransferReasons, on_delete=models.CASCADE, null=True)
    Reasons = models.TextField()
    ApplicationDate = models.DateField(auto_now_add=True)
    SupportingDocuments = models.FileField(upload_to='supporting_documents/')
    FromRegionID = models.ForeignKey(Region,on_delete=models.CASCADE, blank=True, null=True,related_name='from_region')
    FromDistrictID = models.ForeignKey(District, on_delete=models.CASCADE, related_name='from_district')
    ToRegionID = models.ForeignKey(Region, blank=True,on_delete=models.CASCADE, null=True,related_name='to_region')
    ToDistrictID = models.ForeignKey(District, on_delete=models.CASCADE, related_name='to_district')
    Comments = models.TextField(blank=True, null=True)
    ApprovalStatus = models.CharField(max_length=20, choices=APPROVAL_STATUS_CHOICES)
    decision_date = models.DateField(auto_now=True,null=True)


    def __str__(self):
        return f"Application #{self.ApplicationID} - {self.TeacherID.name}"

class SpecialTransfer(models.Model):
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Reason = models.TextField()
    Date = models.DateField(auto_now=True,null=True)
    status = models.CharField(max_length=20, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))

    def __str__(self):
        return f"Special Transfer #{self.SpecialTransferID}"

# the Request model
class Request(models.Model):
    RegionID = models.ForeignKey(Region, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    SubjectID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    filled = models.BooleanField(default=False)

    def __str__(self):
        return f"Request #{self.RequestID}"

# the ArrivingTeachers model
class ArrivingTeachers(models.Model):
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    ArrivalDate = models.DateField()
    AssignedSchoolID = models.ForeignKey(School, on_delete=models.CASCADE)
    departure_date = models.DateField(auto_now=True,null=True)

    def __str__(self):
        return f"Arriving Teacher #{self.ArrivingTeacherID}"
    
class UserRoles(models.Model):
    RoleName = models.CharField(max_length=100)

    def __str__(self):
        return self.RoleName

# the UserRoleAssignment model
class UserRoleAssignment(models.Model):
    UserID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    RoleID = models.ForeignKey(UserRoles, on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment #{self.AssignmentID}"


    
# the Notification model
class Notification(models.Model):
    UserID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Content = models.TextField()
    DateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification #{self.NotificationID}"
    
    
class SalaryTransfer(models.Model):
    teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,null=True, blank=True)
    
    
class Forms(models.Model):
    form_name = models.CharField(max_length=100)
    form = models.FileField(upload_to='forms/')
    
    def __str__(self):
        return self.form_name
    

    
