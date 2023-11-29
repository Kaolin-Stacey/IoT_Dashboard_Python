def getUserByRFID(rfidTag):
    import sqlite3 as sl
    from config import current_user
    with sl.connect('assets/iot_project.db') as con:
        cur = con.cursor()
        params = (rfidTag,)
        res = cur.execute("SELECT * FROM USER WHERE rfid_tag == ?",params)
        current_user = res.fetchone()
        print(current_user)

def getDB():
    import sqlite3 as sl
    with sl.connect('assets/iot_project.db') as con:
        cur = con.cursor()

        results = cur.execute("SELECT * FROM USER")
        user_list = results.fetchall()

        print(*user_list)