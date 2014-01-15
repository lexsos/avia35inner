from __future__ import absolute_import

from django.template import Library
from django.contrib.auth.forms import AuthenticationForm


register = Library()


@register.inclusion_tag('accounts/login.html')
def accounts_login_form():
    return {'form': AuthenticationForm()}
