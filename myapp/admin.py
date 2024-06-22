from django.contrib import admin
from myapp.models import wear, Size, textile


class myProd(admin.ModelAdmin):
    list_display = ["name", "cost", "description", "size", "count", "dod"]


admin.site.register(wear, myProd)
admin.site.register(Size)
admin.site.register(textile)

# Register your models here.
