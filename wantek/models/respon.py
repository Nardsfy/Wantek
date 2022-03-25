def responseJSON(status_code, status, message, result):
    # fungsi untuk formating response ke json
    resp = {}
    resp['status_code'] = status_code
    resp['status'] = status
    resp['message'] = message
    resp['result'] = result
    return resp

def rowsToDict(cursor):
    columns = [i[0].lower() for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]