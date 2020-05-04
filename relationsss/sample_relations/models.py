from django.db import models

# Create your models here.


class jobs(models.Model):
    job_name = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.job_name}"


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class multi(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    job = models.ForeignKey(
        jobs, on_delete=models.CASCADE, related_name="multis")
    tags = models.ManyToManyField(Tag)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    publicatioon_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
