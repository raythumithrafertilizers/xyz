from django.db import models
from django.contrib.auth.models import User
from BaseModule.settings import SECRET_KEY
import binascii
from datetime import datetime, timedelta
import jwt
from Admin.models import *


class Token(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    token_type = models.IntegerField(default=1) #1 for login token & 2 for forgot password &3 for activation
    id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.create_token(self.user.id)
            print self.token
        return super(Token, self).save(*args, **kwargs)

    def create_token(self, userid):
        payload = {
            'sub': str(userid),
            'iat': datetime.now(),
            'exp': datetime.now() + timedelta(days=20)
        }
        token = jwt.encode(payload, SECRET_KEY)
        return token.decode('unicode_escape')

    def __unicode__(self):
        return self.token


class UserDetails(models.Model):
    userKey = models.ForeignKey(User)
    phone = models.CharField(max_length=25)
    activationCode = models.CharField(max_length=50)
    role = models.CharField(max_length=15)





