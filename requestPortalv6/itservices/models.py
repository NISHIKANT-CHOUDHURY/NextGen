from django.db import models

# Create your models here.
purpose_choices=(
   ('Project' , "Project"),
    ('Lab', "Lab"),

)

location_choices=(
   ('EC1' , "EC1"),
    ('EC2', "EC2"),
     ('EC3' , "EC3"),
    ('EC4', "EC4"),

)
tower_choices=(
    ('Tower1' , "Tower1"),
    ('Tower2', "Tower2"),
    ('Tower3' , "Tower3"),
    ('Tower4', "Tower4"),

)

floor_choices=(
    ('1' , "floor 1"),
    ('2', "floor 2"),
    ('3' , "floor 3"),
    ('4', "floor 4"),

)

wing_choices=(
    ('A' , "wing A"),
    ('B', "wing B"),


)

class Desktop(models.Model):
    user = models.CharField(max_length=100)
    # purpose = models.CharField(max_length=100, )
    date = models.CharField(max_length=100, )
    location = models.CharField(max_length=100, )
    days = models.CharField(max_length=100, )
    laptop_type = models.CharField(max_length=100, )


    # tower = models.CharField(max_length=100, )
    # floor = models.CharField(max_length=100,)
    # wing = models.CharField(max_length=100, )
    # monitor_size = models.CharField(max_length=100, )
    # ram = models.CharField(max_length=100, )
    # hard_disk= models.CharField(max_length=100, )
    # processor = models.CharField(max_length=100, )
    # city= models.CharField(max_length=100, )
    # cubical= models.CharField(max_length=100, )



class Page_visited(models.Model):
    user = models.CharField(max_length=100)
    desktop_request = models.IntegerField(default=0)
    url_desktop = models.CharField(max_length=100, )
    it_assest_release = models.IntegerField(default=0)
    url_it_assest_release = models.CharField(max_length=100, )
    admin_access = models.IntegerField(default=0)
    url_admin_access = models.CharField(max_length=100, )
    software_requestion = models.IntegerField(default=0)
    url_software_requestion = models.CharField(max_length=100, )
    dns = models.IntegerField(default=0)
    url_dns = models.CharField(max_length=100, )
    email = models.IntegerField(default=0)
    url_dns = models.CharField(max_length=100, )
    network = models.IntegerField(default=0)
    url_network = models.CharField(max_length=100, )
    it_assest = models.IntegerField(default=0)
    url_it_assest = models.CharField(max_length=100, )
    byod = models.IntegerField(default=0)
    url_byod = models.CharField(max_length=100, )
    link_proposal = models.IntegerField(default=0)
    url_link_proposal = models.CharField(max_length=100, )
    usb_access = models.IntegerField(default=0)
    url_usb_access = models.CharField(max_length=100, )
