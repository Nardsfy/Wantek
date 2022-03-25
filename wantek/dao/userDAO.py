from wantek import dbConnect
from wantek.models.respon import *

def getUser(p_username, p_password):
    # get user by username, password
    connection = dbConnect()
    try:        
        cursor = connection.cursor()
        query = '''SELECT username, password, roles from users 
        WHERE username=%s AND password=%s'''
        cursor.execute(query, (p_username, p_password))
        data = rowsToDict(cursor)        
        cursor.fetchone()               
        if data:                   
            return responseJSON(200, "T", "User data found.", data)
        else:
            return responseJSON(200, "T", "User data not found.", [])
    except Exception as error:
        return responseJSON(400, "F", error, [])
    finally:
        if(connection):
            cursor.close()
            connection.close()