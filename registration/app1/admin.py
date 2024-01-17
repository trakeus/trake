from django.contrib import admin
from .models import UserProfile, Number
from .forms import BalanceUpdateForm

admin.site.register(UserProfile)
admin.site.register(Number)

