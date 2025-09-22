import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="Nathan",
            password="Hiwot@2023",
            database="flight_game"
        )
        cursor = conn.cursor()

        query = """
            SELECT latitude_deg, longitude_deg
            FROM airport
            WHERE ident = %s;
        """
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()

        return (float(result[0]), float(result[1])) if result else None

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def run_airport_distance():
    icao1 = input("Enter ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter ICAO code of the second airport: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if not coords1:
        print(f"Airport with ICAO code '{icao1}' not found in the database.")
    if not coords2:
        print(f"Airport with ICAO code '{icao2}' not found in the database.")

    if coords1 and coords2:
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} kilometers")

if __name__ == "__main__":
    run_airport_distance()
