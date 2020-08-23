# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app.grpc_template import route_pb2 as app_dot_grpc__template_dot_route__pb2


class UpdateServerRouteStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCloudConfig = channel.unary_unary(
                '/server_route.UpdateServerRoute/GetCloudConfig',
                request_serializer=app_dot_grpc__template_dot_route__pb2.Empty.SerializeToString,
                response_deserializer=app_dot_grpc__template_dot_route__pb2.Str.FromString,
                )
        self.InitHubAccount = channel.unary_unary(
                '/server_route.UpdateServerRoute/InitHubAccount',
                request_serializer=app_dot_grpc__template_dot_route__pb2.AccountRequest.SerializeToString,
                response_deserializer=app_dot_grpc__template_dot_route__pb2.AccountResponse.FromString,
                )
        self.GetAppStatus = channel.unary_unary(
                '/server_route.UpdateServerRoute/GetAppStatus',
                request_serializer=app_dot_grpc__template_dot_route__pb2.ReleaseRequest.SerializeToString,
                response_deserializer=app_dot_grpc__template_dot_route__pb2.ReleaseResponse.FromString,
                )
        self.GetDownloadInfo = channel.unary_unary(
                '/server_route.UpdateServerRoute/GetDownloadInfo',
                request_serializer=app_dot_grpc__template_dot_route__pb2.DownloadRequest.SerializeToString,
                response_deserializer=app_dot_grpc__template_dot_route__pb2.DownloadInfo.FromString,
                )


class UpdateServerRouteServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCloudConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitHubAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAppStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDownloadInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpdateServerRouteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCloudConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCloudConfig,
                    request_deserializer=app_dot_grpc__template_dot_route__pb2.Empty.FromString,
                    response_serializer=app_dot_grpc__template_dot_route__pb2.Str.SerializeToString,
            ),
            'InitHubAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.InitHubAccount,
                    request_deserializer=app_dot_grpc__template_dot_route__pb2.AccountRequest.FromString,
                    response_serializer=app_dot_grpc__template_dot_route__pb2.AccountResponse.SerializeToString,
            ),
            'GetAppStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAppStatus,
                    request_deserializer=app_dot_grpc__template_dot_route__pb2.ReleaseRequest.FromString,
                    response_serializer=app_dot_grpc__template_dot_route__pb2.ReleaseResponse.SerializeToString,
            ),
            'GetDownloadInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDownloadInfo,
                    request_deserializer=app_dot_grpc__template_dot_route__pb2.DownloadRequest.FromString,
                    response_serializer=app_dot_grpc__template_dot_route__pb2.DownloadInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'server_route.UpdateServerRoute', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UpdateServerRoute(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCloudConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/server_route.UpdateServerRoute/GetCloudConfig',
            app_dot_grpc__template_dot_route__pb2.Empty.SerializeToString,
            app_dot_grpc__template_dot_route__pb2.Str.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitHubAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/server_route.UpdateServerRoute/InitHubAccount',
            app_dot_grpc__template_dot_route__pb2.AccountRequest.SerializeToString,
            app_dot_grpc__template_dot_route__pb2.AccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAppStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/server_route.UpdateServerRoute/GetAppStatus',
            app_dot_grpc__template_dot_route__pb2.ReleaseRequest.SerializeToString,
            app_dot_grpc__template_dot_route__pb2.ReleaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDownloadInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/server_route.UpdateServerRoute/GetDownloadInfo',
            app_dot_grpc__template_dot_route__pb2.DownloadRequest.SerializeToString,
            app_dot_grpc__template_dot_route__pb2.DownloadInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
