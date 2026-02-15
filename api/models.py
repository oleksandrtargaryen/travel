from django.db import models

# Create your models here.

class Project(models.Model):
    """Travel project model"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Place(models.Model):
    """Place in a travel project"""
    IS_VISITED_CHOICES = [
        ('visited', 'Visited'),
        ('not_visited', 'Not Visited'),
        ('planning', 'Planning to Visit'),
    ]
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='places'
    )
    place_id = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    is_visited = models.CharField(choices=IS_VISITED_CHOICES, max_length=50, default= 'not_visited')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.place_id}"