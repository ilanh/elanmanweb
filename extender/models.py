from .utils import unique_slug_generator
# import yaml
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

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
    exid = models.CharField(max_length=16, null=True)
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
        return self.exid


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
    exid = models.CharField(max_length=16, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = LogicalGroupObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getlogicalgroup', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editlogicalgroup', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid
    

class ConfigSectionObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class ConfigSectionObjectManager(models.Manager):
    def get_queryset(self):
        return ConfigSectionObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ConfigSectionObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    exid = models.CharField(max_length=16, null=True)
    desc = models.CharField(max_length=64, null=True)
    listobject = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = ConfigSectionObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getconfigsection', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editconfigsection', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid


class RoleTaskObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class RoleTaskObjectManager(models.Manager):
    def get_queryset(self):
        return RoleTaskObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RoleTaskObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    desc = models.CharField(max_length=64, null=True)
    role = models.ForeignKey(RoleObject, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = RoleTaskObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getroletask', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editroletask', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.shortname + '-' + self.role.exid
    

class ApiObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class ApiObjectManager(models.Manager):
    def get_queryset(self):
        return ApiObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ApiObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    desc = models.CharField(max_length=64, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = ApiObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getapi', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editapi', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.shortname
    
    
class ApiSectionObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class ApiSectionObjectManager(models.Manager):
    def get_queryset(self):
        return ApiSectionObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ApiSectionObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    exid = models.CharField(max_length=16, null=True)
    desc = models.CharField(max_length=64, null=True)
    api = models.ForeignKey(ApiObject, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = ApiSectionObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getapisection', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editapisection', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid


class RoleTemplateObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class RoleTemplateObjectManager(models.Manager):
    def get_queryset(self):
        return RoleTemplateObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RoleTemplateObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    slug = models.SlugField(null=True, blank=True)
    desc = models.CharField(max_length=64, null=True)
    istemplate = models.BooleanField(default=False)
    role = models.ForeignKey(RoleObject, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = RoleTemplateObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getroletemplate', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editroletemplate', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.shortname + '-' + self.role.exid


class ConfigSubObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class ConfigSubObjectManager(models.Manager):
    def get_queryset(self):
        return ConfigSubObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ConfigSubObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    exid = models.CharField(max_length=16, null=True)
    desc = models.CharField(max_length=64, null=True)
    section = models.ForeignKey(ConfigSectionObject, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = ConfigSubObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getconfigsub', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editconfigsub', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid


class ApiSubObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(shortname__icontains=query) |
                Q(shortname__iexact=query)
            ).distinct()
        return self


class ApiSubObjectManager(models.Manager):
    def get_queryset(self):
        return ApiSubObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ApiSubObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=32)
    exid = models.CharField(max_length=16, null=True)
    desc = models.CharField(max_length=64, null=True)
    section = models.ForeignKey(ApiSectionObject, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.shortname

    objects = ApiSubObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getapisub', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editapisub', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid


class ConfigValueObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(exid__icontains=query) |
                Q(exid__iexact=query)
            ).distinct()
        return self


class ConfigValueObjectManager(models.Manager):
    def get_queryset(self):
        return ConfigValueObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ConfigValueObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exid = models.CharField(max_length=16, null=True)
    subobject = models.ForeignKey(ConfigSubObject, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=256, null=True)
    desc = models.CharField(max_length=64, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.exid

    objects = ConfigValueObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getconfigvalue', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editconfigvalue', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid


class ApiValueObjectQuerySet(models.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(exid__icontains=query) |
                Q(exid__iexact=query)
            ).distinct()
        return self


class ApiValueObjectManager(models.Manager):
    def get_queryset(self):
        return ApiValueObjectQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class ApiValueObject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exid = models.CharField(max_length=16, null=True)
    subobject = models.ForeignKey(ApiSubObject, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=256, null=True)
    desc = models.CharField(max_length=64, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.exid

    objects = ApiValueObjectManager()

    def get_absolute_url(self):
        return reverse('extend:getapivalue', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('extend:editapivalue', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.exid


def ro_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def lgo_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def cs_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def rt_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def ao_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def as_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def rtm_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def co_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def aps_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def cv_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def av_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(ro_pre_save_receiver, sender=RoleObject)
pre_save.connect(lgo_pre_save_receiver, sender=LogicalGroupObject)
pre_save.connect(cs_pre_save_receiver, sender=ConfigSectionObject)
pre_save.connect(rt_pre_save_receiver, sender=RoleTaskObject)
pre_save.connect(ao_pre_save_receiver, sender=ApiObject)
pre_save.connect(as_pre_save_receiver, sender=ApiSectionObject)
pre_save.connect(rtm_pre_save_receiver, sender=RoleTemplateObject)
pre_save.connect(co_pre_save_receiver, sender=ConfigSubObject)
pre_save.connect(aps_pre_save_receiver, sender=ApiSubObject)
pre_save.connect(cv_pre_save_receiver, sender=ConfigValueObject)
pre_save.connect(av_pre_save_receiver, sender=ApiValueObject)
