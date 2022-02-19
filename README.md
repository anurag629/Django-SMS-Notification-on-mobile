# Django-SMS-Notification-on-mobile

## 1. Create 'smsproj' project :
    django-admin startproject smsproj

## 2. create virtual environment and activate it :
    virtualenv env
    source env/bin/activate

## 3. install following inside environment :
    pip install django
    pip install twilio

## 4. create app 'scores' and add to settings .py file :
    python manage.py startapp scores

* add scores app to settings.py file :

        INSTALLED_APPS = [
            'scores',
        ]

## 5. Create models in scores app :
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
                    to='your personal number'
                )
                print(message.sid)
            return super().save(*args, **kwargs)
    
## 6. run miratetions and migrate and create super user :
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser



# Thank you ! All Completed.