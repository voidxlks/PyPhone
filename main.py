# PyPhone - main.py

import time

# ------------------ Core System ------------------ #

class PyPhone:
    def __init__(self):
        self.contacts = {"Mom": "123-456-7890", "Friend": "987-654-3210"}
        self.messages = []
        self.running = True

    def boot(self):
        print("Booting PyPhone...")
        time.sleep(1)
        print("System Ready!\n")

    def home_screen(self):
        while self.running:
            print("\nPyPhone Home")
            print("1. Contacts")
            print("2. Messages")
            print("3. Calculator")
            print("4. Settings")
            print("5. Power Off")

            choice = input("Select an app: ")

            if choice == "1":
                self.contacts_app()
            elif choice == "2":
                self.messages_app()
            elif choice == "3":
                self.calculator_app()
            elif choice == "4":
                self.settings_app()
            elif choice == "5":
                self.power_off()
            else:
                print("Invalid choice")

    # ------------------ Apps ------------------ #

    def contacts_app(self):
        print("\nContacts")
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

        add = input("Add new contact? (y/n): ")
        if add.lower() == "y":
            name = input("Name: ")
            number = input("Number: ")
            self.contacts[name] = number
            print("Contact added")

    def messages_app(self):
        print("\nMessages")
        if not self.messages:
            print("No messages yet.")
        else:
            for msg in self.messages:
                print(f"To {msg['to']}: {msg['text']}")

        send = input("Send message? (y/n): ")
        if send.lower() == "y":
            to = input("To: ")
            text = input("Message: ")
            self.messages.append({"to": to, "text": text})
            print("Message sent")

    def calculator_app(self):
        print("\nCalculator")
        try:
            expr = input("Enter calculation (e.g. 5 + 3): ")
            result = eval(expr)
            print(f"Result: {result}")
        except:
            print("Invalid calculation")

    def settings_app(self):
        print("\nSettings")
        print("1. Clear Messages")
        print("2. Reset Contacts")
        print("3. Back")

        choice = input("Choose: ")
        if choice == "1":
            self.messages.clear()
            print("Messages cleared")
        elif choice == "2":
            self.contacts = {}
            print("Contacts reset")

    # ------------------ System ------------------ #

    def power_off(self):
        print("Shutting down...")
        time.sleep(1)
        self.running = False


# ------------------ Run ------------------ #

if __name__ == "__main__":
    phone = PyPhone()
    phone.boot()
    phone.home_screen()
