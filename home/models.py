from django.db import models

class selectedItems():
    selecteditems = None


class Subscriber(models.Model):
    email = models.EmailField(blank=True, null=True, default=None)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    phone = models.CharField(max_length=48, blank=True, null=True, default=None)

    def __str__(self):
        return '%s (%s) телефон: %s' % (self.email, self.name, self.phone)

class Meta:

    verbose_name = 'Subscriber'
    verbose_name_plural = 'Notification Subscribers'


