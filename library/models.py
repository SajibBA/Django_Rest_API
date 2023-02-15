from django.db import models

# Create your models here.



class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    books = models.ManyToManyField(Book, through='Checkout')


class Checkout(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()