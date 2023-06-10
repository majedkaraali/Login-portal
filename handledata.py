import sqlite3
con=sqlite3.connect('database.db')
c=con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS User(
 	username text,
 	password text
 	)""")

def add_user(username,password):
    global state
    c.execute("SELECT username FROM User WHERE username=:username",{'username':username})
    x=c.fetchone()
    if x==None:
        c.execute("INSERT INTO User VALUES (:username,:password)",{'username':username,'password':password})
        con.commit()
        state=True
    else:
        state=False


def login_user(username,password):
    c.execute("SELECT password from user where username=:username",{'username':username})  
    x=c.fetchone()
    global acess,tx
    if x==None:
        print("invald username")
        acess=False
        tx="invald username"
    else:
        if password==x[0]:
            print('Sucsses')
            acess=True
            tx='Login Sucsses'
        else:
            print("invald password")
            acess=False
            tx="invald password"
        
#con.close()