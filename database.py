class Patient:

    def __init__(self, first_name, last_name, patient_id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.patient_id = patient_id
        self.age = age
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name, patient_last_name,
                         patient_id, patient_age):
    new_patient = Patient(patient_first_name, patient_last_name,
                          patient_id, patient_age)
    return new_patient


def get_full_name(patient):
    return "{} {}".format(patient["First Name"], patient["Last Name"])


def main():
    x = Patient("David", "Ward", "", "")
    print(x.full_name())
    exit()
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 1, 30)
    db[22] = create_patient_entry("Bob",  "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris",  "Chou", 3, 25)
    print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print_database(db)
    print("Patient {} is a {}."
          .format(get_full_name(db[22]), adult_or_minor(db[22])))


def print_database(db):
    for patient_key in db:
        print(patient_key)
        print("Name: {}, Id: {}, age: {}"
              .format(get_full_name(db[patient_key]),
                      db[patient_key]["Id"], db[patient_key]["Age"]))


def find_patient(db, patient_id):
    return db[patient_id]


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
