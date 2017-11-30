from django.shortcuts import render
import pymysql
# Create your views here.






# Connect to the database.


def patients(request):
    # p = Patient.objects.all()
    # patients = len(p)
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
            # SQL
            sql = "SELECT * FROM Patient"
            # Execute query.
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
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

