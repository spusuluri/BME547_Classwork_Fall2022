def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient

def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    print(db)
    print(db[2][2])
    print_db(db)
    print(find_patient(db, 2))
    add_test_to_patient(db, 3, "HDL", 100)
    print(db)

def print_db(db):
    for patient in db:
        print("Name: {}, id: {}, age: {}".format(patient[0], patient[1], patient[2]))

def find_patient(db, patient_id):
    for patient in db:
        if patient[1] == patient_id:
            return patient
    return False

def add_test_to_patient(db, patient_id, test_name, test_value):
    patient = find_patient(db, patient_id)
    patient[3].append((test_name, test_value))



if __name__ == "__main__":
    main()