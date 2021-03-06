# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from a3m.server.rpc import a3m_pb2 as a3m_dot_server_dot_rpc_dot_a3m__pb2


class TransferStub:
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Submit = channel.unary_unary(
            "/a3m.Transfer/Submit",
            request_serializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.SubmitRequest.SerializeToString,
            response_deserializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.SubmitReply.FromString,
        )
        self.Status = channel.unary_unary(
            "/a3m.Transfer/Status",
            request_serializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.StatusRequest.SerializeToString,
            response_deserializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.StatusReply.FromString,
        )


class TransferServicer:
    """Missing associated documentation comment in .proto file"""

    def Submit(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TransferServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Submit": grpc.unary_unary_rpc_method_handler(
            servicer.Submit,
            request_deserializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.SubmitRequest.FromString,
            response_serializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.SubmitReply.SerializeToString,
        ),
        "Status": grpc.unary_unary_rpc_method_handler(
            servicer.Status,
            request_deserializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.StatusRequest.FromString,
            response_serializer=a3m_dot_server_dot_rpc_dot_a3m__pb2.StatusReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "a3m.Transfer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Transfer:
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Submit(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/a3m.Transfer/Submit",
            a3m_dot_server_dot_rpc_dot_a3m__pb2.SubmitRequest.SerializeToString,
            a3m_dot_server_dot_rpc_dot_a3m__pb2.SubmitReply.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Status(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/a3m.Transfer/Status",
            a3m_dot_server_dot_rpc_dot_a3m__pb2.StatusRequest.SerializeToString,
            a3m_dot_server_dot_rpc_dot_a3m__pb2.StatusReply.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
