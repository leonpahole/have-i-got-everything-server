from django.db import models

class ItemsListTemplate(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="")

    user_id = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

class ItemsListTemplateItem(models.Model):
    name = models.CharField(max_length=200)

    items_list = models.ForeignKey(ItemsListTemplate, related_name='items', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ItemsList(models.Model):
    name = models.CharField(max_length=200)

    user_id = models.CharField(max_length=1000)
    is_active = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ItemsListItem(models.Model):
    active_item_list = models.ForeignKey(ItemsList, related_name='items', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    checked = models.BooleanField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name