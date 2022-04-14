# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ocr_server_pb2 as ocr__server__pb2


class OCRServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImageSync = channel.unary_unary(
                '/OCRServer/ImageSync',
                request_serializer=ocr__server__pb2.Text.SerializeToString,
                response_deserializer=ocr__server__pb2.Text.FromString,
                )
        self.StoreImage = channel.unary_unary(
                '/OCRServer/StoreImage',
                request_serializer=ocr__server__pb2.Image.SerializeToString,
                response_deserializer=ocr__server__pb2.Id.FromString,
                )
        self.GetText = channel.unary_unary(
                '/OCRServer/GetText',
                request_serializer=ocr__server__pb2.Id.SerializeToString,
                response_deserializer=ocr__server__pb2.Text.FromString,
                )


class OCRServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ImageSync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StoreImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OCRServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ImageSync': grpc.unary_unary_rpc_method_handler(
                    servicer.ImageSync,
                    request_deserializer=ocr__server__pb2.Text.FromString,
                    response_serializer=ocr__server__pb2.Text.SerializeToString,
            ),
            'StoreImage': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreImage,
                    request_deserializer=ocr__server__pb2.Image.FromString,
                    response_serializer=ocr__server__pb2.Id.SerializeToString,
            ),
            'GetText': grpc.unary_unary_rpc_method_handler(
                    servicer.GetText,
                    request_deserializer=ocr__server__pb2.Id.FromString,
                    response_serializer=ocr__server__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OCRServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OCRServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ImageSync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OCRServer/ImageSync',
            ocr__server__pb2.Text.SerializeToString,
            ocr__server__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StoreImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OCRServer/StoreImage',
            ocr__server__pb2.Image.SerializeToString,
            ocr__server__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OCRServer/GetText',
            ocr__server__pb2.Id.SerializeToString,
            ocr__server__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)