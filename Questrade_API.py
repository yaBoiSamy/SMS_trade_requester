import requests
import time


ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
REFRESH_TOKEN = "YOUR_REFRESH_TOKEN"
API_URL = "https://api.questrade.com/v1"


def get_headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def refresh_token():
    global ACCESS_TOKEN
    url = "https://login.questrade.com/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }
    resp = requests.post(url, data=data).json()
    ACCESS_TOKEN = resp['access_token']
    print("Token refreshed!")


def get_accounts():
    resp = requests.get(f"{API_URL}/accounts", headers=get_headers()).json()
    return resp['accounts']


def get_account_status(account_id):
    resp = requests.get(f"{API_URL}/accounts/{account_id}/balances", headers=get_headers()).json()
    return resp


def place_order(account_id, symbol_id, quantity, action="Buy", order_type="Limit", limit_price=None):
    url = f"{API_URL}/accounts/{account_id}/orders"
    order_data = {
        "symbolId": symbol_id,
        "quantity": quantity,
        "action": action,
        "orderType": order_type,
        "price": limit_price if limit_price else 0,
        "timeInForce": "Day"
    }
    resp = requests.post(url, json=order_data, headers=get_headers())
    return resp.json()


if __name__ == "__main__":
    accounts = get_accounts()
    print("Accounts:", accounts)

    account_id = accounts[0]['number']
    status = get_account_status(account_id)
    print("Account Status:", status)
