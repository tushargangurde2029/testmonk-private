from django.contrib import admin
from mainapp.models import Match_Data,Id_Pass,users_match,User_Data,Register_Match
# Register your models here.

admin.site.register(Match_Data)
admin.site.register(Id_Pass)
admin.site.register(users_match) 
admin.site.register(Register_Match) 
admin.site.register(User_Data)