import json

class SATResults:
    def __init__(self):
        self.data = []

    def insert_data(self, name, address, city, country, pincode, sat_score):
        passed = "Pass" if sat_score > 30 else "Fail"
        candidate_data = {
            "Name": name,
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT Score": sat_score,
            "Passed": passed
        }
        self.data.append(candidate_data)
        print("Record inserted successfully!")

    def view_all_data(self):
        print(json.dumps(self.data, indent=2))

    def get_rank(self, name):
        sorted_data = sorted(self.data, key=lambda x: x["SAT Score"], reverse=True)
        for i, candidate in enumerate(sorted_data, start=1):
            if candidate["Name"] == name:
                return i
        return None

    def update_score(self, name, new_score):
        for candidate in self.data:
            if candidate["Name"] == name:
                candidate["SAT Score"] = new_score
                candidate["Passed"] = "Pass" if new_score > 30 else "Fail"
                print("SAT Score updated successfully!")
                return
        print("Candidate not found!")

    def delete_record(self, name):
        for i, candidate in enumerate(self.data):
            if candidate["Name"] == name:
                del self.data[i]
                print("Record deleted successfully!")
                return
        print("Candidate not found!")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file, indent=2)
        print(f"Record saved to {filename} successfully!")

# Example usage
if __name__ == "__main__":
    sat_system = SATResults()

    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save data to file")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            country = input("Enter Country: ")
            pincode = input("Enter Pincode: ")
            sat_score = int(input("Enter SAT Score: "))
            sat_system.insert_data(name, address, city, country, pincode, sat_score)

        elif choice == "2":
            sat_system.view_all_data()

        elif choice == "3":
            name = input("Enter Name: ")
            rank = sat_system.get_rank(name)
            if rank is not None:
                print(f"{name} is ranked #{rank}")
            else:
                print(f"{name} not found in the data.")

        elif choice == "4":
            name = input("Enter Name: ")
            new_score = int(input("Enter new SAT Score: "))
            sat_system.update_score(name, new_score)

        elif choice == "5":
            name = input("Enter Name to delete: ")
            sat_system.delete_record(name)

        elif choice == "6":
            filename = input("Enter filename to save data (e.g., data.json): ")
            sat_system.save_to_file(filename)

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
