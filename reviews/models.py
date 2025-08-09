from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
# class Review(models.Model):
#     full_name = models.CharField(
#         max_length=100,)
#     email = models.EmailField()
#     rating = models.IntegerField()
#     message = models.TextField(
#         max_length=500,)

#     def __str__(self):
#         return f"{self.full_name} ({self.rating}/5)"


class Review(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={
            "required": _("Your name must not be empty!"),
            "max_length": _("Please enter a shorter name!"),
            "min_length": _("Please enter a valid name"),
        }
    )
    email = models.EmailField(
        error_messages={
            "required": _("Email is required"),
            "invalid": _("Enter a valid email address"),
        }
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        error_messages={
            "required": _("Rating is required"),
            "min_value": _("Please rate correctly (1 to 5)!"),
            "max_value": _("Please rate correctly (1 to 5)!"),
        }
    )
    message = models.TextField(
        max_length=500,
        validators=[MinLengthValidator(3)],
        error_messages={
            "required": _("Feedback message must not be empty!"),
            "max_length": _("Please give a short feedback message!"),
            "min_length": _("Please give valid feedback message"),
        }
    )

    def __str__(self):
        return f"{self.full_name} ({self.rating}/5)"