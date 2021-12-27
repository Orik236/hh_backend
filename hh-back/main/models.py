from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Компании")
    description = models.TextField(verbose_name="Описание")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.TextField(verbose_name="Адресс компании")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.name} - {self.description}'


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Вакансии")
    description = models.TextField(verbose_name="Описание")
    salary = models.IntegerField(default=0, null=True, verbose_name="Зарплата")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }

    def __str__(self):
        return f'Vacancy: {self.name}'
