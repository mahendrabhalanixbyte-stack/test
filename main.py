import requests
#

def delivered():
    feed_url = "https://glacier.xbyte.io/api/feed-process"
    payload = {
        'feed_id': '24084',
        # 'code': f'{feed_id}_{datetime.now().strftime("%Y_%m_%d")}_batch_1',
        'code': f'24084_2026_02_20_batch_1',
        'status': '2',
        'file_path': ""
    }
    try:
        response_delivered = requests.post(url=feed_url, data=payload, timeout=12)
        print(response_delivered)
        print(response_delivered.text)
    except Exception as e:
        print(e)
delivered()