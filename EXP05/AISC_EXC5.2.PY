patients = []

fever = []

cough = []

insurance = []

age = {}


def display_kb():

    print("\n========== KNOWLEDGE BASE ==========")

    print("\nPatients:")
    for p in patients:
        print("Patient(", p, ")")

    print("\nFever:")
    for p in fever:
        print("Fever(", p, ")")

    print("\nCough:")
    for p in cough:
        print("Cough(", p, ")")

    print("\nInsurance:")
    for p in insurance:
        print("Insurance(", p, ")")

    print("\nAge:")
    for p, a in age.items():
        print("Age(", p, ",", a, ")")


def infer():

    print("\n========== FOL INFERENCE ==========")

    for p in patients:

        if p in fever and p in cough:
            print("Flu(", p, ")")

        if p in insurance:
            print("CashlessTreatment(", p, ")")

        if p in age and age[p] > 60:
            print("SeniorCitizen(", p, ")")

        if p in age and age[p] > 60 and p in insurance:
            print("PriorityTreatment(", p, ")")


def add_patient():

    name = input("Enter patient name: ")

    if name in patients:
        print("Patient already exists.")
        return

    patients.append(name)

    has_fever = input("Does the patient have fever? (yes/no): ")
    has_cough = input("Does the patient have cough? (yes/no): ")
    has_insurance = input("Does the patient have insurance? (yes/no): ")
    patient_age = int(input("Enter patient age: "))

    if has_fever == "yes":
        fever.append(name)

    if has_cough == "yes":
        cough.append(name)

    if has_insurance == "yes":
        insurance.append(name)

    age[name] = patient_age

    print("Patient added successfully.")


def update_status():

    name = input("Enter patient name: ")

    if name not in patients:
        print("Patient does not exist.")
        return

    has_fever = input("Does the patient have fever now? (yes/no): ")
    has_cough = input("Does the patient have cough now? (yes/no): ")
    has_insurance = input("Does the patient have insurance now? (yes/no): ")

    if has_fever == "yes" and name not in fever:
        fever.append(name)
    elif has_fever == "no" and name in fever:
        fever.remove(name)

    if has_cough == "yes" and name not in cough:
        cough.append(name)
    elif has_cough == "no" and name in cough:
        cough.remove(name)

    if has_insurance == "yes" and name not in insurance:
        insurance.append(name)
    elif has_insurance == "no" and name in insurance:
        insurance.remove(name)

    print("Status updated successfully.")


def check_flu():

    name = input("Enter patient name: ")

    if name not in patients:
        print("Patient does not exist.")
        return

    if name in fever and name in cough:
        print(name, "has FLU.")
    else:
        print(name, "does not have flu.")


def check_priority():

    name = input("Enter patient name: ")

    if name not in patients:
        print("Patient does not exist.")
        return

    if name in age and age[name] > 60 and name in insurance:
        print(name, "gets PRIORITY treatment.")
    else:
        print(name, "does not get priority treatment.")


def query_fol():

    print("\n========== FOL QUERY ==========")

    print("Examples:")
    print("Patient Rahul")
    print("Fever Rahul")
    print("SeniorCitizen Rahul")

    predicate = input("\nEnter predicate: ")
    value = input("Enter value: ")

    if predicate == "Patient":

        if value in patients:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Fever":

        if value in fever:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Cough":

        if value in cough:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Insurance":

        if value in insurance:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "SeniorCitizen":

        if value in age and age[value] > 60:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Flu":

        if value in fever and value in cough:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "PriorityTreatment":

        if value in age and age[value] > 60 and value in insurance:
            print("TRUE")
        else:
            print("FALSE")

    else:
        print("Unknown predicate.")


while True:

    print("\n")
    print("========================================")
    print("      FOL HOSPITAL MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Add Patient")
    print("2. Update Patient Status")
    print("3. Check Flu")
    print("4. Check Priority Treatment")
    print("5. FOL Query")
    print("6. Display Knowledge Base")
    print("7. Run Inference")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        update_status()

    elif choice == "3":
        check_flu()

    elif choice == "4":
        check_priority()

    elif choice == "5":
        query_fol()

    elif choice == "6":
        display_kb()

    elif choice == "7":
        infer()

    elif choice == "8":
        print("\nThank you for using the FOL Hospital System!")
        break

    else:
        print("Invalid choice. Please try again.")
