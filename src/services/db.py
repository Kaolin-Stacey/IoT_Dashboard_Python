def getUserByRFID(rfidTag):
    import sqlite3 as sl
    from config import current_user
    with sl.connect('../assets/iot_project.db') as con:
        cur = con.cursor()
        params = (rfidTag,)
        res = cur.execute("SELECT * FROM USER WHERE rfid_tag == ?",params)
        current_user = res.fetchone()