def create_patient_entry(patient_first_name, patient_last_name,  patient_id, patient_age):
    new_patient = {
        'First Name' : patient_first_name,
        'Last Name' : patient_last_name,
        'Id' : patient_id,
        'Age' : patient_age,
        'Tests' : []
    }
    return new_patient


def get_full_name(patient):
    return "{} {}".format(patient["First Name"], patient["Last Name"])


def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry("Bob",  "Boyles", 2, 34))
    db.append(create_patient_entry("Chris",  "Chou", 3, 25))
    print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print_database(db)
    print("Patient {} is a {}.".format(get_full_name(db[2]), adult_or_minor(db[2])))


def print_database(db):
    for patient in db:
        print("Name: {}, Id: {}, age: {}"
              .format(get_full_name(patient), patient["Id"], patient["Age"]))


def find_patient(db, patient_id):
    for patient in db:
        if patient['Id'] == patient_id:
            return patient
    return False


def add_test_to_patient(db, patient_id, test_name, test_value):
    patient = find_patient(db, patient_id)
    patient['Tests'].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


if __name__ == "__main__":
    main()
