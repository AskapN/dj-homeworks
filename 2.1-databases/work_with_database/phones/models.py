from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return (f'{self.id},'
                f'{self.name},'
                f'{self.price},'
                f'{self.image},'
                f'{self.release_date},'
                f'{self.lte_exists}'
                f'{self.slug}')

