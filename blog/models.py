from django.db import models
from django.utils import timezone
from django.contrib.auth.models	import User
from django.urls	import	reverse
class PublishedManager(models.Manager):
        def	get_queryset(self):
                return	super(PublishedManager,self).get_queryset()\
                .filter(status='published')
                                                                                                        



class post(models.Model):
    objects=models.Manager()
    published=PublishedManager()
    STATUS_CHOICE=(
        ('draft','Draft'),('published','Published')
    )
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    img=models.ImageField(upload_to='images/',blank=True) 
    class Meta:
        ordering=('-publish',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_details',args=[self.id])
class comment(models.Model):
        post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
        name=models.CharField(max_length=80)	
        email=models.EmailField()	
        body=models.TextField()	
        created	=models.DateTimeField(auto_now_add=True)	
        updated	=models.DateTimeField(auto_now=True)	
        active	=models.BooleanField(default=True)	
        class	Meta:	
            ordering=('created',)	
        def	__str__(self):	
            return	'Comment	by	{}	on	{}'.format(self.name,	self.post)