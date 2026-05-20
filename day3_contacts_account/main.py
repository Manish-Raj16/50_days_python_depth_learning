import csv
import os

FILENAME = "contacts.csv"


if not os.path.exists(FILENAME):

    with open(FILENAME, mode="w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["Name", "Email", "Phone"])


def add_contact():

    print("\n===== ADD CONTACT =====\n")

    name = input("Enter Name : ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["Name"].lower() == name.lower():

                print("\nContact already exists.\n")
                return

    with open(FILENAME, mode="a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([name, email, phone])

    print("\nContact added successfully.\n")


def view_contacts():

    print("\n===== CONTACT LIST =====\n")

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as f:

        reader = csv.reader(f)

        rows = list(reader)

        if len(rows) <= 1:

            print("No contacts found.\n")
            return

        for row in rows[1:]:

            print(f"Name  : {row[0]}")
            print(f"Email : {row[1]}")
            print(f"Phone : {row[2]}")
            print("------------------------")


def search_contact():

    print("\n===== SEARCH CONTACT =====\n")

    search_name = input("Enter name to search: ").strip().lower()

    found = False

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["Name"].lower() == search_name:

                print("\nContact Found:\n")

                print("Name  :", row["Name"])
                print("Email :", row["Email"])
                print("Phone :", row["Phone"])

                found = True
                break

    if not found:

        print("\nContact not found.\n")


def update_contact():

    print("\n===== UPDATE CONTACT =====\n")

    update_name = input("Enter contact name to update: ").strip().lower()

    rows = []

    found = False

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["Name"].lower() == update_name:

                print("\nEnter new details:\n")

                row["Name"] = input("New Name : ").strip()
                row["Email"] = input("New Email: ").strip()
                row["Phone"] = input("New Phone: ").strip()

                found = True

            rows.append(row)

    if found:

        with open(FILENAME, mode="w", newline="", encoding="utf-8") as f:

            fieldnames = ["Name", "Email", "Phone"]

            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)

        print("\nContact updated successfully.\n")

    else:

        print("\nContact not found.\n")


def delete_contact():

    print("\n===== DELETE CONTACT =====\n")

    delete_name = input("Enter name to delete: ").strip().lower()

    rows = []

    found = False

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["Name"].lower() != delete_name:

                rows.append(row)

            else:

                found = True

    if found:

        with open(FILENAME, mode="w", newline="", encoding="utf-8") as f:

            fieldnames = ["Name", "Email", "Phone"]

            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)

        print("\nContact deleted successfully.\n")

    else:

        print("\nContact not found.\n")


def main():

    while True:

        print("\n========== CONTACT BOOK ==========")

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_contact()

        elif choice == "2":

            view_contacts()

        elif choice == "3":

            search_contact()

        elif choice == "4":

            update_contact()

        elif choice == "5":

            delete_contact()

        elif choice == "6":

            print("\nExiting Contact Book...\n")
            break

        else:

            print("\nInvalid choice.\n")


main()