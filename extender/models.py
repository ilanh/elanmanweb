from .utils import unique_slug_generator
import yaml
from django.conf import settings
from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

User = settings.AUTH_USER_MODEL


class RoleObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class RoleObjectManager(models.Manager):
    def get_queryset(self):
        return RoleObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RoleObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    exid = models.CharField(max_length=8, null=True)
    desc = models.CharField(max_length=64, null=True)
    addon = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = RoleObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getrole', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editrole', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.shortname


class LogicalGroupObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class LogicalGroupObjectManager(models.Manager):
    def get_queryset(self):
        return LogicalGroupObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class LogicalGroupObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    exid = models.CharField(max_length=8, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = LogicalGroupObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getlogical', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editlogical', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.shortname


def ro_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def lgo_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(ro_pre_save_receiver, sender=RoleObject)
pre_save.connect(lgo_pre_save_receiver, sender=LogicalGroupObject)
