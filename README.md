# Zabbix → MAX Alertscripts

Send Zabbix alerts to MAX via HTTP API.

Replacement for Telegram notifications in restricted environments.

---

##  Quick Start

bash pip install -r requirements.txt 

1. Copy scripts to:
      /usr/lib/zabbix/alertscripts   

2. Make them executable:
   bash    chmod +x /usr/lib/zabbix/alertscripts/*.py    

3. Set bot token:
   ini    [Service]    Environment="MAX_BOT_TOKEN=YOUR_TOKEN"    

4. Restart Zabbix:
   bash    sudo systemctl daemon-reexec    sudo systemctl daemon-reload    sudo systemctl restart zabbix-server    

5. Get your chat_id:
   bash    export MAX_BOT_TOKEN=YOUR_TOKEN    ./get_user_id.py    

6. Configure Zabbix Media type:
      {ALERT.SENDTO}    {ALERT.SUBJECT}    {ALERT.MESSAGE}   

---

##  Requirements

- Python 3.6+
- requests

---

##  Files

- get_user_id.py — fetches updates to obtain chat_id
- zabbix_max_http.py — sends alerts to MAX

---

##  Zabbix Setup

- Type: Script  
- Script name: zabbix_max_http.py  

User media:
- Send to: chat_id

---

##  Test

bash export MAX_BOT_TOKEN=YOUR_TOKEN  ./zabbix_max_http.py 123456789 "Test subject" "Test message" 

---

##  Errors

- MAX_BOT_TOKEN is not set
- chat_id must be integer
- MAX API error

---

##  Notes

- Uses MAX HTTP API
- No Telegram dependency
- Minimal and dependency-light

---

## 📄 License

MI
