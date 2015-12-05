from __future__ import unicode_literals
from django import forms
from django.utils.html import format_html


class MediumEditorTextarea(forms.Textarea):

    def render(self, name, value, attrs=None):

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
        html = format_html('{}<div {}></div>'.format(html, param_str))
        return html

    class Media:
        css = {'all': (
            '//cdn.jsdelivr.net/medium-editor/latest/css/'
            'medium-editor.min.css',
            'css/mediumeditor/django-mediumeditor.css',
        )}
        js = (
            '//cdn.jsdelivr.net/medium-editor/latest/js/medium-editor.min.js',
            'js/mediumeditor/django-mediumeditor.js', )
