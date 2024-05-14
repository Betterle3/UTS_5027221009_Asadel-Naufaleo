import sys
import os
import grpc
from concurrent import futures
from bson import ObjectId
import pymongo

# Import generated classes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'client')))
import expense_record_pb2_grpc
import expense_record_pb2

class ExpenseTracker(expense_record_pb2_grpc.ExpenseTrackerServicer):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client['ExpenseDatabase']
        self.collection = self.db['ExpenseRecord']

    # Implementasi metode GetAllExpenses
    def GetAllExpenses(self, request, context):
        records = []
        for doc in self.collection.find():
            record = expense_record_pb2.Expense(
                id=str(doc.get('_id')),
                amount=doc.get('amount', 0),
                description=doc.get('description', ""),
                date=doc.get('date', "")
            )
            records.append(record)
        return expense_record_pb2.GetAllExpensesResponse(expenses=records)

    # Implementasi metode CreateExpense
    def CreateExpense(self, request, context):
        new_record = {
            'amount': request.expense.amount,
            'description': request.expense.description,
            'date': request.expense.date
        }
        result = self.collection.insert_one(new_record)
        if result.inserted_id:
            inserted_record = self.collection.find_one({'_id': result.inserted_id})
            created_record = expense_record_pb2.Expense(
                id=str(inserted_record['_id']),
                amount=inserted_record['amount'],
                description=inserted_record['description'],
                date=inserted_record['date']
            )
            return expense_record_pb2.CreateExpenseResponse(expense=created_record)
        else:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Failed to create record.")
            return expense_record_pb2.CreateExpenseResponse()

    # Implementasi metode UpdateExpense
    def UpdateExpense(self, request, context):
        filter_query = {'_id': ObjectId(request.id)}
        update_query = {
            '$set': {
                'amount': request.expense.amount,
                'description': request.expense.description,
                'date': request.expense.date
            }
        }
        result = self.collection.update_one(filter_query, update_query)
        if result.modified_count > 0:
            return expense_record_pb2.UpdateExpenseResponse(expense=request.expense)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Record not found.")
            return expense_record_pb2.UpdateExpenseResponse()

    # Implementasi metode DeleteExpense
    def DeleteExpense(self, request, context):
        filter_query = {'_id': ObjectId(request.id)}
        result = self.collection.delete_one(filter_query)
        if result.deleted_count > 0:
            return expense_record_pb2.DeleteExpenseResponse(message="Record deleted successfully.")
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Record not found.")
            return expense_record_pb2.DeleteExpenseResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    expense_record_pb2_grpc.add_ExpenseTrackerServicer_to_server(ExpenseTracker(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
