class CallNames():
    TOKEN = '16563c5392cc277cea4f2f1c51cfe64d618d4744b4f9b4968cd6af0a27987a81'
    URL = "https://gorest.co.in/public-api"
    HEADERS = {'content-type': 'application/json',
               'Authorization': f'Bearer {TOKEN}'
               }
    CREATE_USER_PATH = "/users/"
    UPDATE_USER_PATH = "/users/"
    DELETE_USER_PATH = "/users/"
    GET_USER = "/users/"
