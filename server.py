import grpc
import src.server.chat_pb2_grpc as chat_pb2_grpc
import src.utils as utils

from src.server.chat_service import ChatService
from concurrent import futures

def main():
    service = ChatService()

    server_host, server_port = utils.get_server_config_from_json()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))  # create a gRPC server
    chat_pb2_grpc.add_ChatServicer_to_server(service, server)  # register the server to gRPC
    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(server_port))
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        service.stop_connection = True


if __name__ == '__main__':
    main()
