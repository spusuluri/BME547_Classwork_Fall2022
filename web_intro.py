import requests

r2 = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r2)
print(type(r2))
print(r2.text)
print(r2.status_code)
if r2.status_code == 200:
    answer = r2.json()
    print(type(answer))
    for branch in answer:
        print(branch["name"])
else:
    print("Bad request: {}".format(r2.text))
user_info = {
    "name": "Satya Pusuluri",
    "net_id": "sbp31",
    "e-mail": "sbp31@duke.edu"
}

r3 = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
                   json=user_info)
print(r3)
print(r3.text)

msg = {"user": "sbp31", "message": "hello sbp31"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=msg)
r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/sbp31")
print(r1.text)
