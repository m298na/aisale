from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class Deal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    description = models.TextField(verbose_name='Описание')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    status = models.CharField(max_length=20, choices=[
        ('Новая', 'Новая'),
        ('В процессе', 'В процессе'),
        ('Закрыта', 'Закрыта'),
        ('Отменена', 'Отменена'),
    ], default='Новая', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"Сделка с {self.client.name}: {self.description}"


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    assigned_to = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, verbose_name='Назначена')
    due_date = models.DateField(verbose_name='Срок выполнения')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title


class Call(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    start_time = models.DateTimeField(verbose_name='Дата и время начала звонка')
    end_time = models.DateTimeField(verbose_name='Дата и время окончания звонка')
    transcription = models.TextField(blank=True, null=True, verbose_name='Транскрипция разговора')
    ai_analysis_results = models.TextField(blank=True, null=True, verbose_name='Результаты анализа ИИ')

    def __str__(self):
        return f"Звонок с {self.client.name} ({self.start_time})"


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    sent_time = models.DateTimeField(verbose_name='Дата и время отправки')
    content = models.TextField(verbose_name='Содержание сообщения')
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ответ на сообщение')
    ai_analysis_results = models.TextField(blank=True, null=True, verbose_name='Результаты анализа ИИ')

    def __str__(self):
        return f"Сообщение клиенту {self.client.name} ({self.sent_time})"


class Employee(AbstractUser):
    position = models.CharField(max_length=100, verbose_name='Должность')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон', blank=True, null=True)
    hire_date = models.DateField(verbose_name='Дата принятия на работу', blank=True, null=True)

    def __str__(self):
        return self.username
