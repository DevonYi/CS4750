from django.shortcuts import render
import pymysql
# Create your views here.






# Connect to the database.


def patients(request):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='cs4750',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    if request.POST.get('edit_Patient'):
        patientUid = request.POST.get('hiddenUid', '')
        print("editing")
        print(patientUid)

        try:
            with connection.cursor() as cursor:
                # SQL
                sql = "SELECT * FROM Patient where pUid = '" + patientUid + "'"
                cursor.execute(sql)
                # print("cursor.description: ", cursor.description)
                for row in cursor:
                    patient = row
        finally:
            # Close connection.
            connection.close()

        return render(
            request,
            'editPatient.html', {
                "patient": patient
            }
        )

    if request.POST.get('submit_Edits'):
        print("submitting")
        patientUid = request.POST.get('editUid', '')
        patientAllergies = request.POST.get('editAllergies')
        patientSSN = request.POST.get('editSSN')
        patientHC = request.POST.get('editHC')
        patientName = request.POST.get('editName')

        print(patientUid)
        print(patientAllergies)
        print(patientSSN)
        print(patientName)
        print(patientHC)

        try:
            with connection.cursor() as cursor:
                # SQL
                sql = "Update patient set pAllergies = '" + patientAllergies + "', pSSN = '" + patientSSN + "', pHealthCare = '" + patientHC + "', pName = '" + patientName + "' " + " where pUid = " + patientUid
                print(sql)
                cursor.execute(sql)
                # print("cursor.description: ", cursor.description)
        finally:
            # Close connection.
            connection.commit()
            connection.close()



    patients = []
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='root',
                                 db='cs4750',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    print("connect successful!!")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Patient"
            # Execute query.
            cursor.execute(sql)
            # print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                patients.append(row)
    finally:
        # Close connection.
        connection.close()


    return render(
        request,
        'patients.html', {
            'patients': patients,
        }
    )

