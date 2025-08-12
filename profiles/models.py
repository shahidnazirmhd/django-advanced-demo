from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.core.exceptions import ValidationError

def file_size(value):
    max_size_mb = 2
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(_("File size should not exceed 2 MB."))



class UserProfile(models.Model):
    profile = models.ImageField(
        upload_to="images",
        max_length=100,
        validators=[file_size],
        error_messages={
            "required": _("File attachment required"),
            "max_length": _("File name must be shorter!"),
        }
    )

    def __str__(self):
        return self.profile.name if self.profile else "No profile file"
