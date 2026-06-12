import requests
import json
import os
import time

cookies = {
    'k_stat': 'f6d2b2e2-e5c2-4809-bdc8-725a3b2fdd41',
    'ks.tg': '9',
    'kaspi.storefront.cookie.city': '750000000',
    'locale': 'ru-RU',
    '_hjSessionUser_283363': 'eyJpZCI6ImQ1ZTcxZjIyLTZhYjgtNWMzMi1iOGZmLTk2MzI4MTExNzY0MSIsImNyZWF0ZWQiOjE3ODExMDM5NzAwNzMsImV4aXN0aW5nIjpmYWxzZX0=',
    'current-action-name': 'Index',
}

headers = {
    'Accept': 'application/json, text/*',
    'Accept-Language': 'ru,en;q=0.9',
    'Referer': 'https://kaspi.kz/shop/c/notebooks/',
    'User-Agent': 'Mozilla/5.0',
    'X-KS-City': '750000000',
}

os.makedirs("data", exist_ok=True)

url_template = "https://kaspi.kz/yml/product-view/pl/results"

for page in range(1000):

    params = {
        "page": page,
        "q": ":category:Notebooks:availableInZones:Magnum_ZONE1",
        "text": "",
        "sort": "relevance",
        "c": "750000000",
    }

    try:
        response = requests.get(
            url_template,
            params=params,
            cookies=cookies,
            headers=headers,
            timeout=10
        )

        print(f"Page {page} | Status: {response.status_code}")

        # 🚨 обработка редиректов
        if response.history:
            print(f"Redirect detected on page {page}")
            break

        if response.status_code != 200:
            print(f"Stopped at page {page}, status {response.status_code}")
            break

        # 🚨 безопасный JSON парсинг
        try:
            data = response.json()
        except Exception:
            print(f"Not JSON at page {page}")
            print(response.text[:200])
            break

        # 🚨 если данных нет — стопаемся
        if not data:
            print("Empty response, stopping...")
            break

        with open(f"data/page_{page}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        time.sleep(1.2)

    except requests.RequestException as e:
        print(f"Request error on page {page}: {e}")
        break
