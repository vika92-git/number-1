from django.db import models


class wear(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    cost = models.IntegerField(verbose_name="Цена")
    description = models.CharField(max_length=200, verbose_name="Описание")
    size = models.CharField(max_length=10, verbose_name="Размер")
    count = models.IntegerField(verbose_name="Количество")
    dod = models.DateField(auto_now=True, verbose_name="Дата поступления")
    pic = models.ImageField(upload_to="myapp/static/img", blank=True)
    Size = models.ForeignKey(
        "Size", on_delete=models.CASCADE, blank=True, null=True, default=1)
    textile = models.ForeignKey(
        "textile", on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.name


class Size(models.Model):
    size_number = models.CharField(max_length=10)

    def __str__(self):
        return self.size_number


class textile(models.Model):
    textile_type = models.CharField(max_length=50)
    textile_color = models.CharField(max_length=50)

    def __str__(self):
        return self.textile_type


class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self, a):
        return f"The {self.name} says '{self.sound}'"

# Create your models here.
