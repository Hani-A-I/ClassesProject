class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()  # Manage doctors
        self.patient_manager = PatientManager()  # Manage patients

    def display_menu(self):
        while True:
            print("\n--- Alberta Hospital Management System ---")
            print("1. Manage Doctors")
            print("2. Manage Patients")
            print("3. Exit")

            option = input("Select an option (1-3): ")

            if option == "1":
                self.display_doctors_menu()
            elif option == "2":
                self.display_patients_menu()
            else:
                print("Invalid option. Please try again.")

    def display_doctors_menu(self):
        while True:
            print("\n--- Doctors Menu ---")
            print("1. View List of Doctors")
            print("2. Search Doctor by ID")
            print("3. Search Doctor by Name")
            print("4. Add New Doctor")
            print("5. Edit Doctor Information")
            print("6. Return to Main Menu")

            option = input("Select an option (1-6): ")

            if option == "1":
                self.doctor_manager.display_doctors_list()
            elif option == "2":
                self.doctor_manager.search_doctor_by_id()
            elif option == "3":
                self.doctor_manager.search_doctor_by_name()
            elif option == "4":
                self.doctor_manager.add_dr_to_file()
            elif option == "5":
                self.doctor_manager.edit_doctor_info()
            elif option == "6":
                break
            else:
                print("Invalid option. Please try again.")

    def display_patients_menu(self):
        while True:
            print("\n--- Patients Menu ---")
            print("1. View List of Patients")
            print("2. Search Patient by ID")
            print("3. Add New Patient")
            print("4. Edit Patient Information")
            print("5. Return to Main Menu")

            option = input("Select an option (1-5): ")

            if option == "1":
                self.patient_manager.display_patients_list()
            elif option == "2":
                self.patient_manager.search_patient_by_Id()
            elif option == "3":
                self.patient_manager.add_patient_to_file()
            elif option == "4":
                self.patient_manager.edit_patient_info_by_id()
            elif option == "5":
                break
            else:
                print("Invalid option. Please try again.")
