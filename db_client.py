import requests


def upload_patient_info(patient_name, patient_id, patient_blood_type):
    out_data = {
        'name': patient_name,
        'id': patient_id,
        'blood_type': patient_blood_type
    }

    r = requests.post("http://127.0.0.1:5000/new_patient",
                      json=out_data)
    return r.text, r.status_code


"""
out_data1 = {
    'id': 3,
    'test_name': 'LDL',
    'test_result': 200
}
r1 = requests.post("http://127.0.0.1:5000/add_test",
                   json=out_data1)
print(r1.status_code)
print(r1.text)
"""
