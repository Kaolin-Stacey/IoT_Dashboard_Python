def getUserByRFID(rfidTag):
    import sqlite3 as sl
    from config import current_user
    with sl.connect('assets/iot_project.db') as con:
        cur = con.cursor()
        params = (rfidTag,)
        res = cur.execute("SELECT * FROM USER WHERE rfid_tag = ?",params)
        current_user = res.fetchone()
        return current_user

def getDB():
    import sqlite3 as sl
    with sl.connect('assets/iot_project.db') as con:
        cur = con.cursor()

        results = cur.execute("SELECT * FROM USER")
        user_list = results.fetchall()

        print(*user_list)

def addUser(name, tag, tempThres, humidThres, lightThres):
    import sqlite3 as sl
    with sl.connect('assets/iot_project.db') as con:
        cur = con.cursor()

        results = cur.execute("INSERT INTO USER (name, rfid_tag,temp_threshold,humidity_threshold,light_threshold) VALUES (?,?,?,?,?)", (name, tag, tempThres, humidThres, lightThres))

        # results = cur.execute("UPDATE USER SET rfid_tag = ? WHERE name = ?",(tag, name))

        con.commit()