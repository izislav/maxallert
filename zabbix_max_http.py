#!/usr/bin/env python3
import json
import os
import sys

import requests

def fail(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 1

def main() -> int:
    if len(sys.argv) < 4:
        return fail("Usage: zabbix_max_http.py <chat_id> <subject> <message>")

    token = os.environ.get("MAX_BOT_TOKEN")
    if not token:
        return fail("MAX_BOT_TOKEN is not set")

    try:
        chat_id = int(sys.argv[1])
    except ValueError:
        return fail("chat_id must be integer")

    subject = sys.argv[2]
    message = sys.argv[3]

    body = {
        "text": f"{subject}\n{message}",
        "notify": True
    }

    try:
        resp = requests.post(
            "https://platform-api.max.ru/messages",
            headers={
                "Authorization": token,
                "Content-Type": "application/json",
            },
            params={"chat_id": chat_id},
            data=json.dumps(body),
            timeout=15
        )
    except Exception as e:
        return fail(f"Request failed: {e}")

    if resp.status_code >= 300:
        return fail(f"MAX API error {resp.status_code}: {resp.text}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
