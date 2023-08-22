from django.db import models

# Create your models here.

class Liabrary(models.Model):
    section=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.section
    
class Books(models.Model):
    section=models.ForeignKey(Liabrary, on_delete=models.CASCADE)
    Bname=models.CharField(max_length=100, primary_key=True)
    auther=models.CharField(max_length=100)

    def __str__(self):
        return self.Bname
    
class reader(models.Model):
    Rid=models.IntegerField(primary_key=True)
    Rname=models.CharField(max_length=100)
    Email=models.EmailField()

    def __str__(self):
        return self.Rname
    
class reading(models.Model):
    Rid=models.ForeignKey(reader, on_delete=models.CASCADE)
    Bname=models.ForeignKey(Books, on_delete=models.CASCADE)
    Tdate=models.DateField()
    Sdate=models.DateField()
