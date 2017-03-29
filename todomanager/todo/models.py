from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


def validate_image(fieldfile_obj):
    if fieldfile_obj:
        filesize = fieldfile_obj.file.size
        megabyte_limit = int(15)
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max : %s Mo" % str(megabyte_limit))


def avatar_filename(instance, filename):
    fname, dot, extension = filename.rpartition('.')
    slug = instance.slug
    path = 'gallery/'
    return '%s%s.%s' % (path, slug, extension)

class Member(models.Model):
    user = models.OneToOneField(
        User,
        related_name="member"
    )
    avatar = models.ImageField(
        verbose_name="Avatar membre",
        upload_to=avatar_filename,
        validators=[validate_image],
        null=True,
        blank=True
    )
    settings = models.ForeignKey(
        'Setting',
        null=True,
        blank=True,
        verbose_name="Paramêtres"
    )


    class Meta:
        app_label = "todo"
        ordering = ['user__date_joined']

    def __str__(self):
        return str(self.user.username)


class Parano(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Créé le"
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Modifié le"
    )
    created_by = models.ForeignKey(
        'Member',
        verbose_name="Créé par",
        related_name="%(app_label)s_%(class)s_creator"
    )
    modified_by = models.ForeignKey(
        'Member',
        verbose_name="Modifié par",
        related_name="%(app_label)s_%(class)s_modificator")

    class Meta:
        abstract = True
        app_label = "todo"



class Setting(Parano, models.Model):
    notify_mail = models.BooleanField(
        verbose_name="Notification par Email ? ",
        default=True,
        blank=True
    )
    notify_sms = models.BooleanField(
        verbose_name="Notification par SMS ? ",
        default=True,
        blank=True
    )

    class Meta:
        app_label = "todo"


class Relation(models.Model):
    choices_types = (
        ('developper', 'Développeur'),
        ('guest', 'Invité'),
        ('manager', 'Manager'),
    )

    created_at = models.DateTimeField(
        verbose_name="Créé le",
        auto_now_add=True
    )

    type = models.CharField(
        max_length=15,
        verbose_name="Type de relation ",
        default="guest",
        choices=choices_types
    )

    member = models.ForeignKey(
        "Member",
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        "Group",
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = "todo"

    def __str__(self):
        return str(self.type)


class Group(Parano, models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name="Nom du groupe"
    )

    avatar = models.ImageField(
        verbose_name="Avatar Groupe",
        upload_to=avatar_filename,
        validators=[validate_image],
        null=True,
        blank=True
    )
    settings = models.ForeignKey(
        Setting,
        verbose_name="Paramêtres"
    )
    members = models.ManyToManyField(
        Member,
        verbose_name="Membre du groupe",
        related_name="groups",
        through=Relation,
        symmetrical=False
    )

    class Meta:
        app_label = "todo"

    def __str__(self):
        return str(self.name)

    # def get_absolute_url(self):
    #     return reverse_lazy('todo:groups:retrieve', kwargs={'pk': self.id})

class Task(Parano, models.Model):
    status_choices = (
        (None, '---'),
    )
    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )
    # assigned_to = models.ForeignKey(
    #     Member,
    #     verbose_name="Assigné à",
    #     related_name="tasks_assigned",
    #     null=True,
    #     blank=True
    # )
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )
    due_date = models.DateTimeField(
        verbose_name="Fin prévue le",
        null=True,
        blank=True,
        default=timezone.now() + timedelta(1)
    )
    completed = models.BooleanField(
        verbose_name="Tache terminée ? ",
        default=False,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=None,
        null=True,
        blank=True
    )
    # list = models.ForeignKey(
    #     Group,
    #     verbose_name="Liste",
    #     related_name="tasks"
    # )

    class Meta:
        app_label = "todo"
        # ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    # def get_absolute_url(self):
    #     return reverse_lazy('todo:tasks:retrieve', kwargs={'pk': self.id})
