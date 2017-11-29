# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.models import Doctor


def doctor(request):

    # num_doctors = Doctor.objects.all.count()

    return render(
        request,
        'doctor.html',
    )