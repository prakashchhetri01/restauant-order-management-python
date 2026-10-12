import csv
import datetime   #for current date and time in order

PIZZA_PRICES = {
                 "Pepperoni": 9.99,
                 "Veggie": 5.99
                                     }   #Pizza prices with two options

orders = []      #empty list to store orders

ORDER_FILE = "prakash.txt"  #to store orders in files for search order

def load_orders():   #def function to load orders from files
    global orders    #global variable to access orders
    orders = []
    try:
        with open(ORDER_FILE, "r", newline="", encoding="utf-8") as file:
            for parts in csv.reader(file):
                if len(parts) == 8:
                    order = {                      #create order dictionary with length 8
                        "Order number": int(parts[0]),
                        "Customer name": parts[1],
                        "Customer email": parts[2],
                        "Phone number": parts[3],
                        "Order date": parts[4],
                        "Menu item": parts[5],
                        "Total amount": float(parts[6]),
                        "Payment status": parts[7] == "True"
                    }
                    orders.append(order)    #to add order list
    except FileNotFoundError:
        pass             #pass if file doesn't exit


def save_orders():  #def to save orders
    with open(ORDER_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for order in orders:
            writer.writerow([order["Order number"], order["Customer name"],
                             order["Customer email"], order["Phone number"],
                             order["Order date"], order["Menu item"],
                             order["Total amount"], order["Payment status"]])

#def to add an order
def add_order(order_number, customer_name, customer_email, phone_number,
              order_date, menu_item, total_amount, payment_status):
    order = {         #new dictionary for new orders from customer
        "Order number": order_number,
        "Customer name": customer_name,
        "Customer email": customer_email,
        "Phone number": phone_number,
        "Order date": order_date,
        "Menu item": menu_item,
        "Total amount": total_amount,
        "Payment status": payment_status
                                         }
    orders.append(order)   #add to order list
    save_orders()
    return order


def delete_order(): #def to delete an order from previous saved list
    try:
        order_number = int(input("Enter Order number to delete: "))
        for i, order in enumerate(orders):
            if order["Order number"] == order_number:
                orders.pop(i)     #delete order from list
                save_orders()     #update order from list
                print(f"Order number {order_number} deleted successfully.")
                return
        print(f"No order found with Order number {order_number}.")
    except ValueError:   #to execute invalid input
        print("Please enter a valid order number.")


def find_orders():  #def to find or search orders from list
    find_term = input("Enter customer name, email, or phone number to find: ").lower().strip()
    found = False
    print("\nfind Results:")
    for order in orders:   #to check every orders
        if (find_term in order["Customer name"].lower() or
                find_term in order["Customer email"].lower() or
                find_term in order["Phone number"]):
            #to display matching order
            print("\nOrder Details:")
            print(f"Order number: {order['Order number']}")
            print(f"Customer Name: {order['Customer name']}")
            print(f"Email: {order['Customer email']}")
            print(f"Phone: {order['Phone number']}")
            print(f"Date: {order['Order date']}")
            print(f"Items: {order['Menu item']}")
            print(f"Total Amount: £{order['Total amount']:.2f}")
            print(f"Payment Status: {'Completed' if order['Payment status'] else 'Pending'}")
            print("-" * 30)
            found = True
    if not found:
        print("No matching orders found.")


def order_update():   #def to update an order
    find_term = input("Enter customer name, email, or phone number to search: ").lower().strip()
    results = []
    for order in orders:
        if (find_term in order["Customer name"].lower() or
                find_term in order["Customer email"].lower() or
                find_term in order["Phone number"]):
            results.append(order)

    if not results:    # to handle no matches
        print("No matching orders found.")
        return

    print("\nfind Results:")
    for i, order in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Order number: {order['Order number']}")
        print(f"Customer Name: {order['Customer name']}")
        print(f"Email: {order['Customer email']}")
        print(f"Phone: {order['Phone number']}")
        print(f"Date: {order['Order date']}")
        print(f"Items: {order['Menu item']}")
        print(f"Total Amount: £{order['Total amount']:.2f}")
        print(f"Payment Status: {'Completed' if order['Payment status'] else 'Pending'}")
        print("-" * 30)

    while True:   #to update selected order
        try:
            choice = int(input(f"Enter result number (1-{len(results)}) to update, or 0 to cancel: "))
            if choice == 0:
                print("Update cancelled.")
                return
            if 1 <= choice <= len(results):
                break
            print(f"Please enter a number between 1 and {len(results)}, or 0 to cancel.")
        except ValueError:
            print("Please enter a valid number.")

    selected_order = results[choice - 1]
    print("\nWhat to update?")   #to update field character
    print("1. Customer name")
    print("2. Customer email")
    print("3. Phone number")
    print("4. Pizza type and quantity")
    print("5. Payment status")

    field_choice = input("Enter choice (1-5): ").strip()

    if field_choice == "1":
        new_name = input("Enter new customer name: ").strip()
        if new_name:
            selected_order["Customer name"] = new_name
        else:
            print("Name cannot be blank. Update skipped.")

    elif field_choice == "2":
        new_email = input("Enter new customer email: ").strip()
        if new_email:
            selected_order["Customer email"] = new_email

    elif field_choice == "3":
        while True:
            new_phone = input("Enter new phone number (10 digits): ").strip()
            if new_phone.isdigit() and len(new_phone) == 10:
                selected_order["Phone number"] = new_phone
                break
            print("Please enter a valid 10-digit phone number.")

    elif field_choice == "4":
        print("\nAvailable Pizzas:")
        for item, price in PIZZA_PRICES.items():
            print(f"{item}: £{price:.2f}")
        while True:
            pizza_choice = input("Enter pizza type (Pepperoni/Veggie): ").strip().title()
            if pizza_choice in PIZZA_PRICES:
                break
            print("Please choose a valid pizza type.")
        while True:
            try:
                pizza_count = int(input("How many pizzas? (1 or more): "))
                if pizza_count >= 1:
                    break
                print("Please enter a number 1 or greater!")
            except ValueError:
                print("Enter a valid number!")
        selected_order["Menu item"] = f"{pizza_count} {pizza_choice} pizza(s)"
        selected_order["Total amount"] = pizza_count * PIZZA_PRICES[pizza_choice]

    elif field_choice == "5":
        while True:     #update payment pending
            payment_choice = input("Payment done? (yes/no): ").strip().lower()
            if payment_choice in ["yes", "no"]:
                selected_order["Payment status"] = payment_choice == "yes"
                break
            print("Please enter 'yes' or 'no' only!")

    else:
        print("Invalid choice. Update skipped.")
        return

    save_orders()    #save updated orders from list
    print("Order updated successfully.")


def display_all_orders():  #def to display all orders
    if not orders:      # to handle empty orders
        print("\nNo orders found in the database.")
        return
    print("\n All orders ")
    for order in orders:    # to show each order from list
        print("\nOrder Details:")
        print(f"Order number: {order['Order number']}")
        print(f"Customer Name: {order['Customer name']}")
        print(f"Email: {order['Customer email']}")
        print(f"Phone: {order['Phone number']}")
        print(f"Date: {order['Order date']}")
        print(f"Items: {order['Menu item']}")
        print(f"Total Amount: £{order['Total amount']:.2f}")
        print(f"Payment Status: {'Completed' if order['Payment status'] else 'Pending'}")
        print("-" * 30)


def place_order():    #def to place an order
    print("\nWelcome to Da-Sandro Pizzeria Ristorante 🍕🍴!")
    customer_name = input("Enter your name: ").strip()
    while not customer_name:
        print("Name cannot be empty!")
        customer_name = input("Enter your name: ").strip()

    while True:
        customer_email = input("Enter your email: ").strip()
        if "@" in customer_email and "." in customer_email:
            break
        print("Please enter a valid email containing @ and .")

    while True:
        phone_number = input("Enter your phone number (10 digits): ").strip()
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        print("Please enter a valid 10-digit phone number.")

    print("\nAvailable Pizzas:")    #display menu item
    for item, price in PIZZA_PRICES.items():
        print(f"{item}: £{price:.2f}")

    while True:
        pizza_choice = input("Enter pizza type (Pepperoni/Veggie): ").strip().title()
        if pizza_choice in PIZZA_PRICES:
            break
        print("Please choose a valid pizza type.")

    while True:
        try:
            pizza_count = int(input("How many pizzas do you want to order? (1 or more): "))
            if pizza_count >= 1:
                break
            print("Please enter a number 1 or greater!")
        except ValueError:
            print("Enter a valid number!")

    total_amount = pizza_count * PIZZA_PRICES[pizza_choice] #calculation of total price

    while True:
        payment_choice = input("Payment done? (yes/no): ").strip().lower()
        if payment_choice in ["yes", "no"]:
            payment_status = payment_choice == "yes"
            break
        print("Please enter 'yes' or 'no' only!")

    order_number = max((order["Order number"] for order in orders), default=1000) + 1
    order_date = datetime.date.today()
    menu_item = f"{pizza_count} {pizza_choice} pizza(s)"

    order = add_order(order_number, customer_name, customer_email,
                      phone_number, order_date, menu_item,
                      total_amount, payment_status)

    print("\n***** Order Summary *****")     #summary display
    print(f"Order number: {order['Order number']}")
    print(f"Customer Name: {order['Customer name']}")
    print(f"Email: {order['Customer email']}")
    print(f"Phone: {order['Phone number']}")
    print(f"Date: {order['Order date']}")
    print(f"Items: {order['Menu item']}")
    print(f"Total Amount: £{order['Total amount']:.2f}")
    print(f"Payment Status: {'Completed' if order['Payment status'] else 'Pending'}")
    print("Order placed successfully! Thank you! Visit again 🙏😊")


def main():
    load_orders()   #to start and load orders
    while True:
        print("\n==^^==Welcome to Da-Sandro Pizzeria Ristorante ==^^==")
        print("1. Place an order")
        print("2. View all orders")
        print("3. Find orders")
        print("4. Update an order")
        print("5. Delete an order")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip() #choices to display

        if choice == "1":
            place_order()
        elif choice == "2":
            display_all_orders()
        elif choice == "3":
            find_orders()
        elif choice == "4":
            order_update()
        elif choice == "5":
            delete_order()
        elif choice == "6":
            print("Thank you for visiting us🙏 See You Again😊!")
            break       #exit the program
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
