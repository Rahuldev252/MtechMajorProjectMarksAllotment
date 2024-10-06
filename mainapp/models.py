from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
   # phone = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    ROLE_CHOICES = [
        ('mentor', 'Mentor'),
        ('examiner', 'Examiner'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='mentor')
    name = models.CharField(max_length=100,null=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # def save(self, *args, **kwargs):
    #     # Automatically set the name to user.username before saving
    #     self.name = self.user.username
    #     super(Student, self).save(*args, **kwargs)

    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True)
    # def save(self, *args, **kwargs):
    #     # Automatically set the name to user.username before saving
    #     self.email = self.user.email
    #     super(Student, self).save(*args, **kwargs)
    project_title = models.CharField(max_length=255,default='N/A')
    presentation_date = models.DateField(null=True)

    presentation_from_time = models.CharField(max_length=100,default='N/A')
    presentation_to_time = models.CharField(max_length=100,default='N/A')

    
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentored_students')  # Change related_name
    examiner1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='examined_students1')  # Change related_name
    examiner2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='examined_students2')  # Change related_name
    examiner3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='examined_students3')  # Change related_name
    
    submission_status = models.CharField(
        max_length=10,
        choices=[('green', 'Submitted'), ('red', 'Not Submitted')],
        default='red'
    )
    midsem_marks = models.IntegerField(default=0)
    total_midsem_marks = models.IntegerField(default=0)
    endsem_marks = models.IntegerField(default=0)
    total_endsem_marks = models.IntegerField(default=0)

    password = models.CharField(max_length=128)
    professor_marks = models.IntegerField(default=0)
    examiner1_marks = models.IntegerField(default=0)
    examiner2_marks = models.IntegerField(default=0)
    examiner3_marks = models.IntegerField(default=0)
    professor_endmarks = models.IntegerField(default=0)
    examiner1_endmarks = models.IntegerField(default=0)
    examiner2_endmarks = models.IntegerField(default=0)
    examiner3_endmarks = models.IntegerField(default=0)

    midsem_marks = models.IntegerField(default=0)
    total_midsem_marks = models.IntegerField(default=0)
    endsem_marks = models.IntegerField(default=0)
    total_endsem_marks = models.IntegerField(default=0)

    submission_status = models.CharField(
        max_length=10,
        choices=[('green', 'Submitted'), ('red', 'Not Submitted')],
        default='red'
    )

    def update_total_marks(self):
        self.total_midsem_marks = (
            self.professor_marks +
            self.examiner1_marks +
            self.examiner2_marks +
            self.examiner3_marks
        )
        self.total_endsem_marks = (
            self.professor_endmarks +
            self.examiner1_endmarks +
            self.examiner2_endmarks +
            self.examiner3_endmarks
        )

        self.save()

    def check_all_marks_submitted(self):
        return all([
            self.professor_marks > 0,
            self.examiner1_marks > 0,
            self.examiner2_marks > 0,
            self.examiner3_marks > 0
        ])

    def update_submission_status(self):
        if self.check_all_marks_submitted():
            self.submission_status = 'green'
        else:
            self.submission_status = 'red'
        self.save()
    
    def __str__(self):
        return f"{self.name} ({self.roll_number})"

    @property
    def total_marks(self):
        return self.total_midsem_marks + self.total_endsem_marks



class MarkSheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Professor who submitted the marks
    guide_name = models.CharField(max_length=100)
    presentation_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    project_title = models.CharField(max_length=200)
    
    # Marks fields
    depth_of_understanding = models.IntegerField(null=True)
    work_done_and_results = models.IntegerField(null=True)
    exceptional_work = models.IntegerField(null=True)
    viva_voce = models.IntegerField(null=True)
    presentation = models.IntegerField(null=True)
    report = models.IntegerField(null=True)
    attendance = models.IntegerField(null=True,default=0)

    submitted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name}'s Marksheet - {self.project_title}"

    @property
    def total_marks(self):
         return (
        (self.depth_of_understanding or 0) +
        (self.work_done_and_results or 0) +
        (self.exceptional_work or 0) +
        (self.viva_voce or 0) +
        (self.presentation or 0) +
        (self.report or 0) +
        (self.attendance or 0)
    )
