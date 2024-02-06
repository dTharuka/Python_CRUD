# def individual_serial(user) -> dict:
#     return {
#         "id": str(user["_id"]),
#         "firstName": user["firstName"],
#         "lastName": user["lastName"],
#         "userName": user["userName"],
#         "email": user["email"],
#         "contactNumber": user["contactNumber"],
#         "gender": user["gender"],
#         "country": user["country"],
#         "state": user["state"],
#         "city": user["city"],
#     }
#
#
# def list_serial(users) -> list:
#     return [individual_serial(user) for user in users]



def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "userName": user["userName"],
        "email": user["email"],
        "contactNumber": user["contactNumber"],
        "gender": user["gender"],
        "country": user["country"],
        "state": user["state"],
        "city": user["city"],
    }

def list_serial(users) -> list:
    return [individual_serial(user) for user in users]
