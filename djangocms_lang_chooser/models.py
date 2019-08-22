from cms.models import CMSPlugin
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


# Create your models here.
MARKERS = [
    ('raw', _('Raw language marker')),
    ('native', _('Native language marker')),
    ('current', _('Current language marker')),
    ('short', _('Short language marker')),
]


class LanguageChooser(CMSPlugin):
    template = models.CharField(max_length=10, blank=True, choices=MARKERS)
    template_other = models.CharField(max_length=200, blank=True)
    i18n_mode = models.CharField(max_length=10, blank=True, choices=MARKERS)
    i18n_mode_other = models.CharField(max_length=50, blank=True)

    @cached_property
    def get_template(self):
        return self.template or self.template_other

    @cached_property
    def get_i18n_mode(self):
        return self.i18n_mode or self.i18n_mode_other