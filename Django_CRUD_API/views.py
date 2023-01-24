
import requests, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Django_CRUD_API.models import PersonBasicDetails

@csrf_exempt
def get_record(request):
    try:
        request_object = json.loads(request.body)
        return_object = {}
        if 'person_number' in request_object and request_object['person_number']:
            person_object = []
            if request_object['person_number'].lower()=="all":
                person_object = list(PersonBasicDetails.objects.filter(is_deleted = False).values())
            else:
                person_object = list(PersonBasicDetails.objects.filter(is_deleted = False, person_number = request_object['person_number']).values())

            if person_object:
                return_object = {
                    "status": 200,
                    "message": "Data retrived successfully",
                    "result":person_object
                }
            else:
                return_object = {
                    "status": 200,
                    "message": "No data found",
                    "result": []
                }
        else: 
            return_object = {
                "status": 500,
                "message": "Invalid Request object"
            }
    except (Exception) as error:
        print("get_record(): ",error)
        return_object = {
            "status": 500,
            "message": "Something went wrong"
        }
    return JsonResponse(return_object, safe=False)

@csrf_exempt
def add_record(request):
    try:
        print("request-->",request)
        request_object = json.loads(request.body)
        return_object = {}
        print("request_object-->",request_object)
        if 'person_name' in request_object and request_object['person_name'] and 'contact' in request_object and request_object['contact'] and 'email_id' in request_object and request_object['email_id']:
            person_object = PersonBasicDetails()
            person_object.person_name = request_object['person_name']
            person_object.contact = request_object['contact']
            person_object.email_id = request_object['email_id']
            if 'country' in request_object and request_object['country']:
                person_object.country = request_object['country']
            if 'state' in request_object and request_object['state']:
                person_object.state = request_object['state']
            if 'district' in request_object and request_object['district']:
                person_object.district = request_object['district']
            if 'city' in request_object and request_object['city']:
                person_object.city = request_object['city']
            if 'pincode' in request_object and request_object['pincode']:
                person_object.pincode = request_object['pincode']
            person_object.save()

            return_object = {
                "status": 200,
                "message": "Record inserted successfully"
            }
        else: 
            print("request_object-->",request_object)
            return_object = {
                "status": 500,
                "message": "Invalid Request object"
            }
    except (Exception) as error:
        print("add_record(): ",error)
        return_object = {
            "status": 500,
            "message": "Something went wrong"
        }
    return JsonResponse(return_object, safe=False)

@csrf_exempt
def update_record(request):
    try:
        request_object = json.loads(request.body)
        return_object = {}
        if 'person_number' in request_object and request_object['person_number']:
            #  and 'contact' in request_object and request_object['contact'] and 'email_id' in request_object and request_object['email_id']:
            person_object = PersonBasicDetails.objects.filter(is_deleted = False, person_number = request_object['person_number'])
            if 'person_name' in request_object and request_object['person_name']:
                person_object.update(person_name = request_object['person_name'])
            if 'contact' in request_object and request_object['contact']:
                person_object.update(contact = request_object['contact'])
            if 'email_id' in request_object and request_object['email_id']:
                person_object.update(email_id = request_object['email_id'])
            if 'country' in request_object and request_object['country']:
                person_object.update(country = request_object['country'])
            if 'state' in request_object and request_object['state']:
                person_object.update(state = request_object['state'])
            if 'district' in request_object and request_object['district']:
                person_object.update(district = request_object['district'])
            if 'city' in request_object and request_object['city']:
                person_object.update(city = request_object['city'])
            if 'pincode' in request_object and request_object['pincode']:
                person_object.update(pincode = request_object['pincode'])
            # person_object.save()

            return_object = {
                "status": 200,
                "message": "Record inserted successfully"
            }
        else: 
            return_object = {
                "status": 500,
                "message": "Invalid Request object"
            }
    except (Exception) as error:
        print("update_record(): ",error)
        return_object = {
            "status": 500,
            "message": "Something went wrong"
        }
    return JsonResponse(return_object, safe=False)

@csrf_exempt
def delete_record(request):
    try:
        request_object = json.loads(request.body)
        return_object = {}
        if 'person_number' in request_object and request_object['person_number']:
            person_object = PersonBasicDetails.objects.filter(is_deleted = False, person_number = request_object['person_number']).update(is_deleted=True)
            return_object = {
                "status": 200,
                "message": "Record deleted successfully"
            }
        else: 
            return_object = {
                "status": 500,
                "message": "Invalid Request object"
            }
    except (Exception) as error:
        print("delete_record(): ",error)
        return_object = {
            "status": 500,
            "message": "Something went wrong"
        }
    return JsonResponse(return_object, safe=False)