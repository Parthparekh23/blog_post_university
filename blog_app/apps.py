# Import the AppConfig class from django.apps
from django.apps import AppConfig

# Define the BlogAppConfig class which inherits from AppConfig
class BlogAppConfig(AppConfig):
    """
    BlogAppConfig is the configuration class for the 'blog_app' application.
    It specifies the default primary key field type and the name of the app.
    """

    # Set the default primary key field type to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define the name of the application
    name = 'blog_app'
