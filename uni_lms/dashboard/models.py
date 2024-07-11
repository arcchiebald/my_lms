from django.db import models
from users.models import LmsUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class Student(LmsUser):
    faculty = models.CharField(max_length=50)
    gpa = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)],
        help_text="GPA must be between 0.00 and 4.00"
    )
    current_semester = models.IntegerField(
        choices=
            [
                (1, '1'), (2, '2'), (3, '3'), (4, '4'),
                (5, '5'), (6, '6'), (7, '7'), (8, '8')                                      
            ],
        default=1
        )
    subjects = models.CharField(
        max_length=100, 
        validators=[
            RegexValidator(
                regex=r'^([a-zA-Z0-9-]+\/)*[a-zA-Z0-9-]+$',
                message="Enter a list of subjects separated by symbol '/'. Example: i2i/mnsc/calc/fop/db",
                code="invalid-subjects"
            )])
    gpa_history = models.CharField(
        max_length=50, 
        validators=[
            RegexValidator(
                regex=r'^(4\.00|[0-3](\.\d{1,2})?)(\/(4\.00|[0-3](\.\d{1,2})?))*$',
                message="Enter a list of gpa's per semester separated by symbol '/'. Example: 3.40/2/2.5/1.95",
                code="invalid-gpahistory"
            )])
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return self.username
    
    

    