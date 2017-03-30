import itchat

itchat.auto_login()

# itchat.send('Hello, filehelper', toUserName='filehelper')
SINCERE_WISH = u'祝%s新年快乐！'
friendsList = itchat.get_friends(update=True)[1:]
for friend in friendsList:
    print(SINCERE_WISH % (friend['DisplayName']
                          or friend['NickName']), friend['UserName'])
