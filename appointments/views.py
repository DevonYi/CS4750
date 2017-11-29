
from django.shortcuts import render
import pymysql


def appointments(request):
    appointments = []
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
            sql = "select aUid, aptDate, reason, pName, pSSN, pAllergies, nName, dName, hName, rNumber " \
                  "from appointment inner join nurse on (appointment.nUid = nurse.nUid) " \
                  "inner join patient on (appointment.pUid = patient.pUid) " \
                  "inner join doctor on (appointment.dUid = doctor.dUid)" \
                  "inner join hospital on (appointment.hUid = hospital.hUid)"
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                appointments.append(row)
                print("record: " + str(row))
    finally:
        # Close connection.
        connection.close()
    num_doctors = len(appointments)

    practiceSet = set()


    print(practiceSet)

    return render(
        request,
        'appointment.html', {
            'appointments': appointments
        }
    )