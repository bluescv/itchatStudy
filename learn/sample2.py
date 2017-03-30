import itchat, time
import json

itchat.auto_login(True)

chatroomList = itchat.get_chatrooms(update=True)[1:]
for chatroom in chatroomList:
    # json_chatroom = json.loads(chatroom)
    print(chatroom.NickName)
    if chatroom.NickName == 'Fantastic Four':
        print("got ya")
        itchat.send("testMessage",chatroom['NickName'])
