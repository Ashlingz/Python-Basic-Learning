import urllib
import requests as req
from datetime import datetime
import priceSub as ps

bot_token = '6106396315:AAEAbZ8kxT3O2ohSln-GUl-6-2FQJbZlL2w'
chat_id = '@ashlingz123'
# chat_id = '861466985'

date = datetime.now().strftime("%d-%m-%Y %H:%M")
html = f"<strong>Order date: ({date})</strong>\n"
html += f"<strong>Sub Total: ({ps.sub_total})</strong>\n"
html += f"<strong>Sub Total: ({ps.sub_total})</strong>\n"
html += f"<strong>Discount Amount: ({ps.discount_amount})</strong>\n"
html += f"<strong>Grand Total:: ({ps.grand_total})</strong>\n"
html += f"<strong>Singly</strong>\n"
html = urllib.parse.quote(html)

r = req.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML')
print(r.text)
