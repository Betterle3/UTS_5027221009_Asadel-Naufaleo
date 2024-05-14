import tkinter as tk
from tkinter import ttk
import grpc
import expense_record_pb2
import expense_record_pb2_grpc

class ExpenseTrackerClient:
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = expense_record_pb2_grpc.ExpenseTrackerStub(channel)

    def get_all_expenses(self):
        request = expense_record_pb2.GetAllExpensesRequest()
        response = self.stub.GetAllExpenses(request)
        return response.expenses

    def create_expense(self, amount, description, date):
        expense = expense_record_pb2.Expense(amount=amount, description=description, date=date)
        request = expense_record_pb2.CreateExpenseRequest(expense=expense)
        response = self.stub.CreateExpense(request)
        return response.expense

    def update_expense(self, expense_id, amount, description, date):
        expense = expense_record_pb2.Expense(id=expense_id, amount=amount, description=description, date=date)
        request = expense_record_pb2.UpdateExpenseRequest(id=expense_id, expense=expense)
        response = self.stub.UpdateExpense(request)
        return response.expense

    def delete_expense(self, expense_id):
        request = expense_record_pb2.DeleteExpenseRequest(id=expense_id)
        response = self.stub.DeleteExpense(request)
        return response.message

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.client = ExpenseTrackerClient()

        self.create_widgets()

    def create_widgets(self):
        self.amount_label = ttk.Label(self.root, text="Amount:")
        self.amount_entry = ttk.Entry(self.root)
        self.amount_label.grid(row=0, column=0, sticky=tk.W)
        self.amount_entry.grid(row=0, column=1)

        self.description_label = ttk.Label(self.root, text="Description:")
        self.description_entry = ttk.Entry(self.root)
        self.description_label.grid(row=1, column=0, sticky=tk.W)
        self.description_entry.grid(row=1, column=1)

        self.date_label = ttk.Label(self.root, text="Date:")
        self.date_entry = ttk.Entry(self.root)
        self.date_label.grid(row=2, column=0, sticky=tk.W)
        self.date_entry.grid(row=2, column=1)

        self.create_button = ttk.Button(self.root, text="Create Expense", command=self.create_expense)
        self.create_button.grid(row=3, columnspan=2)

        self.edit_button = ttk.Button(self.root, text="Edit Expense", command=self.edit_expense)
        self.edit_button.grid(row=5, column=0)

        self.delete_button = ttk.Button(self.root, text="Delete Expense", command=self.delete_expense)
        self.delete_button.grid(row=5, column=1)

        self.expenses_tree = ttk.Treeview(self.root, columns=("Amount", "Description", "Date"))
        self.expenses_tree.heading("#0", text="ID")
        self.expenses_tree.heading("Amount", text="Amount")
        self.expenses_tree.heading("Description", text="Description")
        self.expenses_tree.heading("Date", text="Date")
        self.expenses_tree.grid(row=4, columnspan=2)

        self.refresh_expenses()

    def refresh_expenses(self):
        self.expenses_tree.delete(*self.expenses_tree.get_children())
        expenses = self.client.get_all_expenses()
        for expense in expenses:
            self.expenses_tree.insert("", "end", text=expense.id, values=(expense.amount, expense.description, expense.date))

    def create_expense(self):
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        date = self.date_entry.get()
        self.client.create_expense(amount, description, date)
        self.refresh_expenses()

    def edit_expense(self):
        selected_item = self.expenses_tree.selection()
        if selected_item:
            expense_id = self.expenses_tree.item(selected_item)['text']
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()
            date = self.date_entry.get()
            self.client.update_expense(expense_id, amount, description, date)
            self.refresh_expenses()

    def delete_expense(self):
        selected_item = self.expenses_tree.selection()
        if selected_item:
            expense_id = self.expenses_tree.item(selected_item)['text']
            self.client.delete_expense(expense_id)
            self.refresh_expenses()

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
