import json
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.db.models.fields.related import ManyToManyField
from django.db.models.fields import DateTimeField
from django_countries.fields import CountryField
from django.core import serializers


def send_template_mail(subject, template, context, to, fail_silently=False):
    email = EmailMultiAlternatives(subject=subject, to=to)
    c = Context(context)

    if 'txt' in template:
        email.body = render_to_string(template, c)

    if 'html' in template:
        html = render_to_string(template, c)
        email.attach_alternative(html, 'text/html')

    return email.send(fail_silently=fail_silently)


def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(
                    f.value_from_object(instance).values_list('pk', flat=True)
                )
        elif isinstance(f, DateTimeField):
            data[f.name] = f.value_from_object(instance).strftime("%B %d, %Y")
        elif isinstance(f, CountryField):
            data[f.name] = f.value_from_object(instance).name
        else:
            data[f.name] = f.value_from_object(instance)
    return data


def serialize_to_json(querySet):
    try:
        querySet = [qs.serialize() for qs in querySet]
        return json.dumps(querySet)
    except AttributeError:
        pass
    return serializers.serialize('json', querySet)
