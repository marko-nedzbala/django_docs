from django.db import models

class Person(models.Model):
    first_name = models.CharField('person first name', max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshamn'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)

    MyType = models.TextChoices('MyType', 'Type01 Type02 Type03')
    my_type = models.CharField(blank=True, choices=MyType, max_length=8)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['first_name']

    def baby_boomer_status(self):
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return 'Pre-boomer'
        elif self.birth_date < datetime.date(1965, 1, 1):
            return 'Baby boomer'
        else:
            return 'Post-boomer'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name
    
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['person', 'group'],
                name='unique_person_group'
            )
        ]

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Manufacturer(models.Model):
    man_name = models.CharField('manugacturer name', max_length=100)

    def __str__(self):
        return self.man_name

class Car(models.Model):
    man_ref = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
