#qna models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

STATUS = (
    (0,"Not Solved"),
    (1,"Solved")
)

class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='question_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate the slug from the title
        self.slug = slugify(self.title)

        super(Question, self).save(*args, **kwargs)

    def can_change_status(self, user):
        return self.author == user
    
    def change_status(self, user, new_status):
        if self.can_change_status(user):
            self.status = new_status
            self.save()
        else:
            raise PermissionDenied("You do not have permission to change the status of this question.")
    
    def upvote(self):
        self.upvotes += 1
        self.save()

    def downvote(self):
        self.downvotes += 1
        self.save()
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-posted_on']
    