patients = {}
from datetime import datetime


#sample data
patients['A001']={
        "registration_date": "12-12-2024",
        "name": "ani",
        "dob": "1-2-1992",
        "gender": "woman",
        "address": "Jl S Parman no 123",
        "phone": "082345678",
        "payment_scheme": "Cash",
        "clinical_data": {
            "BP": "120/80",
            "HR": 100,
            "T": 38,
            "RR": 18,
            "SpO2": 99
        }
}

patients['A002']={
        "registration_date": "13-12-2024",
        "name": "Budi",
        "dob": "02-02-2008",
        "gender": "man",
        "address": "Jl Mertoyudan no 99, Yogyakarta",
        "phone": "09876546",
        "payment_scheme": "Cash",
        "clinical_data": {
            "BP": "110/70",
            "HR": 120,
            "T": 39.5,
            "RR": 22,
            "SpO2": 94
        }
}

patients['A003']={
        "registration_date": "13-12-2024",
        "name": "Lala",
        "dob": "08-10-1980",
        "gender": "woman",
        "address": "Jl Agung no 27 Jakarta",
        "phone": "085678455",
        "payment_scheme": "Private Insurance",
        "clinical_data": {
            "BP": "180/90",
            "HR": 120,
            "T": 36.8,
            "RR": 24,
            "SpO2": 90
        }
}

patients['A004']={
        "registration_date": "18-01-2025",
        "name": "Setiadi",
        "dob": "14-08-1970",
        "gender": "man",
        "address": "Jl Abimanyu no.88 Bekasi",
        "phone": "0876547656",
        "payment_scheme": "Public Insurance",
        "clinical_data": {
            "BP": "145/73",
            "HR": 89,
            "T": 37.2,
            "RR": 20,
            "SpO2": 98
        }
}

patients['A005']={
        "registration_date": "21-02-2025",
        "name": "Anna",
        "dob": "30-05-2012",
        "gender": "woman",
        "address": "Jl Menari no.72, Depok",
        "phone": "0878989750",
        "payment_scheme": "Cash",
        "clinical_data": {
            "BP": "132/84",
            "HR": 76,
            "T": 36.5,
            "RR": 18,
            "SpO2": 98
        }
}

# Menu Display
def show_menu():
    print("\nPatient Registration Menu:")
    print("1. Add Patient Data")
    print("2. View All Patient Data")
    print("3. Search Patient Data")
    print("4. Edit Patient Data")
    print("5. Delete Patient Data")
    print("6. Sort Patient Data")
    print("7. Filter Patient Data")
    print("8. Treatment options")
    print("9. Exit\n")
    choice = input("Enter your choice (1-9): ")
    return choice


# Utility functions

def validate_phone_number(number):
    return number.isdigit() and (10 <= len(number) <= 13)

def validate_gender(gender):
    return gender.lower() in ['man', 'woman']

def validate_payment_scheme(scheme):
    return scheme.lower() in ['private insurance', 'public insurance', 'cash']

#Function to Add Patient Data

def add_patient():
    mrn = input("Enter Medical Record Number (MRN): ")
    if mrn.lower() in (key.lower() for key in patients):
        print("Patient with this MRN already exists!")
        return

    #enter_name
    name = input("Enter Patient Name: ")
    
    #enter_DOB
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    
    #enter_Gender
    while True:
        gender = input("Enter Gender (Man/Woman): ").lower()
        if validate_gender(gender):
            break
        else:      
            print("Invalid input. Choose Gender (Man/Woman): ")
    
    #enter_address
    address = input("Enter Address: ")
    
    #enter_phone_number
    while True:
        phone = input("Enter Phone Number: ")
        if validate_phone_number(phone):
            break
        else:
            print("Invalid number. Enter Phone Number: ")
    
    #enter_payment_scheme
    while True:
        payment_scheme = input("Enter Payment Scheme (Private Insurance, Public Insurance, Cash): ").lower()
        if validate_payment_scheme(payment_scheme):
            break
        else:
            print("Invalid scheme. Enter Payment Scheme: ")
    
    #enter_vital_signs
    print("Enter Vital Signs:")
    blood_pressure = input("Blood Pressure (e.g., 120/80): ")
    heart_rate = (int(input("Heart Rate (bpm): ")))
    temperature = (float(input("Temperature (°C): ")))
    respiratory_rate = (int(input("Respiratory Rate (breaths/min): ")))
    oxygen_saturation = (int(input("Oxygen Saturation (%): ")))

    patients[mrn] = {
        "registration_date": datetime.today().strftime('%d-%m-%Y'),
        "name": name,
        "dob": dob,
        "gender": gender,
        "address": address,
        "phone": phone,
        "payment_scheme": payment_scheme,
        "clinical_data": {
            "BP": blood_pressure,
            "HR": heart_rate,
            "T": temperature,
            "RR": respiratory_rate,
            "SpO2": oxygen_saturation
        }
    }
    print("Patient data successfully added!")

#Function to view all patient data

def view_patients():
    if len(patients) == 0:
        print("No patients saved yet.")
    else:
        print("-" * 173)
        print("MRN" + ' ' * (5 - len("MRN")) + "| " +
              "Date" + ' ' * (10 - len("Date")) + "| " +
              "Name" + ' ' * (10 - len("Name")) + "| " +
              "DOB" + ' ' * (10 - len("DOB")) + "| " +
              "Gender" + ' ' * (7 - len("Gender")) + "| " +
              "Address" + ' ' * (35 - len("Address")) + "| " +
              "Phone Number" + ' ' * (13 - len("Phone Number")) + "| " +
              "Payment scheme" + ' ' * (18 - len("Payment scheme")) + "| " +
              "Clinical data" + ' ' * (48 - len("Clinical data")))
        print("-" * 173)
        
        for mrn, info in patients.items():
            #create clinical data string inside the loop
            clinical_data_str = ', '.join([f"{key}: {value}" for key, value in info['clinical_data'].items()])
            print(mrn + ' ' * (5 - len(mrn)) + "| " +
                  info['registration_date'] + ' ' * (10 - len(info['registration_date'])) + "| " +
                  info['name'] + ' ' * (10 - len(info['name'])) + "| " +
                  info['dob'] + ' ' * (10 - len(info['dob'])) + "| " +
                  info['gender'] + ' ' * (7 - len(info['gender'])) + "| " +
                  info['address'] + ' ' * (35 - len(info['address'])) + "| " +
                  info['phone'] + ' ' * (13 - len(info['phone'])) + "| " +
                  info['payment_scheme'] + ' ' * (18 - len(info['payment_scheme'])) + "| " +
                  clinical_data_str
                  )
        
        print("-" * 173)

#Function to search a contact
def search_patients():
    search_term = input("Enter MRN or Name to search: ").lower()
    patient_found = False
    
    print("-" * 173)
    print("MRN" + ' ' * (5 - len("MRN")) + "| " +
          "Date" + ' ' * (10 - len("Date")) + "| " +
          "Name" + ' ' * (10 - len("Name")) + "| " +
          "DOB" + ' ' * (10 - len("DOB")) + "| " +
          "Gender" + ' ' * (7 - len("Gender")) + "| " +
          "Address" + ' ' * (35 - len("Address")) + "| " +
          "Phone_Number" + ' ' * (13 - len("Phone_Number")) + "| " +
          "Payment scheme" + ' ' * (18 - len("Payment scheme")) + "| " +
          "Clinical data" + ' ' * (48 - len("Clinical data")))
    print("-" * 173)
    
    for mrn, info in patients.items():
        if (search_term in mrn.lower() or
            search_term in info['name'].lower()
          ):
            
            #clinical data string
            clinical_data_str = ', '.join([f"{key}: {value}" for key, value in info['clinical_data'].items()])
            
            # Print patient data
            print(mrn + ' ' * (5 - len(mrn)) + "| " +
                  info['registration_date'] + ' ' * (10 - len(info['registration_date'])) + "| " +
                  info['name'] + ' ' * (10 - len(info['name'])) + "| " +
                  info['dob'] + ' ' * (10 - len(info['dob'])) + "| " +
                  info['gender'] + ' ' * (7 - len(info['gender'])) + "| " +
                  info['address'] + ' ' * (35 - len(info['address'])) + "| " +
                  info['phone'] + ' ' * (13 - len(info['phone'])) + "| " +
                  info['payment_scheme'] + ' ' * (18 - len(info['payment_scheme'])) + "| " +
                  clinical_data_str)
            
            patient_found = True
    
    if not patient_found:
        print("No patient found with the given search term.")
        
    print("-" * 173)

#Function to edit patients data
def edit_patients():
    mrn = input("Enter MRN of the patient to edit: ")
    
    if mrn in patients:
        print("\nPatient Found:")
        print("-" * 173)
        print("MRN" + ' ' * (5 - len("MRN")) + "| " +
          "Date" + ' ' * (10 - len("Date")) + "| " +
          "Name" + ' ' * (10 - len("Name")) + "| " +
          "DOB" + ' ' * (10 - len("DOB")) + "| " +
          "Gender" + ' ' * (7 - len("Gender")) + "| " +
          "Address" + ' ' * (35 - len("Address")) + "| " +
          "Phone_Number" + ' ' * (13 - len("Phone_Number")) + "| " +
          "Payment scheme" + ' ' * (18 - len("Payment scheme")) + "| " +
          "Clinical data" + ' ' * (48 - len("Clinical data")))
        print("-" * 173)

        # Display the patient data before edit
        info = patients[mrn]
        clinical_data_str = ', '.join([f"{key}: {value}" for key, value in info['clinical_data'].items()])
        
        print(mrn + ' ' * (5 - len(mrn)) + "| " +
              info['registration_date'] + ' ' * (10 - len(info['registration_date'])) + "| " +
              info['name'] + ' ' * (10 - len(info['name'])) + "| " +
              info['dob'] + ' ' * (10 - len(info['dob'])) + "| " +
              info['gender'] + ' ' * (7 - len(info['gender'])) + "| " +
              info['address'] + ' ' * (35 - len(info['address'])) + "| " +
              info['phone'] + ' ' * (15 - len(info['phone'])) + "| " +
              info['payment_scheme'] + ' ' * (18 - len(info['payment_scheme'])) + "| " +
              clinical_data_str)
        print("-" * 173)

        print("\nWhat would you like to edit?")
        print("1. Edit All Data")
        print("2. Edit Specific Data")
        print("3. Cancel and Return to Main Menu")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            # Edit All Data (Sequentially)
            print("\nEditing All Data for MRN:", mrn)
            name = input("Enter New Name: ")
            dob = input("Enter New Date of Birth (DD-MM-YYYY): ")
            
            while True:
                gender = input("Enter New Gender (Man/Woman): ").lower()
                if validate_gender(gender):
                    break
                else:
                    print("Invalid input. Choose Gender (Man/Woman): ")
            
            address = input("Enter New Address: ")
            
            while True:
                phone = input("Enter New Phone Number: ")
                if validate_phone_number(phone):
                    break
                else:
                    print("Invalid number. Enter Phone Number: ")
            
            while True:
                payment_scheme = input("Enter New Payment Scheme (Private Insurance, Public Insurance, Cash): ").lower()
                if validate_payment_scheme(payment_scheme):
                    break
                else:
                    print("Invalid scheme. Enter Payment Scheme: ")
            
            print("Enter New Vital Signs:")
            blood_pressure = input("Blood Pressure (e.g., 120/80): ")
            heart_rate = (int(input("Heart Rate (bpm): ")))
            temperature = (float(input("Temperature (°C): ")))
            respiratory_rate = (int(input("Respiratory Rate (breaths/min): ")))
            oxygen_saturation = (int(input("Oxygen Saturation (%): ")))
            
            patients[mrn] = {
                "registration_date": patients[mrn]['registration_date'],  # the original registration date
                "name": name,
                "dob": dob,
                "gender": gender,
                "address": address,
                "phone": phone,
                "payment_scheme": payment_scheme,
                "clinical_data": {
                    "BP": blood_pressure,
                    "HR": heart_rate,
                    "T": temperature,
                    "RR": respiratory_rate,
                    "SpO2": oxygen_saturation
                }
            }
            print("All data updated successfully!")
        
        elif choice == "2":
            # Edit Specific Data
            print("\nEdit Specific Data:")
            print("1. Name")
            print("2. Date of Birth")
            print("3. Gender")
            print("4. Address")
            print("5. Phone Number")
            print("6. Payment Scheme")
            print("7. Clinical Data")
            print("8. Cancel and Return to Main Menu")
            choice_specific = input("Enter your choice (1-8): ")
            
            if choice_specific == "1":
                patients[mrn]['name'] = input("Enter New Name: ")
                print("Name updated successfully!")
            
            elif choice_specific == "2":
                patients[mrn]['dob'] = input("Enter New Date of Birth (DD-MM-YYYY): ")
                print("DOB updated successfully!")
            
            elif choice_specific == "3":
                while True:
                    gender = input("Enter New Gender (Man/Woman): ").lower()
                    if validate_gender(gender):
                        patients[mrn]['gender'] = gender
                        print("Gender updated successfully!")
                        break
                    else:
                        print("Invalid input. Choose Gender (Man/Woman): ")
            
            elif choice_specific == "4":
                patients[mrn]['address'] = input("Enter New Address: ")
                print("Address updated successfully!")
            
            elif choice_specific == "5":
                while True:
                    phone = input("Enter New Phone Number: ")
                    if validate_phone_number(phone):
                        patients[mrn]['phone'] = phone
                        print("Phone Number updated successfully!")
                        break
                    else:
                        print("Invalid number. Enter Phone Number: ")
            
            elif choice_specific == "6":
                while True:
                    payment_scheme = input("Enter New Payment Scheme (Private Insurance, Public Insurance, Cash): ").lower()
                    if validate_payment_scheme(payment_scheme):
                        patients[mrn]['payment_scheme'] = payment_scheme
                        print("Payment Scheme updated successfully!")
                        break
                    else:
                        print("Invalid scheme. Enter Payment Scheme: ")
            
            elif choice_specific == "7":
                print("Editing Clinical Data:")
                patients[mrn]['clinical_data']['BP'] = input("Blood Pressure (e.g., 120/80): ")
                patients[mrn]['clinical_data']['HR'] = int(input("Heart Rate (bpm): "))
                patients[mrn]['clinical_data']['T'] = float(input("Temperature (°C): "))
                patients[mrn]['clinical_data']['RR'] = int(input("Respiratory Rate (breaths/min): "))
                patients[mrn]['clinical_data']['SpO2'] = int(input("Oxygen Saturation (%): "))
                print("Clinical Data updated successfully!")
            
            elif choice_specific == "8":
                print("Edit cancelled. Returning to main menu.")
                return
            
            else:
                print("Invalid choice.")
        
        elif choice == "3":
            print("Edit cancelled. Returning to main menu.")
            return
        
        else:
            print("Invalid choice.")
    else:
        print("No patient found with this MRN.")


#Function to delete patients data
def delete_patients():
    mrn = input("Enter MRN of the patient to delete: ")
    
    if mrn in patients:
        print("\nPatient found:")
        print("-" * 173)
        
        # Display the patient data before deletion
        info = patients[mrn]
        clinical_data_str = ', '.join([f"{key}: {value}" for key, value in info['clinical_data'].items()])
        
        print(mrn + ' ' * (5 - len(mrn)) + "| " +
              info['registration_date'] + ' ' * (10 - len(info['registration_date'])) + "| " +
              info['name'] + ' ' * (10 - len(info['name'])) + "| " +
              info['dob'] + ' ' * (10 - len(info['dob'])) + "| " +
              info['gender'] + ' ' * (7 - len(info['gender'])) + "| " +
              info['address'] + ' ' * (35 - len(info['address'])) + "| " +
              info['phone'] + ' ' * (15 - len(info['phone'])) + "| " +
              info['payment_scheme'] + ' ' * (18 - len(info['payment_scheme'])) + "| " +
              clinical_data_str)
        
        print("-" * 173)
        
        # Confirm deletion
        confirmation = input("Are you sure you want to delete this patient data? (yes/no): ").lower()
        
        if confirmation == 'yes':
            del patients[mrn]
            print("Patient data successfully deleted.")
        else:
            print("Deletion cancelled.")
            
    else:
        print("No patient found with this MRN.")

#Function to display sort and filter function
def display_patients(patient_list):
    if len(patient_list) == 0:
        print("No patient is listed")
    else: 
        print("-" * 173)
        print("MRN" + ' ' * (5 - len("MRN")) + "| " +
          "Date" + ' ' * (10 - len("Date")) + "| " +
          "Name" + ' ' * (10 - len("Name")) + "| " +
          "DOB" + ' ' * (10 - len("DOB")) + "| " +
          "Gender" + ' ' * (7 - len("Gender")) + "| " +
          "Address" + ' ' * (35 - len("Address")) + "| " +
          "Phone_Number" + ' ' * (13 - len("Phone_Number")) + "| " +
          "Payment scheme" + ' ' * (18 - len("Payment scheme")) + "| " +
          "Clinical data" + ' ' * (48 - len("Clinical data")))
        print("-" * 173)

        for mrn, info in patient_list.items():
            #create clinical data string inside the loop
            clinical_data_str = ', '.join([f"{key}: {value}" for key, value in info['clinical_data'].items()])
            print(mrn + ' ' * (5 - len(mrn)) + "| " +
                  info['registration_date'] + ' ' * (10 - len(info['registration_date'])) + "| " +
                  info['name'] + ' ' * (10 - len(info['name'])) + "| " +
                  info['dob'] + ' ' * (10 - len(info['dob'])) + "| " +
                  info['gender'] + ' ' * (7 - len(info['gender'])) + "| " +
                  info['address'] + ' ' * (35 - len(info['address'])) + "| " +
                  info['phone'] + ' ' * (13 - len(info['phone'])) + "| " +
                  info['payment_scheme'] + ' ' * (18 - len(info['payment_scheme'])) + "| " +
                  clinical_data_str
                  )
        
        print("-" * 173)

#Function to sort patients data
def sort_patients():
    print("\nSort Patients By:")
    print("1. MRN")
    print("2. Registration Date")
    print("3. Name")
    print("4. Date of Birth")
    print("5. Gender")
    print("6. Payment Scheme")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        sorted_data = dict(sorted(patients.items()))  
    elif choice == "2":
        sorted_data = dict(sorted(patients.items(), key=lambda x: datetime.strptime(x[1]['registration_date'], "%d-%m-%Y")))
    elif choice == "3":
        sorted_data = dict(sorted(patients.items(), key=lambda x: x[1]['name'].lower()))
    elif choice == "4":
        sorted_data = dict(sorted(patients.items(), key=lambda x: datetime.strptime(x[1]['dob'], "%d-%m-%Y")))
    elif choice == "5":
        sorted_data = dict(sorted(patients.items(), key=lambda x: x[1]['gender'].lower()))
    elif choice == "6":
        sorted_data = dict(sorted(patients.items(), key=lambda x: x[1]['payment_scheme'].lower()))
    else:
        print("Invalid choice. Returning to main menu.")
        return
    
    display_patients(sorted_data)

#Function to filter patient data
def filter_patients():
    print("\nFilter Patients By:")
    print("1. Gender")
    print("2. Payment Scheme")
    choice = input("Enter your choice (1-2): ")

    filtered_data = {}
    
    if choice == "1":
        gender = input("Enter Gender to filter (man/woman): ").lower()
        filtered_data = {mrn: info for mrn, info in patients.items() if info['gender'].lower() == gender}
        display_patients(filtered_data)
    elif choice == "2":
        scheme = input("Enter Payment Scheme to filter (Private Insurance, Public Insurance, Cash): ").lower()
        filtered_data = {mrn: info for mrn, info in patients.items() if info['payment_scheme'].lower() == scheme}
        display_patients(filtered_data)
    else:
        print("Invalid choice. Returning to main menu.")
        return
    
#Function for treatment options
def treatment_options():
    # MRN and validation
    while True:
        mrn = input("Enter MRN: ")
        if mrn in patients:
            patient = patients[mrn]
            print(f"Patient Found: {patient['name']}, {patient['address']}, DOB: {patient['dob']}")
            break
        else:
            print("Invalid MRN. Please enter a valid one.")
    
    department = choose_department()
    treatments, total_price = choose_treatment()
    print_bill(mrn, patient, department, treatments, total_price)

#Function to choose department
def choose_department():
    departments = [
        "Internal Medicine", "Obstetric", "Surgery", "Pediatrics", 
        "Ophthalmology", "Dermatology", "Ear, Nose and Throat", "Psychiatry"
    ]
    
    while True:
        print("\nChoose a Department:")
        for i, dept in enumerate(departments, start=1):
            print(f"{i}. {dept}")
        
        choice = input("Select a department (Enter number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(departments):
            selected_department = departments[int(choice) - 1]
            print(f"Selected department: {selected_department}")
            return selected_department
        else:
            print("Invalid choice, please select a valid number.")

#function to choose treatment
def choose_treatment():
    treatments = [
        ("Doctor consultation", 100000),
        ("Physical examination", 100000),
        ("Medical procedure", 300000),
        ("Imaging", 200000),
        ("Laboratory examination", 150000)
    ]

    selected_treatments = []
    total_price = 0

    while True:
        print("\nChoose Clinical Management:")
        for i, (treatment, price) in enumerate(treatments, start=1):
            print(f"{i}. {treatment} - {price} IDR")  

        choices = input("Select treatments (e.g., 1,2 for multiple): ").replace(" ", "").split(",")
        
        valid_selection = False  

        for opt in choices:
            if opt.isdigit():
                opt = int(opt)
                if 1 <= opt <= len(treatments):
                    treatment_name, price = treatments[opt - 1]
                    if (treatment_name, price) not in selected_treatments:  
                        selected_treatments.append((treatment_name, price))
                        total_price += price
                        valid_selection = True
                else:
                    print("Invalid choice, please select again.")
                    break  
            else:
                print("Invalid input. Please enter numbers only.")
                break  

        if valid_selection:
            return selected_treatments, total_price  
        show_menu()
       


#billing 
def print_bill(mrn, patient, department, treatments, total_price):
    print("\n----------- Hospital Bill -----------")
    print(f"MRN: {mrn}")
    print(f"Name: {patient['name']}")
    print(f"Address: {patient['address']}")
    print(f"DOB: {patient['dob']}")
    print(f"Department: {department}")
    print(f"Payment Scheme: {patient['payment_scheme']}")
    print("\nTreatments:")
    print("--------------------------------------")
    for treat, price in treatments:
        print(f"{treat.ljust(26)} {price} IDR")
    print("--------------------------------------")
    print(f"Total Bill: {total_price} IDR")
    print("--------------------------------------\n")

#menu
while True:
    choice = show_menu()

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        search_patients()
    elif choice == "4":
        edit_patients()
    elif choice == "5":
        delete_patients()
    elif choice == "6":
        sort_patients()
    elif choice == "7":
        filter_patients()
    elif choice == "8":
        treatment_options()
    elif choice == "9":
        print("Thank you for using the application")
        break
    else:
        print("Invalid choice. Please try again.")
