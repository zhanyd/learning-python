from django.db import models

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        '''返回一个表示对象的字符串'''
        return self.text
    

class Entry(models.Model):
    '''用户学习的主题的笔记'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''返回一个表示对象的字符串'''
        if(len(self.text) > 50):
            return f'{self.text[:50]}...'  
        else:
            return self.text
        
          