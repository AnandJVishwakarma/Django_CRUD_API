from django.db import models

class ConstantFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class PersonBasicDetails(ConstantFields):
    person_number = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=256, null=False)
    contact = models.IntegerField(null=False)
    email_id = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    pincode = models.CharField(max_length=256)

    class Meta:
        db_table = "person_basic_details"