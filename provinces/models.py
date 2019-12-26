from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from base.models import BaseModel
from offices.models import ProvinceJudiciaryOffice, ExecutiveOffice


class ProvinceJudiciary(BaseModel):
    court = models.ForeignKey(ProvinceJudiciaryOffice, on_delete=models.DO_NOTHING, null=True, default=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pro_jud_last_modified_by',
                                         null=True,
                                         blank=True)

    def __str__(self):
        return self.title


class ProvinceExecutive(BaseModel):
    related_ministry = models.ForeignKey(ExecutiveOffice, on_delete=models.DO_NOTHING, null=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='pro_ex_last_modified_by',
                                         null=True,
                                         blank=True)

    def __str__(self):
        return self.title
