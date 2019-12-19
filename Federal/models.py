from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from base.models import BaseModel
from offices.models import ExecutiveOffice, LegislativeOffice, JudiciaryOffice


class Executive(BaseModel):
    related_ministry = models.ForeignKey(ExecutiveOffice, on_delete=models.DO_NOTHING, null=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='ex_last_modified_by',
                                         null=True,
                                         blank=True)

    def __str__(self):
        return self.title

    '''def get_absolute_url(self):
        return reverse('executive_update', args=(self.pk,))'''


class Legislative(BaseModel):
    related_house = models.ForeignKey(LegislativeOffice, on_delete=models.DO_NOTHING, null=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='leg_last_modified_by',
                                         null=True,
                                         blank=True)

    def __str__(self):
        return self.title


class Judiciary(BaseModel):
    related_court = models.ForeignKey(JudiciaryOffice, on_delete=models.DO_NOTHING, null=True, default=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='jud_last_modified_by',
                                         null=True,
                                         blank=True)

    def __str__(self):
        return self.title
