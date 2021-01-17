from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 1'den fazla ForeignKey değerimiz olduğu zaman hata alırız.
# ForeignKey default olarak modelname_set olarak gelir
# 2 tane ForeignKey değerimiz olduğu için birtanesine related_name değeri vermeliyiz.
# Add or change a related_name argument to the definition for 'Student.department' or 'Student.subject'
class Student(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='student_department')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
