# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bala.models import ContactDetails, Articles, Comments

admin.site.register(ContactDetails)
admin.site.register(Articles)
admin.site.register(Comments)