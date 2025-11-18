from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_airport(icao):
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="1111",
        autocommit=True
    )

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result


@app.route('/airport/<icao>')
def airport(icao):
    icao = icao.upper()
    data = get_airport(icao)

    if data is None:
        return {"ICAO": icao, "Error": "Airport not found"}

    return {
        "ICAO": icao,
        "Name": data["name"],
        "Location": data["municipality"]
    }


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)