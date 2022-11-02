import pytest
from database_definition import Patient


def test_add_patient():
    from db_server import add_patient, init_server
    init_server()
    patient_name = "David"
    patient_id = 222
    blood_type = "A+"
    answer = add_patient(patient_name, patient_id, blood_type)
    find_patient = Patient.objects.raw({"_id": 222}).first()
    find_patient.delete()
    assert answer.name == patient_name
