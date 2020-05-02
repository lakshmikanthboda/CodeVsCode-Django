from django.contrib import admin
from .models import register,questions,post,comment

# Register your models here.
admin.site.register(register)
admin.site.register(questions)
admin.site.register(post)
admin.site.register(comment)