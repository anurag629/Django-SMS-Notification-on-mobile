from django.db import models
from twilio.rest import Client
# Create your models here.


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'twillio sid id'
            auth_token = 'twilio sid auth token'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'The current result is bad - {self.result}',
                from_='your twllio number',
                to='+918052027789'
            )
            print(message.sid)
        return super().save(*args, **kwargs)
