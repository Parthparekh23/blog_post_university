# Import the models module from Django
from django.db import models

# Define the BlogPost model class
class BlogPost(models.Model):
    """
    BlogPost model represents a single blog post entry in the database.
    Each blog post has a title, content, and a timestamp for when it was created.
    """

    # Title of the blog post, with a maximum length of 100 characters
    title = models.CharField(max_length=100)
    
    # Content of the blog post, with no specific length limit
    content = models.TextField()
    
    # Timestamp for when the blog post was created, automatically set to the current date and time when the post is created
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the BlogPost model
    def __str__(self):
        return self.title
