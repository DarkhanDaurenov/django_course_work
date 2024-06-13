from django.contrib import admin

from mail_server.models import Client, Letter, Distribution, TryLetter


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'second_name', 'email',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('title_message', 'body_message',)
    list_filter = ('title_message',)


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'period', 'status',)
    list_filter = ('start_time',)


@admin.register(TryLetter)
class TryLetterAdmin(admin.ModelAdmin):
    list_display = ('distribution', 'try_start_time', 'try_status', 'mail_answer',)
    list_filter = ('try_status',)




