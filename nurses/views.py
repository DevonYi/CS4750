
from django.shortcuts import render
import pymysql


def nurses(request):
    nurses = []
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
            sql = "SELECT * FROM nurse "
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                nurses.append(row)
                print("record: " + str(row))
    finally:
        # Close connection.
        connection.close()
    num_doctors = len(nurses)

    practiceSet = set()


    print(practiceSet)

    return render(
        request,
        'nurse.html', {
            'nurses': nurses
        }
    )