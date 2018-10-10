from django.contrib import admin
from .models import *
from .views import *

# from notifications.views import emailform
#from notifications.models import notification
#from notifications.models import notificationAdmin
# from notifications.forms import sendEmailForm

class SubscriberAdmin(admin.ModelAdmin):
    email.short_description = "Отправить уведомление по Email"
    whatsapp.short_description = "Отправить уведомление Whatsapp"
    actions=[email, whatsapp]

    #list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]

    #exclude = ["id"]
    #fields = []
    list_filter = ["name"]
    search_fields = [field.name for field in Subscriber._meta.fields]

    class Meta:
        model = Subscriber

# class createNotificationAdmin(admin.ModelAdmin):
#     form = sendEmailForm

admin.site.register(Subscriber, SubscriberAdmin)
# admin.site.register(sendEmailForm, createNotificationAdmin)

#admin.site.register(notification, notificationAdmin)
#admin.site.disable_action('delete_selected')

#admin.site.register(Subscriber.emailNotification)
#admin.site.register(emailNotification)