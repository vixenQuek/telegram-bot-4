
import asyncio
import logging
from telethon import events
from telethon.sync import TelegramClient




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                   level=logging.INFO)

# +12762228909 - A1
api_id1 = 6159626
api_hash1 = '26e2bfe87a2f1af6ab133cbee61ba45f'

# +12762228957 - A2
api_id2 = 6807448
api_hash2 = 'e93277f834ca41667276da9c35a37b8f'

# +12762228881 - A3
api_id3 = 6471186
api_hash3 = '3c8e77048664774033c1688e59d46702'

# +6283182513497 - A4
api_id4 = 6204352
api_hash4 = '51e1e01a2baf6418153380b85772aaa1'

# +6283138573419 - A5
api_id5 = 5494449
api_hash5 = 'b4dc7ee478293198dae7410d9460b5a1'


client1 = TelegramClient("+12762228909", api_id1, api_hash1)
client2 = TelegramClient("+12762228957", api_id2, api_hash2)
client3 = TelegramClient("+12762228881", api_id3, api_hash3)
client4 = TelegramClient("+6283182513497", api_id4, api_hash4)
client5 = TelegramClient("+6283138573419", api_id5, api_hash5)




MESSAGE_TO_SENT1 = None
MESSAGE_TO_SENT = None
MESSAGE_TO_SENT2 = None
MESSAGE_TO_SENT3 = None
MESSAGE_TO_SENT4 = None
MESSAGE_TO_SENT5 = None

Timer = None

PATH1 = None
PATH2 = None
PATH3 = None
PATH4 = None
PATH5 = None



CHAT_LIST = []
CHAT_LIST1 = []
CHAT_LIST2 = []
CHAT_LIST3 = []
CHAT_LIST4 = []
CHAT_LIST5 = []

def main():
    client1.start()
    client2.start()
    client3.start()
    client4.start()
    client5.start()

    print("Userbot on!")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message())
    client1.run_until_disconnected()
    client2.run_until_disconnected()
    client3.run_until_disconnected()
    client4.run_until_disconnected()
    client5.run_until_disconnected()


async def send_message():


    global CHAT_LIST, CHAT_LIST1, CHAT_LIST2, CHAT_LIST3, CHAT_LIST4, CHAT_LIST5, MESSAGE_TO_SENT1,MESSAGE_TO_SENT, MESSAGE_TO_SENT2, MESSAGE_TO_SENT3, MESSAGE_TO_SENT4, MESSAGE_TO_SENT5, Timer, PATH1, PATH2, PATH3, PATH4, PATH5
    while True:
        if Timer is None:
            Timer = 30
        print(Timer)
        await asyncio.sleep(Timer)
        for i in CHAT_LIST1:
            if MESSAGE_TO_SENT1 is not None and PATH1 is not None:
                await client1.send_message(entity= i, message= MESSAGE_TO_SENT1, file= PATH1)
            else:
                if MESSAGE_TO_SENT1 is not None:
                    await client1.send_message(i,MESSAGE_TO_SENT1)
                if PATH1 is not None:
                    await client1.send_file(i,PATH1)
        for i in CHAT_LIST2:
            if MESSAGE_TO_SENT2 is not None and PATH2 is not None:
                await client2.send_message(entity= i, message= MESSAGE_TO_SENT2, file= PATH2)
            else:
                if MESSAGE_TO_SENT2 is not None:
                    await client2.send_message(i,MESSAGE_TO_SENT2)
                if PATH2 is not None:
                    await client2.send_file(i,PATH2)
        for i in CHAT_LIST3:
            if MESSAGE_TO_SENT3 is not None and PATH3 is not None:
                await client3.send_message(entity= i, message= MESSAGE_TO_SENT3, file= PATH3)
            else:
                if MESSAGE_TO_SENT3 is not None:
                    await client3.send_message(i,MESSAGE_TO_SENT3)
                if PATH3 is not None:
                    await client3.send_file(i,PATH3)
        for i in CHAT_LIST4:
            if MESSAGE_TO_SENT4 is not None and PATH4 is not None:
                await client4.send_message(entity= i, message= MESSAGE_TO_SENT4, file= PATH4)
            else:
                if MESSAGE_TO_SENT4 is not None:
                    await client4.send_message(i,MESSAGE_TO_SENT4)
                if PATH4 is not None:
                    await client4.send_file(i,PATH4)
        for i in CHAT_LIST5:
            if MESSAGE_TO_SENT5 is not None and PATH5 is not None:
                await client5.send_message(entity= i, message= MESSAGE_TO_SENT5, file= PATH5)
            else:
                if MESSAGE_TO_SENT5 is not None:
                    await client5.send_message(i,MESSAGE_TO_SENT5)
                if PATH5 is not None:
                    await client5.send_file(i,PATH5)                






@client1.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST1, MESSAGE_TO_SENT1, Timer, PATH1
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            if replyed_to.media is not None:
                PATH1 = await client1.download_media(replyed_to.media)
                await client1.send_message(entity='me', message = f'{PATH1} is set as message')
            MESSAGE_TO_SENT1 = replyed_to.message
            if MESSAGE_TO_SENT1 is not None:
                await client1.send_message(entity='me', message = f'{MESSAGE_TO_SENT1} is set as message')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client1.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST1.append(chat_title)
            await client1.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client1.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST1.remove(chat_title)
            await client1.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client1.send_message(entity='me', message = f'This is the list {CHAT_LIST1}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client1.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client1.send_message('me', f'reply to an number')



@client2.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST2, MESSAGE_TO_SENT2, Timer, PATH2
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            if replyed_to.media is not None:
                PATH2 = await client2.download_media(replyed_to.media)
                await client2.send_message(entity='me', message = f'{PATH2} is set as file')
            MESSAGE_TO_SENT2 = replyed_to.message
            if MESSAGE_TO_SENT2 is not None:
                await client2.send_message(entity='me', message = f'{MESSAGE_TO_SENT2} is set as message')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client2.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST2.append(chat_title)
            await client2.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client2.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST2.remove(chat_title)
            await client2.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client2.send_message(entity='me', message = f'This is the list {CHAT_LIST2}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client2.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client2.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client2.send_message('me', f'reply to an number')




@client3.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST3, MESSAGE_TO_SENT3, Timer, PATH3
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            if replyed_to.media is not None:
                PATH3 = await client3.download_media(replyed_to.media)
                await client3.send_message(entity='me', message = f'{PATH3} is set as file')
            MESSAGE_TO_SENT3 = replyed_to.message
            if MESSAGE_TO_SENT3 is not None:
                await client3.send_message(entity='me', message = f'{MESSAGE_TO_SENT3} is set as message')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client3.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST3.append(chat_title)
            await client3.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client3.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST3.remove(chat_title)
            await client3.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client3.send_message(entity='me', message = f'This is the list {CHAT_LIST3}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client3.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client3.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client3.send_message('me', f'reply to an number')



@client4.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST4, MESSAGE_TO_SENT4, Timer,PATH4
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            if replyed_to.media is not None:
                PATH4 = await client4.download_media(replyed_to.media)
                await client4.send_message(entity='me', message = f'{PATH4} is set as file')
            MESSAGE_TO_SENT4 = replyed_to.message
            if MESSAGE_TO_SENT4 is not None:
                await client4.send_message(entity='me', message = f'{MESSAGE_TO_SENT4} is set as message')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client4.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST4.append(chat_title)
            await client4.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client4.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST4.remove(chat_title)
            await client4.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client4.send_message(entity='me', message = f'This is the list {CHAT_LIST4}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client4.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client4.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client4.send_message('me', f'reply to an number')



@client5.on(events.NewMessage(chats='me'))
async def set_game(event):
    global CHAT_LIST5, MESSAGE_TO_SENT5, Timer, PATH5
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setmessage': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            if replyed_to.media is not None:
                PATH5 = await client5.download_media(replyed_to.media)
                await client5.send_message(entity='me', message = f'{PATH5} is set as file')
            MESSAGE_TO_SENT5 = replyed_to.message
            if MESSAGE_TO_SENT5 is not None:
                await client5.send_message(entity='me', message = f'{MESSAGE_TO_SENT5} is set as message')
    elif my_message == '/addchat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client5.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST5.append(chat_title)
            await client5.send_message(entity='me', message = f'{chat_title} is added to list')
    elif my_message == '/removechat': # Check if the message is '/setgame'
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            chat_id = replyed_to.fwd_from.saved_from_peer
            chat_id_entity = await client5.get_entity(chat_id)
            chat_title = chat_id_entity.title
            CHAT_LIST5.remove(chat_title)
            await client5.send_message(entity='me', message = f'{chat_title} is remove from list')


    elif my_message == '/showlist': # Check if the message is '/setgame'
        await client5.send_message(entity='me', message = f'This is the list {CHAT_LIST5}')
    
    elif my_message == '/settimer': # Check if the message is '/setgame'
        print('asdfj')
        get_message = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_message is not None: # Work if there is any replied to message 
            replyed_to = await client5.get_messages('me', ids=get_message.reply_to_msg_id)
            message = replyed_to.message
            if message.isdigit():
                Timer = int(message)
                await client5.send_message('me', f'Timer is set for every {Timer} seconds')
            else:
                await client5.send_message('me', f'reply to an number')



if __name__ == "__main__":
    main()


