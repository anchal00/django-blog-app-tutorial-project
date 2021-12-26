from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField('date published')
    body = models.CharField(max_length = 500)

    def __repr__(self):
        return 'Post : [ '+ self.title +' , '+str(self.created_at) + ' , ' + self.body + ' ]'