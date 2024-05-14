# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import expense_record_pb2 as expense__record__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in expense_record_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ExpenseTrackerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllExpenses = channel.unary_unary(
                '/ExpenseTracker.ExpenseTracker/GetAllExpenses',
                request_serializer=expense__record__pb2.GetAllExpensesRequest.SerializeToString,
                response_deserializer=expense__record__pb2.GetAllExpensesResponse.FromString,
                _registered_method=True)
        self.CreateExpense = channel.unary_unary(
                '/ExpenseTracker.ExpenseTracker/CreateExpense',
                request_serializer=expense__record__pb2.CreateExpenseRequest.SerializeToString,
                response_deserializer=expense__record__pb2.CreateExpenseResponse.FromString,
                _registered_method=True)
        self.UpdateExpense = channel.unary_unary(
                '/ExpenseTracker.ExpenseTracker/UpdateExpense',
                request_serializer=expense__record__pb2.UpdateExpenseRequest.SerializeToString,
                response_deserializer=expense__record__pb2.UpdateExpenseResponse.FromString,
                _registered_method=True)
        self.DeleteExpense = channel.unary_unary(
                '/ExpenseTracker.ExpenseTracker/DeleteExpense',
                request_serializer=expense__record__pb2.DeleteExpenseRequest.SerializeToString,
                response_deserializer=expense__record__pb2.DeleteExpenseResponse.FromString,
                _registered_method=True)


class ExpenseTrackerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllExpenses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExpense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExpense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteExpense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExpenseTrackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllExpenses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllExpenses,
                    request_deserializer=expense__record__pb2.GetAllExpensesRequest.FromString,
                    response_serializer=expense__record__pb2.GetAllExpensesResponse.SerializeToString,
            ),
            'CreateExpense': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExpense,
                    request_deserializer=expense__record__pb2.CreateExpenseRequest.FromString,
                    response_serializer=expense__record__pb2.CreateExpenseResponse.SerializeToString,
            ),
            'UpdateExpense': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExpense,
                    request_deserializer=expense__record__pb2.UpdateExpenseRequest.FromString,
                    response_serializer=expense__record__pb2.UpdateExpenseResponse.SerializeToString,
            ),
            'DeleteExpense': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteExpense,
                    request_deserializer=expense__record__pb2.DeleteExpenseRequest.FromString,
                    response_serializer=expense__record__pb2.DeleteExpenseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ExpenseTracker.ExpenseTracker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExpenseTracker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllExpenses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ExpenseTracker.ExpenseTracker/GetAllExpenses',
            expense__record__pb2.GetAllExpensesRequest.SerializeToString,
            expense__record__pb2.GetAllExpensesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateExpense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ExpenseTracker.ExpenseTracker/CreateExpense',
            expense__record__pb2.CreateExpenseRequest.SerializeToString,
            expense__record__pb2.CreateExpenseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateExpense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ExpenseTracker.ExpenseTracker/UpdateExpense',
            expense__record__pb2.UpdateExpenseRequest.SerializeToString,
            expense__record__pb2.UpdateExpenseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteExpense(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ExpenseTracker.ExpenseTracker/DeleteExpense',
            expense__record__pb2.DeleteExpenseRequest.SerializeToString,
            expense__record__pb2.DeleteExpenseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)