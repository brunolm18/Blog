from django.db import models


#Autor
class Autor(models.Model):
    full_name = models.CharField(max_length=200,verbose_name="Autor",blank=False,)
    email = models.EmailField(max_length=100,unique=True)
    biografia = models.TextField(verbose_name="Biografia") 

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        db_table = "Autores"

#Categoria
class Categoria(models.Model): 
    category = models.CharField(max_length=50,verbose_name="Categorias")

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        db_table = "Categorias"
        

    def __str__(self):
        return self.category

#Posts
class Post(models.Model):
    category = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="Title")
    image = models.ImageField(upload_to="blog_images",verbose_name="Image",blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['date']
        db_table = "Posts"
        
