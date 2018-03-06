import urlparse
import datetime

from django import forms
from django.utils.safestring import mark_safe
from django.forms.utils import ErrorList
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import pytz

from .models import Content

class ContentAdminForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = "__all__"
        widgets = {'status': forms.RadioSelect}

    def clean(self):
        """
        To validate story URL
        """
        super(ContentAdminForm, self).clean()
        cleaned_data = self.cleaned_data
        isDuplicate = False
            # check for duplicate slug
        title = cleaned_data.get('title')
        slug = cleaned_data.get('slug')
        pub_date = cleaned_data.get('published_date')
        body = cleaned_data.get('body_html')
        pubstatus = cleaned_data.get('status')
        story_status = cleaned_data.get('story_status')
        if pubstatus == 2 and story_status != 0:
            self._errors['story_status'] = ErrorList([mark_safe("Can not publish with this status.")])
        if pubstatus == 2 and not pub_date:
            self._errors['published_date'] = ErrorList([mark_safe("published date can not be null.")])
        s = len(body.split('.'))
        if s < 8 or len(body) < 300:
            self._errors['body_html'] = ErrorList([mark_safe("Word count minimum error")])
        if not slug:
            slug = slugify(title)
        storyQs = Content.objects.only('id', 'slug').filter(slug=slug)
        if self.instance:
            storyQs = storyQs.exclude(id=self.instance.id)
        if storyQs:
            isDuplicate = True
            self._errors['title'] = ErrorList([mark_safe(
                """<p><a href="/admin/content_management_system/content/%d/" target="_blank">Potential Duplicate: story with same title already exists.</a></p>""" % (
                    storyQs.values_list('id', flat=True)[0]))])
        if pub_date:
            pub_date = cleaned_data.get('published_date').replace(tzinfo=None)
            d = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
            print pub_date, d
            if pub_date:
                if pub_date > d:
                    self._errors['published_date'] = ErrorList([mark_safe("published date can't be future date")])
        return cleaned_data

