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

    def __str__(self):
        return self.item_name


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



#class Medicine(models.Model):
 #   meds_name = models.CharField(max_length=100)
  #  meds_price = models.FloatField(max_length=10)
   # meds_image = models.CharField(max_length=100)
    ##meds_overview = models.CharField(max_length=1000)
    #meds_description = models.CharField(max_length=500)
    #meds_direction = models.CharField(max_length=1000)
    #meds_ingredient = models.CharField(max_length=1000)
    #meds_indication = models.CharField(max_length=1000)
    #meds_caution = models.CharField(max_length=1000)


    #def __str__(self):
     #   return self.meds_name +" "+ str(self.meds_price)


#class Supplement (models.Model):
 #   supp_name = models.CharField(max_length=100)
  #  supp_price = models.FloatField(max_length=10)
   # supp_image = models.CharField(max_length=100)
    #supp_overview = models.CharField(max_length=1000)
    #supp_description = models.CharField(max_length=500)
    #supp_direction = models.CharField(max_length=1000)
    #supp_ingredient = models.CharField(max_length=1000)
    #supp_indication = models.CharField(max_length=1000)
    #supp_caution = models.CharField(max_length=1000)

    #def __str__(self):
     #   return self.supp_name +" "+ str(self.supp_price)