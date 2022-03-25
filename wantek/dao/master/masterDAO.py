from wantek import dbConnect
from wantek.models.respon import *

def getUser():
    # get user all user
    connection = dbConnect()
    try:        
        cursor = connection.cursor()
        query = '''SELECT username, password, roles from users'''
        cursor.execute(query)
        data = rowsToDict(cursor)        
        cursor.fetchall()               
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

def insertUser(p_username, p_password, p_role):
    connection = dbConnect()
    try:
        cursor = connection.cursor()
        query = '''INSERT INTO users(username, password, roles)
        VALUES(%s, %s, %s)        
        '''
        cursor.execute(query, (p_username, p_password, p_role))
        connection.commit()
        return responseJSON(200, "T", "Success add new user.", [])
    except Exception as error:
        return responseJSON(400, "F", error, [])
    finally:
        if(connection):
            cursor.close()
            connection.close()