# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pymysql
from app.models import Doctor



def doctor(request):

    queryVal = 'all'

    if request.POST.get('submit_btn'):
        queryVal = str(request.POST.get('queryValue'))

    print(queryVal)

    print("loading page")
    doctors = []
    allDoctors = []
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='cs4750',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM doctor"

            if queryVal != "all":
                sql += " where practiceName = '" + queryVal + "'"

            print(sql)
            # Execute query.
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                doctors.append(row)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM doctor"

            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                allDoctors.append(row)

    finally:
        # Close connection.
        connection.close()

    practiceSet = set()

    practiceSet.add("all")

    for d in allDoctors:
        if d['practiceName'] not in practiceSet:
            practiceSet.add(d['practiceName'])


    return render(
        request,
        'doctor.html', {
            'doctors': doctors,
            'practices': practiceSet
        }
    )