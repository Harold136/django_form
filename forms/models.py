from django.db import models
from django.urls import reverse

standing = (
    ('freshman', 'Freshman'),
    ('sophomore', 'Sophomore'),
    ('junior', 'Junior'),
    ('senior', 'Senior'),
)

languages = (
    ('python', 'Python'),
    ('java', 'Java'),
    ('cpp', 'C++'),
    ('javascript', 'JavaScript'),
)


class Post(models.Model):
    major = (
        ("major", "Computer Science"),
        
    )
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    major = models.CharField(max_length=100, choices=major)
    grad_year = models.IntegerField()
    class_standing = models.CharField(max_length=100, choices=standing)
    comments = models.TextField()
    languages = models.CharField(max_length=100)


def __str__(self):
    return self.title 

def get_absolute_url(self):
    return reverse('base', args=[str(self.id)])
