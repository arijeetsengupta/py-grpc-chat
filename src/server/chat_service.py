import logging
import random
import json
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
from hashlib import md5


class ChatService(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        super(ChatService, self).__init__()
        self.chats = []
        self.users = {}
        self.stop_connection = False

    def register(self, request, context):
        print("server- in register user")
        filename = "users.json"
        with open(filename, 'r+') as file:
            file_data = json.load(file)
        new_data = {
            "username": request.username,
            "password": request.password
        }
        for usr_dtls in file_data["users"]:
            if usr_dtls["username"] == request.username:
                return chat_pb2.ServerResponse(response="Username already exists")
        file_data["users"].append(new_data)
        with open("users.json", "w") as outfile:
            json.dump(file_data, outfile)
        return chat_pb2.ServerResponse(response="Registration successful")

    def login(self, request, context):
        user_id = request.username
        password = request.password
        with open('users.json') as json_file:
            data = json.load(json_file)["users"]
            for entry in data:
                # print(entry)
                if entry["username"] == user_id and entry["password"] != password:
                    return chat_pb2.ServerResponse(response="Incorrect password")
                elif entry["username"] == user_id and entry["password"] == password:
                    return chat_pb2.ServerResponse(response="Login successful")
            return chat_pb2.ServerResponse(response="User does not exist")

    def connect(self, request, context):
        user_id = request.username
        self.users[user_id] = request.username
        return chat_pb2.ChatUserConnected(username=request.username, userId=user_id)

    def disconnect(self, request, context):
        del self.users[request.userId]
        return chat_pb2.ChatUserDisconnect(isDisconnected=True)

    def sendMessage(self, request, context):
        self.chats.append(request)
        return chat_pb2.ServerResponse(
            response="Server recieved message [{}] from [{}] to [{}]".format(
                request.message, request.userId, request.recipient))

    def subscribeMessages(self, request, context):
        current_user_id = request.userId
        last_seen_message_index = 0
        while not self.stop_connection and self.__is_user_still_connected(current_user_id):
            while len(self.chats) > last_seen_message_index:
                message = self.chats[last_seen_message_index]
                last_seen_message_index += 1
                if message.userId != current_user_id:
                    yield message

    def __is_user_still_connected(self, user_id):
        return self.users.get(user_id, None) is not None

    def subscribeActiveUsers(self, request, context):
        current_hash = ""
        current_user_id = request.userId
        while not self.stop_connection and self.__is_user_still_connected(current_user_id):
            json_users = json.dumps(self.users)
            md5_hash = md5(bytes(json_users, 'utf-8')).hexdigest()
            if current_hash != md5_hash:
                current_hash = md5_hash
                for user_id, username in self.users.items():
                    if user_id != current_user_id:
                        yield chat_pb2.ChatActiveUser(username=username,
                                                      userId=user_id,
                                                      currentHash=current_hash)
