from django.contrib.gis.db import models

class Shop(models.Model):
    #  Shop Information
    business_name = models.CharField(max_length=200)
    physical_address = models.TextField()
    business_phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    updated = models.DateField(auto_now=True)

    # Contact Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title_position = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    # Posted Labour Rates
    body_sheet_metal = models.IntegerField()
    aluminum_body = models.IntegerField()
    refinish_labour = models.IntegerField()
    aluminum_structure = models.IntegerField()
    structural = models.IntegerField()
    carbon_fibre = models.IntegerField()
    frame = models.IntegerField()
    fibre_glass = models.IntegerField()
    mechanical = models.IntegerField()
    paint_materials = models.IntegerField()
    luxury_body = models.IntegerField()
    luxury_refinish = models.IntegerField()
    luxury_structural = models.IntegerField()
    luxury_frame = models.IntegerField()
    luxury_mechanical = models.IntegerField()

    # Prices for Other Services
    inside_storage = models.IntegerField()
    outside_storage = models.IntegerField()
    four_wheel_alignment = models.IntegerField()
    pre_scan = models.IntegerField()
    post_scan = models.IntegerField()

    # Geometry fields
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lon = models.DecimalField(max_digits=5, decimal_places=2)
    geom  = models.PointField(srid=4326)
    geom_m = models.PointField(srid=3857) # web mercator

    def __str__(self):
        return self.business_name

class ZipCodes(models.Model):
    ZIP = models.CharField(max_length=6)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)
    geom = models.PointField(srid=3857)

    def __str__(self) -> str:
        return f"{self.ZIP} {self.geom}"