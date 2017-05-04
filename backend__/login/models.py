from django.db import models
from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django_countries.fields import CountryField

from .utils import (
    send_template_mail, default_token_generator, to_dict
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        # python-social-auth compatibility
        if 'username' in extra_fields:
            del extra_fields['username']

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True, blank=False)
    full_name = models.CharField(_('name'), max_length=64, blank=False)

    is_verified = models.BooleanField(_('verified'), default=False)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=now)

    country = CountryField()

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.full_name.partition(' ')[0]

    def get_full_name(self):
        return self.full_name

    def send_verification_mail(self, request):
        if not self.pk:
            self.save()

        return send_template_mail(
            'Verificação de email',
            'users/user_verification_email.html',
            {
                'user': self,
                'verification_url': request.build_absolute_uri(
                    reverse('users:user_verify', kwargs={
                        'uidb64': urlsafe_base64_encode(force_bytes(self.pk)),
                        'token': default_token_generator.make_token(self)
                    })
                )
            },
            [self.email]
        )


class Relationship(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="relationship_user_teacher"
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="relationship_user_student"
    )
    learn = models.CharField(max_length=128)
    teach = models.CharField(max_length=128)
    date_created = models.DateField(_('date joined'), default=now)

    def __str__(self):
        t = self.teacher.get_short_name()
        s = self.student.get_short_name()
        return '{} - {}'.format(t, s)

    def serialize(self):
        return {
            'teacher': self.teacher.full_name,
            'student': self.student.full_name,
            'learn': self.learn,
            'teach': self.teach,
            'date_created': self.date_created.strftime("%B %d, %Y")
        }


class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Interest(models.Model):
    OPTIONS = (
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    LEVELS = (
        (0, 'Basic'),
        (1, 'Intermediate'),
        (2, 'Advanced')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='interests'
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    iam = models.CharField(max_length=1, choices=OPTIONS)
    level = models.IntegerField(choices=LEVELS)

    def __str__(self):
        return '{} - {}'.format(self.user.get_short_name(), self.subject)

    def serialize(self):
        return {
            'user': self.user.full_name,
            'subject': self.subject.name,
            'iam': self.iam,
            'level': self.level
        }


class Message(models.Model):

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages_sender'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages_receiver'
    )

    subject = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
