from flask import Flask, request, jsonify
import logging
from pymodm import connect, MongoModel, fields
from database_definition import Patient

"""
Database format

[{
"name": <string>,
"id": <integer>,
"blood_type": <string>,
"test_name": [<string1>, <string2>],
"test_result": <string>
}]

"""
app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_on():
    return "DB server is on"


def add_patient(patient_name, patient_id, blood_type):
    new_patient = Patient(name=patient_name,
                          id=patient_id,
                          blood_type=blood_type)
    added_patient = new_patient.save()
    return added_patient


def init_server():
    # initialize logging
    connect("mongodb+srv://bme547classwork:UqZB1uVntFpMWioG@bme547"
            ".s4vkcnr.mongodb.net/health_db?retryWrites=true&w=majority")


@app.route('/new_patient', methods=["POST"])
def add_new_patient_to_server():
    """
    Receive data from POSt request
    Call other functions to do all the work
    Return information
    """
    in_data = request.get_json()
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    add_patient(in_data["name"],
                in_data['id'],
                in_data['blood_type'])
    return "Patient successfully added", 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return "Key {} has the wrong data type".format(key)
    return True


@app.route('/add_test', methods=["POST"])
def add_test():
    in_data = request.get_json()
    msg, status_code = add_test_worker(in_data)
    return "Test added", 200


def add_test_worker(in_data):
    result = validate_new_test_info(in_data)
    if result is not True:
        return result, 400
    msg, status_code = add_test_info(in_data)
    return msg, status_code


def find_patient(patient_id):
    from pymodm import errors as pymodm_errors
    try:
        found_patient = Patient.objects.raw({"_id": patient_id}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return found_patient


def validate_new_test_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [int, str, int]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return "Key {} has the wrong data type".format(key)
    return True


def add_test_info(in_data):
    patient = find_patient(in_data["id"])
    if patient is False:
        return "Patient ID {} not found in database."\
                   .format(in_data["id"]), 400
    patient.test_name.append(in_data["test_name"])
    patient.test_result.append(in_data["test_result"])
    patient.save()
    return "Successfully added test.", 200


if __name__ == "__main__":
    init_server()
    app.run()
