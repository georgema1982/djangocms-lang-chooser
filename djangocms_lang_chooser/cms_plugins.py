from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase

from djangocms_lang_chooser.models import LanguageChooser


@plugin_pool.register_plugin
class LanguageChooserPlugin(CMSPluginBase):
    model = LanguageChooser
    render_template = 'djangocms_lang_chooser/lang_chooser.html'
    name = _('Language Chooser')
