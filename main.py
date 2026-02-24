import requests

FEED_URL = "https://glacier.xbyte.io/api/feed-process"
FEED_ID = "24084"
BATCH_CODE = "24084_2026_02_20_batch_1"


def delivered() -> bool:
    """Notify the feed service that a batch has been delivered."""
    payload = {
        "feed_id": FEED_ID,
        "code": BATCH_CODE,
        "status": "2",
        "file_path": "",
    }

    try:
        response = requests.post(url=FEED_URL, data=payload, timeout=12)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Delivery update failed: {exc}")
        return False

    print(f"Delivery update succeeded: {response.status_code}")
    print(response.text)
    return True


if __name__ == "__main__":
    delivered()
