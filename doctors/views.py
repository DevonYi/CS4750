# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pymysql
from app.models import Doctor


def doctor(request):
    doctors = []
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='cs4750',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    print("connect successful!!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM doctor"
            # Execute query.
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                doctors.append(row)
                print("record: " + str(row))
    finally:
        # Close connection.
        connection.close()
    num_doctors = len(doctors)

    practiceSet = set()

    practiceSet.add("all")

    for d in doctors:
        print(d)
        print(d.keys())
        if d['practiceName'] not in practiceSet:
            practiceSet.add(d['practiceName'])

    print(practiceSet)

    return render(
        request,
        'doctor.html', {
            'doctors': doctors,
            'practices': practiceSet
        }
    )