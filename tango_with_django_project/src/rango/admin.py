# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Page,UserProfile
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display=["title","category","url",]
    class Meta:
        model=Page
        
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
