
from django.shortcuts import render
import pymysql
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.shortcuts import redirect


@csrf_exempt
def appointments(request):
    appointments = []
    assert isinstance(request, HttpRequest)

    if (request.POST.get('create_apt')):
        return redirect('/create_apt/')

        # return render(
        #     request,
        #     'appointment.html', {
        #         # 'appointments': appointments
        #     }
        # )




    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='cs4750',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "select aUid, aptDate, reason, pName, pSSN, pAllergies, nName, dName, hName, rNumber " \
                  "from appointment left outer join nurse on (appointment.nUid = nurse.nUid) " \
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

@csrf_exempt
def create_apt(request):
    doctors = []
    patients = []
    hospitalrooms = []
    nurses = []
    rooms = []
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='cs4750',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "select * from doctor"
            cursor.execute(sql)
            print()
            for row in cursor:
                doctors.append(row)

        with connection.cursor() as cursor:
            # SQL
            sql = "select * from patient"
            cursor.execute(sql)
            print()
            for row in cursor:
                patients.append(row)

        with connection.cursor() as cursor:
            # SQL
            sql = "select * from hospital, room where hospital.hUid = room.hUid"
            cursor.execute(sql)
            print()
            for row in cursor:
                hospitalrooms.append(row)

        with connection.cursor() as cursor:
            # SQL
            sql = "select * from nurse"
            cursor.execute(sql)
            print()
            for row in cursor:
                nurses.append(row)

    finally:
        # Close connection.
        connection.close()

    if request.POST.get('submit_btn'):
        doctor = str(request.POST.get('doctor'))
        hospitalroom = str(request.POST.get('hospitalroom'))
        hospital = hospitalroom.split("+")[0]
        room = hospitalroom.split("+")[1]
        nurse = str(request.POST.get('nurse'))
        patient = str(request.POST.get('patient'))
        aptType = str(request.POST.get('aptType'))
        aptDate_temp = str(request.POST.get('aptDate'))
        reason = str(request.POST.get('reason'))
        aptDate =""

        print(aptDate_temp)
        for c in aptDate_temp:
            if c == "-":
                c="/"
            if c == "T":
                c = " "
            aptDate = aptDate+(str(c))
            print("HERE IS " + c)
        print("APT DATE" + aptDate)

        connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='root',
                                     db='cs4750',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        #appointment(aUid, aptDate, reason, aptType, nUid, dUid, pUid, rNumber, hUid);
        sql = "insert into appointment (aptDate, reason, aptType, nUid, dUid, pUid, rNumber, hUid) values (\"" + aptDate + "\", \"" + reason + "\", \"" + aptType + "\", " + nurse + ", " + doctor + ", " + patient + ", " + room + ", " + hospital + ")"
        try:
            with connection.cursor() as cursor:
                # SQL
                cursor.execute(sql)
                connection.commit()

        finally:
            # Close connection.
            connection.close()
        return redirect('/appointment/')

    return render(
        request,
        'create_apt.html', {
            'doctors': doctors,
            'patients': patients,
            'hospitalrooms': hospitalrooms,
            'nurses': nurses,

        }
    )