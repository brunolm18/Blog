from django.contrib import admin
from blog.models import Post,Autor,Categoria

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    actions_on_top = True
    list_display = ("category","autor","title","date","text",)
    ordering = ['date']
    list_per_page = 10
   

class AutorAdmin(admin.ModelAdmin):
    list_filter = ("full_name","email",)
    ordering = ("full_name",)
    list_per_page = 10
    
   

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("category",)
    list_per_page = 10


admin.site.register(Autor,AutorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)
    