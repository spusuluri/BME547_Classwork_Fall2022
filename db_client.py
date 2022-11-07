import requests
"""
out_data = {
    'name': "Charlie",
    'id': 3,
    'blood_type': "AB-"
}
r = requests.post("http://127.0.0.1:5000/new_patient",
                  json=out_data)
print(r.status_code)
print(r.text)
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
