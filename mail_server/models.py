from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(max_length=150, verbose_name='почта', unique=True)
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    second_name = models.CharField(max_length=100, verbose_name='отчетство')
    comments = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f"{self.name} {self.surname} {self.second_name} ({self.email})"

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email',)


class Letter(models.Model):
    title_message = models.CharField(max_length=150, verbose_name='тема письма')
    body_message = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.title_message

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Distribution(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTH = "Раз в месяц"

    PERIOD_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTH, "Раз в месяц"),
    ]

    FINAL = "Завершена"
    CREATE = "Создана"
    PUSH = "Запушена"

    STATUS_CHOICES = [
        (FINAL, "Завершена"),
        (CREATE, "Создана"),
        (PUSH, "Запушена"),

    ]

    start_time = models.DateTimeField(auto_now_add=True, verbose_name='начало рассылки')
    period = models.CharField(max_length=50, verbose_name='периодичность', choices=PERIOD_CHOICES)
    status = models.CharField(max_length=50, verbose_name='статус рассылки',choices=STATUS_CHOICES, default=CREATE)
    message = models.OneToOneField('Letter', on_delete=models.CASCADE, verbose_name='письмо клиенту', related_name='distribution')
    clients = models.ManyToManyField('Client', related_name='distributions')

    def __str__(self):
        return f'время: {self.start_time}, period:{self.period}, status:{self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class TryLetter(models.Model):
    SUCCESS = 'успешно'
    UNSUCCESSFUL = 'не успешно'

    TRY_STATUS = [
        (SUCCESS, 'успешно'),
        (UNSUCCESSFUL, 'не успешно')
    ]

    distribution = models.ForeignKey('Distribution', on_delete=models.CASCADE, verbose_name='рассылка', related_name='try_letters')
    try_start_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней  попытки')
    try_status = models.CharField(max_length=50, verbose_name='статус попытки', choices=TRY_STATUS)
    mail_answer = models.TextField(verbose_name='ответ сервера')

    def __str__(self):
        return f'{self.distribution} - {self.try_status} at {self.try_start_time}'

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
        ordering = ('-try_start_time',)