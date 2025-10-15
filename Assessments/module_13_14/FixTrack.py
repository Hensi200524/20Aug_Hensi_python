# FixTrack 

orders = []         # List to store all orders
order_id = 1        # Auto-increment ID

# ---------------- Book New Order ----------------
def book_order():
    global order_id
    print("\n--- Book New Repair Order ---")
    name = input("Customer Name: ").strip()
    device = input("Device Type: ").strip()
    issue = input("Issue Description: ").strip()
    date = input("Due Date (DD/MM/YYYY): ").strip()

    if not name or not device or not issue or not date:
        print("All fields are required.")
        return

    order = {
        "id": order_id,
        "name": name,
        "device": device,
        "issue": issue,
        "date": date,
        "status": "Pending",
        "parts": 0,
        "fee": 0
    }
    orders.append(order)
    print(f"Order booked! Order ID: {order_id}")
    order_id += 1


# ---------------- View All Orders ----------------
def view_orders():
    if not orders:
        print("\nNo orders available.")
        return

    print("\n--- All Orders ---")
    for o in orders:
        print(f"\nID: {o['id']}")
        print(f"Customer: {o['name']}")
        print(f"Device: {o['device']}")
        print(f"Issue: {o['issue']}")
        print(f"Due Date: {o['date']}")
        print(f"Status: {o['status']}")


# ---------------- Generate Bill ----------------
def generate_bill():
    if not orders:
        print("\nNo orders found.")
        return

    try:
        oid = int(input("Enter Order ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for o in orders:
        if o["id"] == oid:
            if o["status"] == "Billed":
                print("Bill already generated.")
                return

            try:
                parts = float(input("Parts Cost ₹: "))
                fee = float(input("Repair Fee ₹: "))
            except ValueError:
                print("Invalid amount.")
                return

            dis = input("Apply discount? (y/n): ").lower()
            disc_rate = 0
            if dis == 'y':
                try:
                    disc_rate = float(input("Discount %: "))
                except ValueError:
                    disc_rate = 0

            subtotal = parts + fee
            discount = subtotal * (disc_rate / 100)
            taxable = subtotal - discount
            tax = taxable * 0.18
            total = taxable + tax

            o["parts"] = parts
            o["fee"] = fee
            o["status"] = "Billed"

            print("\n--- Invoice ---")
            print(f"Order ID: {o['id']}")
            print(f"Customer: {o['name']}")
            print(f"Device: {o['device']}")
            print(f"Issue: {o['issue']}")
            print(f"Parts: ₹{parts:.2f}")
            print(f"Repair Fee: ₹{fee:.2f}")
            print(f"Subtotal: ₹{subtotal:.2f}")
            print(f"Discount ({disc_rate}%): -₹{discount:.2f}")
            print(f"Tax (18%): ₹{tax:.2f}")
            print(f"Total: ₹{total:.2f}")
            print("Bill Generated.")
            return

    print("Order not found.")


# ---------------- Menu ----------------
def menu():
    while True:
        print("\n===== FixTrack Menu =====")
        print("1. Book Order")
        print("2. View Orders")
        print("3. Generate Bill")
        print("4. Exit")
        ch = input("Enter choice: ")

        if ch == '1':
            book_order()
        elif ch == '2':
            view_orders()
        elif ch == '3':
            generate_bill()
        elif ch == '4':
            print("Thank you for using FixTrack!")
            break
        else:
            print("Invalid choice.")

# Start Program
menu()
