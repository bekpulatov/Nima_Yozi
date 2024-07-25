import sqlite3
com = sqlite3.connect("Baza.db")
sql = com.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS bollar_info(chatid TEXT, username TEXT)')
com.commit()

def add_user(chatid, username): 
    sql.execute(f"INSERT INTO bollar_info(chatid, username) VALUES('{chatid}', '{username}')")
    com.commit()
    return "qo'shildi"



# com.close()
