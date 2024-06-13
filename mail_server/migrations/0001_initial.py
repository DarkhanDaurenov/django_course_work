# Generated by Django 5.0.6 on 2024-06-05 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='почта')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('surname', models.CharField(max_length=100, verbose_name='фамилия')),
                ('second_name', models.CharField(max_length=100, verbose_name='отчетство')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('email',),
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_message', models.CharField(max_length=150, verbose_name='тема письма')),
                ('body_message', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='начало рассылки')),
                ('period', models.CharField(choices=[('Раз в день', 'Раз в день'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], max_length=50, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('Завершена', 'Завершена'), ('Создана', 'Создана'), ('Запушена', 'Запушена')], default='Создана', max_length=50, verbose_name='статус рассылки')),
                ('clients', models.ManyToManyField(related_name='distributions', to='mail_server.client')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='distribution', to='mail_server.letter', verbose_name='письмо клиенту')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='TryLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('try_start_time', models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней  попытки')),
                ('try_status', models.CharField(choices=[('успешно', 'успешно'), ('не успешно', 'не успешно')], max_length=50, verbose_name='статус попытки')),
                ('mail_answer', models.TextField(verbose_name='ответ сервера')),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='try_letters', to='mail_server.distribution', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'попытка рассылки',
                'verbose_name_plural': 'попытки рассылки',
                'ordering': ('-try_start_time',),
            },
        ),
    ]
