from django.contrib import admin
from app1.models.user import Signup ,Songs


class SignupAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "password1",
        "password2",
    ]


admin.site.register(Signup, SignupAdmin)
admin.site.register(Songs)

# Register your models here.
