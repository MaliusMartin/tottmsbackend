from django.db import models

from datetime import date, timedelta

# Create your models here.


# Define the EducationLevel model
class EducationLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# # Define the SchoolLevel model
class SchoolLevel(models.Model): 
    levelName = models.CharField(max_length=100,null=True)
    subvote = models.IntegerField(null=True)
    def __str__(self):
        return self.levelName
    
# Define the Region model
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# Define the District model
class District(models.Model):
    name = models.CharField(max_length=100)
    votecode = models.CharField(max_length=20, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}, {self.region}"

# Define the School model
class School(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    School_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name},{self.School_level},{self.region} {self.district}"
    
# Define the Subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    subjectcode=models.IntegerField( unique=True,null=True)

    def __str__(self):
        return self.name
    
class WorkerGrade(models.Model):
    grade = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.grade
    
class SalaryScale(models.Model):
    scale= models.CharField(max_length=50,null=True)
    amount = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.scale



# Define the Teacher model
class Teacher(models.Model):
    fname = models.CharField(max_length=100,null=True)
    mname = models.CharField(max_length=100,null=True)
    sname = models.CharField(max_length=100, null=True)
    check_number = models.CharField(max_length=20, unique=True,null=True)  # This is your primary key
    position = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=10,null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    date_of_birth = models.DateField(null=True)  # Add this field for the teacher's date of birth
    expected_retirement_date = models.DateField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    school_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, null=True)
    subjects_taught = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=True)  # You should hash and salt passwords
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # subvote = models.CharField(max_length=10, null=True) will be equal to the subject id
    # votecode = models.CharField(max_length=10) will be equal to the district id

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Calculate the expected retirement date based on the start_date and date_of_birth
        years_of_service = (self.start_date - self.date_of_birth).days / 365
        retirement_age = 60  # Adjust this to the retirement age in your context
        retirement_date = self.start_date + timedelta(days=(retirement_age - years_of_service) * 365)
        
        self.expected_retirement_date = retirement_date
        super(Teacher, self).save(*args, **kwargs)

    
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
    Reasons = models.TextField()
    ApplicationDate = models.DateField()
    SupportingDocuments = models.FileField(upload_to='supporting_documents/')
    FromDistrictID = models.ForeignKey(District, on_delete=models.CASCADE, related_name='from_district')
    ToDistrictID = models.ForeignKey(District, on_delete=models.CASCADE, related_name='to_district')
    RequestedDistrictID = models.ForeignKey(District, on_delete=models.CASCADE, related_name='requested_district')
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

# Define the Request model
class Request(models.Model):
    RegionID = models.ForeignKey(Region, on_delete=models.CASCADE)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE)
    SubjectID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    filled = models.BooleanField(default=False)

    def __str__(self):
        return f"Request #{self.RequestID}"

# Define the ArrivingTeachers model
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

# Define the UserRoleAssignment model
class UserRoleAssignment(models.Model):
    UserID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    RoleID = models.ForeignKey(UserRoles, on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment #{self.AssignmentID}"


    
# Define the Notification model
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