from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Task(models.Model):
    # Drop-down menu in English and French.
    PRIORITY_CHOICES = (
        ('Low', 'Basse'),
        ('Medium', 'Moyenne'),
        ('High', 'Haute'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        return self.due_date and self.due_date < timezone.now().date() and not self.completed
