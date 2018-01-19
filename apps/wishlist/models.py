from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
from datetime import datetime
from ..login.models import User

class ItemManager(models.Manager):
    def validate_item(self, post_data, added_by):
        errors = []
        if len(post_data['item_name']) < 4:
            errors.append("item name must be at least 3 characters")
        if not errors:
            new_item = self.create(
                added_by = added_by.name,
                name = post_data["item_name"]
                )
            new_item.wished_by.add(added_by)
            return new_item
        return errors


class Item(models.Model):
    name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    date_added = models.DateField(default = datetime.now)
    # https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/
    objects = ItemManager()
    wished_by = models.ManyToManyField(User, blank = True)
    

