from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(null=True,blank=True)
def __str__(self):
    return self.title




#1-1 relationships
#1 user can have only 1 prof =>1
#1 profile is associated to only 1 user
# OneToOneField()= any models
#
## 1-M relationship
# 1 user can add m post =>MemoryError1 post is associated to only 1 user => 1
# In django use foreign key() => use in many side models
#
## M-M relationship
# 1 student can learn from M teachers =M
# 1 teacher can teach M students
# ManyToManyField() =>Any place



