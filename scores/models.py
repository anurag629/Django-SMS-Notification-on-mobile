from django.db import models
from twilio.rest import Client

# Create your models here.


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'ACbf1f7d728696d08a18ba347b8abf5906'
            auth_token = '5c08aabd9cf5f3c75e1d26095ee433bc'
            client = Client(account_sid, auth_token)

            message = client.message.create(
                body=f'The current result is bad - {self.result}',
                from_='+19036622331',
                to='+918052027789'
            )
            print(message.sid)
        return super().save(*args, **kwargs)
