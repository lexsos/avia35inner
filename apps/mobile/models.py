from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


MONTH_CHOICES = (
    (1, _('january')),
    (2, _('february')),
    (3, _('march')),
    (4, _('april')),
    (5, _('may')),
    (6, _('june')),
    (7, _('july')),
    (8, _('august')),
    (9, _('september')),
    (10, _('october')),
    (11, _('november')),
    (12, _('december')),
)


class Phone(models.Model):

    phone_number = models.CharField(
        verbose_name=_('phone number'),
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
    )

    def __unicode__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = _('phones items')
        verbose_name = _('phone item')
        ordering = ['phone_number',]


class MonthlyLimit(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
    )
    limit_sum = models.FloatField(
        verbose_name=_('limit sum'),
        null=True,
        blank=True,
    )
    phone = models.ForeignKey(
        Phone,
        verbose_name=_('phone'),
    )
    deleted_at = models.DateTimeField(
        verbose_name=_('deleted at'),
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return u'{0}:{1}:{2}'.format(self.user, self.phone, self.limit_sum)

    class Meta:
        verbose_name_plural = _('monthly limits items')
        verbose_name = _('monthly limit item')
        ordering = ['user', 'phone']
        unique_together = ('user', 'phone', 'deleted_at')


class Month(models.Model):

    consumption_file = models.FileField(
        upload_to='mobile',
        verbose_name=_('consumption file'),
    )
    month_number = models.PositiveIntegerField(
        verbose_name=_('month number'),
        choices=MONTH_CHOICES,
    )
    year_number = models.PositiveIntegerField(
        verbose_name=_('year number'),
    )

    def __unicode__(self):
        return u'{0} {1}'.format(
            self.year_number,
            MONTH_CHOICES[self.month_number-1][1],
        )

    @models.permalink
    def get_absolute_url(self):
        return ('mobile_month_enquiry', [str(self.id)])

    def save(self, *args, **kwargs):
        super(Month, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _('monthes items')
        verbose_name = _('month item')
        ordering = ['year_number', 'month_number']
        unique_together = ('year_number', 'month_number')


class Consumption(models.Model):

    month = models.ForeignKey(
        Month,
        verbose_name=_('month item'),
    )
    monthly_limit = models.ForeignKey(
        MonthlyLimit,
        verbose_name=_('monthly limit item'),
    )
    consumption_sum = models.FloatField(
        verbose_name=_('consumption sum'),
    )

    def get_overrun(self):
        if self.monthly_limit.limit_sum is None:
            return 0
        delta = self.monthly_limit.limit_sum - self.consumption_sum
        if delta > 0:
            return 0
        return -delta

    def __unicode__(self):
        return u'{0}-{1}-{2}'.format(
            unicode(self.month),
            unicode(self.monthly_limit),
            self.consumption_sum,
        )

    class Meta:
        verbose_name_plural = _('consumptions items')
        verbose_name = _('consumption item')
        ordering = ['month', 'monthly_limit']
        unique_together = ('month', 'monthly_limit')



