from django.db import models


# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=128, unique=True)
    phone = models.CharField(max_length=11)
    fam = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    otc = models.CharField(max_length=128)


class Coords(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    height = models.IntegerField()


class Level(models.Model):
    TYPE_LEVEL = [
        (' ', ' '),
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('4A', '4A'),
    ]
    winter = models.CharField(max_length=2, choices=TYPE_LEVEL, default=" ")
    summer = models.CharField(max_length=2, choices=TYPE_LEVEL, default=" ")
    autumn = models.CharField(max_length=2, choices=TYPE_LEVEL, default=" ")
    spring = models.CharField(max_length=2, choices=TYPE_LEVEL, default=" ")


class Pereval(models.Model):
    STATUS = [
        ('new', 'новый объект'),
        ('pending', 'модерация работает'),
        ('accepted', 'модерация прошла успешно'),
        ('rejected', 'модерация прошла, информация не принята'),
    ]
    status = models.CharField(max_length=25, choices=STATUS, default='new')
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')

class Images(models.Model):
    title = models.CharField(max_length=255)
    data = models.URLField(blank=True)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
