from django.db import models

class PageSource (models.Model):
    page_id = models.AutoField(primary_key = True)
    page_url = models.CharField (max_length=400)
    page_name = models.CharField (max_length=20)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return self.info

class SearchItem (models.Model):
    item_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(PageSource, on_delete=models.CASCADE)
    item_price = models.CharField(max_length= 100)
    item_name = models.CharField(max_length=300)
    item_image = models.CharField(max_length=300)
    item_link = models.CharField(max_length=300)
    item_allergy = models.CharField(max_length=300)
    #store_location = models.CharField(max_length=10000)

    def __str__(self):
        return self.item_name

class Location (models.Model):
    location_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(PageSource, on_delete=models.CASCADE)
    store_location = models.CharField(max_length=10000)

    def __str__(self):
        return self.store_location


class Description (models.Model):
    item_id = models.ForeignKey(SearchItem, on_delete=models.CASCADE)
    quick_overview = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    direction_use = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=500)
    contra_indication = models.CharField(max_length=500)
    caution = models.CharField(max_length=500)

    def __str__(self):
        return self.quick_overview + self.ingredients

