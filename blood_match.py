import requests

part1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sbp31")
id_dic = part1.json()
part2_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"
                           + id_dic['Donor'])
donor_blood_type = part2_donor.text
part2_recipient = requests.get("http://vcm-7631.vm.duke.edu:5002/"
                               "get_blood_type/"+id_dic['Recipient'])
recipient_blood_type = part2_recipient.text
match = None
if donor_blood_type == recipient_blood_type:
    match = "Yes"
else:
    match = "No"
out_data = {"Name": "sbp31", "Match": match}
part_final = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                           json=out_data)
print(part_final.text)
