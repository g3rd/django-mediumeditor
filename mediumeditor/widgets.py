from __future__ import unicode_literals
import json
from django import forms
from django.utils.safestring import mark_safe

from .conf import settings


class MediumEditorTextarea(forms.Textarea):

    def render(self, name, value, attrs=None, renderer=None):

        if attrs is None:
            attrs = {}
        attrs.update({'class': 'django-mediumeditor-input'})

        identifier = attrs.get('id', 'id_{}'.format(name))
        params = {
            'data-mediumeditor-textarea': identifier,
            'class': 'django-mediumeditor-editable',
            'id': '{}_editable'.format(identifier),
        }
        param_str = ' '.join('{}="{}"'.format(k, v) for k, v in params.items())
        html = super(MediumEditorTextarea, self).render(name, value, attrs)
        options = json.dumps(settings.MEDIUM_EDITOR_OPTIONS)
        html = mark_safe(u'''{}
            <div {}></div>
            <script type="text/javascript">
                MediumEditorOptions={};
            </script>'''.format(html, param_str, options))
        return html

    class Media:
        css = {'all': (
            '//cdn.jsdelivr.net/medium-editor/latest/css/'
            'medium-editor.min.css',
            'css/mediumeditor/django-mediumeditor.css',
            '//cdn.jsdelivr.net/medium-editor/latest/css/themes/{}.min.css'.format(
                settings.MEDIUM_EDITOR_THEME
            )
        )}
        js = (
            '//cdn.jsdelivr.net/medium-editor/latest/js/medium-editor.min.js',
            'js/mediumeditor/django-mediumeditor.js', )
