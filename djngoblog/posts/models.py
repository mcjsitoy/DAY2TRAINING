from django.db import models
from users.models import CustomUser




class Articles(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    content=models.TextField()
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    # def get_title(self):
    #     return self.title
    # def description(self):
    #     return self.description
    # def content(self):
    #     return self.content
    # def owner(self):
    #     return self.owner

    # comments=models.CharField(max_length=250)
    # likes=
    # date_created=models.DateTimeField(auto_now_add=True)
    # date_updated=models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.title



class ArticleComment(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment=models.CharField(max_length=250)
    article=models.ForeignKey(Articles, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)


    

class ArticleLikes(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article=models.ForeignKey(Articles, on_delete=models.CASCADE)
    is_liked=models.BooleanField(default=False)



    
    
    
      

            
    
    
    


    


    
    
    



    


    


    
