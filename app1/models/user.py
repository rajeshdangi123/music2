from django.db import models


class Signup(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    password1 = models.CharField(max_length=50, blank=True, null=True)
    password2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def register(self):
        self.save()

    def isExists(self):
        if Signup.objects.filter(email=self.email):
            return True
        else:
            return False

    # def get_customer_by_email(email):
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Signup.objects.get(email=email)
        except:
            return False


# class login(models.Model):

class Songs(models.Model):
    song=models.FileField(upload_to="audio/songs/" ,blank=True,null=True)
    
    def __str__(self) -> str:
        return str(self.song)