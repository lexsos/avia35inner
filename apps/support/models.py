from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Ticket(models.Model):

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
    )
    content = models.TextField(
        verbose_name=_('content'),
    )
    opened = models.BooleanField(
        verbose_name=_('opened'),
        default=True,
    )
    updated_author = models.BooleanField(
        verbose_name=_('updated author'),
        default=True,
    )
    updated_suppoter = models.BooleanField(
        verbose_name=_('updated suppoter'),
        default=False,
    )
    author = models.ForeignKey(
        User,
        verbose_name=_('author'),
    )
    create_date = models.DateTimeField(
        verbose_name=_('create date'),
        auto_now_add = True,
    )

    def is_updated(self, user):
        if (user == self.author) and self.updated_suppoter:
            return True
        if (user != self.author) and self.updated_author:
            return True
        return False

    def on_update(self, user):
        if user == self.author:
            self.updated_author = True
        else:
            self.updated_suppoter = True
        self.save()

    def on_read(self, user):
        if user == self.author:
            self.updated_suppoter = False
        else:
            self.updated_author = False
        self.save()

    def last_update(self):
        qs = self.comment_set.order_by('-create_date')
        if qs.exists():
            return qs[0].create_date
        return None

    @models.permalink
    def get_absolute_url(self):
        return ('support_ticket_detail', (), {'pk': self.pk})

    def __unicode__(self):
        return u'{0}:{1}'.format(self.author, self.title)

    class Meta:
        verbose_name_plural = _('tickets items')
        verbose_name = _('ticket item')
        ordering = ['-create_date']


class Comment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        verbose_name=_('ticket'),
    )
    content = models.TextField(
        verbose_name=_('content'),
    )
    author = models.ForeignKey(
        User,
        verbose_name=_('author'),
    )
    create_date = models.DateTimeField(
        verbose_name=_('create date'),
        auto_now_add = True,
    )

    def __unicode__(self):
        return u'{0}:{1}:{2}'.format(self.author, self.ticket, self.content)

    class Meta:
        verbose_name_plural = _('comments items')
        verbose_name = _('comment item')
        ordering = ['create_date']
