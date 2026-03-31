import tkinter as tk
import json
import os

FILE = "expenses.json"
expenses = []


# 🔹 Load data
def load_data():
    global expenses

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            expenses = json.load(f)

        for exp in expenses:
            listbox.insert(tk.END, exp)


# 🔹 Save data
def save_data():
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)


# 🔹 Add expense
def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()

    if amount and category:
        entry = f"₹{amount} - {category}"

        expenses.append(entry)
        listbox.insert(tk.END, entry)

        save_data()

        result_label.config(text="Added!")

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        result_label.config(text="Fill all fields")


# 🔹 Delete expense
def delete_expense():
    selected = listbox.curselection()

    if not selected:
        result_label.config(text="Select item")
        return

    index = selected[0]

    listbox.delete(index)
    expenses.pop(index)

    save_data()
    result_label.config(text="Deleted")


# 🔹 Search
def search_expense():
    keyword = search_entry.get().lower()

    listbox.delete(0, tk.END)

    for exp in expenses:
        if keyword in exp.lower():
            listbox.insert(tk.END, exp)


# 🔹 Show all
def show_all():
    listbox.delete(0, tk.END)

    for exp in expenses:
        listbox.insert(tk.END, exp)


# 🔹 Total by category
def total_by_category():
    keyword = search_entry.get().lower()
    total = 0

    for exp in expenses:
        if keyword in exp.lower():
            amount = float(exp.split(" - ")[0].replace("₹", ""))
            total += amount

    result_label.config(text=f"Total: ₹{total}")


# 🔹 GUI Setup
root = tk.Tk()
root.title("Expense Analyzer")
root.geometry("350x500")

tk.Label(root, text="Expense Analyzer", font=("Arial", 14)).pack(pady=10)

# Inputs
tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_expense).pack(pady=5)

# Search
tk.Label(root, text="Search Category").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search_expense).pack(pady=5)
tk.Button(root, text="Show All", command=show_all).pack()
tk.Button(root, text="Total for Category", command=total_by_category).pack(pady=5)

# Result
result_label = tk.Label(root, text="")
result_label.pack()

# List
tk.Label(root, text="Expenses").pack()
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Load data
load_data()

# Run app
root.mainloop()