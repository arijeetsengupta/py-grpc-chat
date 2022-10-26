import grpc
import src.utils as utils
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
import src.client.exceptions as client_exceptions

class ChatClient:

    def __init__(self):
        server_host, server_port = utils.get_server_config_from_json()
        self.__channel = grpc.insecure_channel(f'{server_host}:{server_port}')
        self.__stub = chat_pb2_grpc.ChatStub(self.__channel)
        self.__user = None
        self.__is_connected = False

    @property
    def is_connected(self):
        return self.__is_connected

    @property
    def username(self):
        if not self.__is_connected:
            return None
        return self.__user.username

    # @property
    # def user_id(self):
    #     if not self.__is_connected:
    #         return -1
    #     return self.__user.userId

    def connect(self, username):
        response = self.__stub.connect(chat_pb2.ChatUser(username=username))
        self.__user = response
        self.__is_connected = True
        return response

    def disconnect(self):
        if not self.is_connected:
            return True

        self.__stub.disconnect(self.__user)
        self.__user = None
        self.__is_connected = False
        return True

    def subscribe_messages(self):
        if not self.__is_connected:
            raise client_exceptions.NotConnectedError("Error: you have not connected to the chat server!")

        return self.__stub.subscribeMessages(self.__user)

    def send_message(self, message):
        if not self.__is_connected:
            raise client_exceptions.NotConnectedError("Error: you have not connected to the chat server!")
        message.is_broadcast = 1
        return self.__stub.sendMessage(message)

    def subscribe_active_users(self):
        if not self.__is_connected:
            raise client_exceptions.NotConnectedError("Error: you have not connected to the chat server!")
        return self.__stub.subscribeActiveUsers(self.__user)
