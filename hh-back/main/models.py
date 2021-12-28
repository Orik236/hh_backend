from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Компании")
    description = models.TextField(verbose_name="Описание")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.TextField(verbose_name="Адресс компании")

    def __str__(self):
        return f'{self.name} - {self.description}'


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Вакансии")
    description = models.TextField(verbose_name="Описание")
    salary = models.IntegerField(default=0, null=True, verbose_name="Зарплата")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'Vacancy: {self.name}'


class Resumes(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя сотрудника")
    job_title = models.CharField(max_length=200, verbose_name="Специальность")
    city = models.CharField(max_length=100, verbose_name="Город проживания")
    expected_salary = models.IntegerField(default=0, null=True, verbose_name="Ожидаемая зарплата")
    job_experience = models.IntegerField(default=0, verbose_name="Опыт работы в годах")
    study_degree = models.CharField(max_length=200, null=True, verbose_name="Образование")
    description = models.TextField(null=True, verbose_name="Описание себя")
    email = models.CharField(max_length=200, verbose_name='Email', null=True)

    def __str__(self):
        return f"Имя: {self.name}, Специальность: {self.job_title}"
