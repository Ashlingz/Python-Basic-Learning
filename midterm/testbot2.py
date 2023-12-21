import urllib
import requests as req
from datetime import datetime
import studentist as s
s.Register()
bot_token = '6106396315:AAEAbZ8kxT3O2ohSln-GUl-6-2FQJbZlL2w'
chat_id = '@ashlingz123'
# chat_id = '861466985'



date = datetime.now().strftime("%d-%m-%Y %H:%M")
html = f"<strong>Registed Date: ({date})</strong>\n"
html += '\n'.join([f"Student Name: {s['name']}\nGender: {s['gender']}\nSkill: {s['skill']}" for s in s.student_list])
html += '\n----------------------'
html += '\n----------------------'
html = urllib.parse.quote(html)

r = req.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML')
print(r.text)
