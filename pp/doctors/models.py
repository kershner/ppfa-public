from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)

    PODIATRIST = 'po'
    CARDIOLOGIST = 'ca'
    DERMATOLOGIST = 'de'
    IMMUNOLOGIST = 'im'
    NEUROLOGIST = 'ne'
    GYNECOLOGIST = 'gy'
    SPECIALIZATION_CHOICES = [
        (PODIATRIST, 'Podiatrist'),
        (CARDIOLOGIST, 'Cardiologist'),
        (DERMATOLOGIST, 'Dermatologist'),
        (IMMUNOLOGIST, 'Immunologist'),
        (NEUROLOGIST, 'Neurologist'),
        (GYNECOLOGIST, 'Gynecologist'),
    ]
    specialization = models.CharField(
        max_length=2,
        choices=SPECIALIZATION_CHOICES,
        default=PODIATRIST,
        null=False
    )

    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ]
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=1,
        null=False
    )

    def __str__(self):
        return '{}'.format(self.name)
