# Zabbix → MAX Alertscripts

Simple Python scripts to send Zabbix alerts to MAX (https://max.ru) via HTTP API.

Useful in environments where Telegram or other messaging platforms are restricted or unavailable.

---

##  Contents

### 1. get_user_id.py
Script to retrieve chat_id using MAX API.

Used once to identify your user/chat ID.

---

### 2. zabbix_max_http.py
Main script for sending alerts from Zabbix to MAX.

Designed to be used as a Zabbix AlertScript.

---

## Installation

Place scripts into:

/usr/lib/zabbix/alertscripts

Make them executable:

chmod +x /usr/lib/zabbix/alertscripts/*.py

---

## Token Configuration

Set your bot token via environment variable MAX_BOT_TOKEN.

Example for systemd:

[Service] Environment="MAX_BOT_TOKEN=YOUR_TOKEN"

Apply changes:

sudo systemctl daemon-reexec sudo systemctl daemon-reload sudo systemctl restart zabbix-server

Verify:

sudo systemctl show zabbix-server --property=Environment

---

## Get chat_id

Run

export MAX_BOT_TOKEN=YOUR_TOKEN ./get_user_id.py

The script will return JSON with updates. Find your chat_id there.

---

## Zabbix Configuration

1. Go to:
      Administration → Media types   

2. Create new Media type:
   - Type: Script
   - Script name: zabbix_max_http.py

3. Parameters:
      {ALERT.SENDTO}    {ALERT.SUBJECT}    {ALERT.MESSAGE}   

---

## User Setup

1. Go to:
      Administration → Users   

2. Add Media:
   - Type: MAX (created above)
   - Send to: chat_id

---

## Manual Test

export MAX_BOT_TOKEN=YOUR_TOKEN  ./zabbix_max_http.py 123456789 "Test subject" "Test message"

---

## ⚠️ Common Errors

- MAX_BOT_TOKEN is not set  
  → token is not configured

- chat_id must be integer  
  → invalid chat_id format

- MAX API error ...  
  → API returned an error

---

## 📌 Notes

- Uses MAX HTTP API
- No Telegram dependency
- Suitable for restricted or isolated environments
