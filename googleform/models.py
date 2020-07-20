from django.db import models

class CVModel(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(blank=True)
    file1=models.FileField(upload_to='uploads/')
    file2=models.FileField(blank=True,upload_to='uploads/')


    def __str__(self):
        return self.firstname
