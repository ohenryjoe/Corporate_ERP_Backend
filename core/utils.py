import re
from datetime import datetime

from functools import reduce
from operator import concat

from django.template.defaultfilters import slugify
from django.utils import timezone
from dateutil.relativedelta import relativedelta

"""
Taken from SmileyChris' post @ https://djangosnippets.org/snippets/690/
"""


def unique_slugify(
        instance, value, slug_field_name="slug", queryset=None, slug_separator="-"
):  # sourcery skip: avoid-builtin-shadow
    """
    Calculates a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug. Chop its length down if we need to.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create a queryset, excluding the current instance.
    if not queryset:
        queryset = instance.__class__._default_manager.all()
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = f"-{next}"
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[: slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = f"{slug}{end}"
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator=None):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    if separator == "-" or not separator:
        re_sep = "-"
    else:
        re_sep = f"(?:-|{re.escape(separator)})"
        value = re.sub(f"{re_sep}+", separator, value)
    return re.sub(f"^{re_sep}+|{re_sep}+$", "", value)


def nested_getattr(
        instance: object, attributes: str, separator=".", default=None, call=True
):
    """
    Returns nested getattr and returns default if not found
    :param instance: object to get nested attributes from
    :param attributes: separator separated attributes
    :param separator: separator between nested attributes.
    :param default: default value to return if attribute was not found
    :param call: flag that determines whether to call or not if callable
    :return:
    """
    nested_attrs = attributes.split(separator)
    nested_attrs.insert(0, instance)
    try:
        attr = reduce(
            lambda instance_, attribute_: getattr(instance_, attribute_), nested_attrs
        )
        if call and callable(attr):
            return attr()
        return attr
    except AttributeError:
        return default


def get_date_after_days(days):
    """
    :param days: Days to be subtracted from today's date. (Defaults to 30)
    """
    return timezone.now() + timezone.timedelta(days=days)


def get_date_after_days_from_date(start_date, days):
    """
    :param days: Days to be subtracted from today's date. (Defaults to 30)
    """
    return start_date + timezone.timedelta(days=days)


def get_date_after_months_from_date(start_date, months):
    """
    :param days: Days to be subtracted from today's date. (Defaults to 30)
    """


def period_prop(start_date):
    # start_date = datetime.strptime(start_date, '%d/%m/%Y')
    this_yr = start_date.year
    next_yr = this_yr + 1
    last_year = this_yr - 1
    m = start_date.month
    if 1 <= m <= 6:
        this_half = 2
        this_fy = concat(concat(last_year.__str__(), '-'), this_yr.__str__())
        if 1 <= m <= 3:
            this_quarter = 3
        else:
            this_quarter = 4
    else:
        this_fy = concat(concat(this_yr.__str__(), '-'), next_yr.__str__())
        this_half = 1
        if 7 <= m <= 9:
            this_quarter = 1
        else:
            this_quarter = 2
    return {'h': this_half, 'q': this_quarter, 'fy': this_fy, 'year_part': this_yr}
