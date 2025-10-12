"""I first used burpsuite to learn about the behavior of the application, and then I figured that every 15 minutes
sending the request can block other users from trying to get the seat.
So I asked ChatGPT to help me write this program that will send the web request every 15 minutes.
This is how I enforced the seat next to Teresa at a Jazz concert we went. By blocking access of the seat by anyone else.
"""


import requests
import time

# Burp Proxy Setup (Make sure Burp is running)
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

# Target URL
url = "https://tickets.mru.ca/include/modules/SeatingChart/Request/reserveSeatmapSeats.asp"

# Headers (Copied from your request)
headers = {
    "Host": "tickets.mru.ca",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Sec-Ch-Ua-Mobile": "?0",
    "Origin": "https://tickets.mru.ca",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://tickets.mru.ca/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Priority": "u=1, i",
    "Cookie": "_gid=GA1.2.1713971953.1741235819; _fbp=fb.1.1741235819506.343655166763345388; sa-user-id=s%253A0-a80380e1-aaa8-58c6-4d90-77d2264933b0.8YI7yw3hu5HmTfS1Mu5bjL8r4wI2kcsI5QjVox7UhII; sa-user-id-v2=s%253AqAOA4aqoWMZNkHfSJkkzsEufnmg.E7tMl88Lq0yg6JezNhNgKRhmTvQ7Ur1kOmSOxQEHHeE; sa-user-id-v3=s%253AAQAKILsPtS4GcBBxn5g5fztLV5HzNzmPIWDkvs6wkDbnJ0WOEAEYAyCmn6u1BjABOgQob8fjQgTlHy6F.YPeuG8LH8gRMxyjbfSVTiVBLky4MRivv06evllUaNeg; CSTMEVENTID=; userbasketid=3TSTFkQ0VLUwQDM5E3MMjDMy0SNDIM1zEjNwM0MUTTN30yNS4NxwUTMuk4LEj0UW1CN05UY%5FJVQV9S%5F%5F%5F; ASPSESSIONIDASBBRBAA=GANPJFLAFGKEFJEHPOGGDJON; hasperformances=True; ASPSESSIONIDAQBARBAA=MEFAKFLAHKGKFFKPPDEGJDDA; ShowareVersion=newUI; ASPSESSIONIDSQDDRCAC=HNPPJFLAFLHLECHDECDIIEAB; WordVerificationAuditHash=E1%7Cc4dUlATIlEaXC0w79IMdpQ%3D%3D%7CpSswOoqRp7YginjtxA32YUS0h%2FrXeu2CbgP5qUua1Ji83JTtfBw271lrZMQl6D%2FmD3gN08bh7OD6t9MnKcBlyX3kSouCWYW4oaSDPju4jHMZtV4%2Bb4J6TJlluP3hYyI%2B; ValidLines=E1%7CQ6c34YdmUSS6yzK4zNa%2BYQ%3D%3D%7CBHMvTeEiuEgeE6%2BXrHwNKQ%3D%3D; _gcl_au=1.1.1606673634.1741235819.1696341259.1741299347.1741299527; _ga_2P7H4WW4SF=GS1.1.1741299346.2.1.1741300094.0.0.0; _gat_UA-152680229-1=1; _ga_07YPDKDMPP=GS1.1.1741299346.3.0.1741300094.60.0.0; _ga_71Y4Q7K8GS=GS1.1.1741299345.2.1.1741300094.0.0.0; _ga_Z3P95V6E8X=GS1.1.1741299345.2.1.1741300094.0.0.0; _ga_8D0L8ZY547=GS1.1.1741299345.2.1.1741300094.0.0.0; _ga_XWH5FCZYVQ=GS1.1.1741299345.2.1.1741300094.0.0.0; _ga=GA1.2.41340770.1741235819"
}

# Request Body (Your exact data payload)
data = '{"p":1653,"gaSeats":[],"reservedSeats":[{"area":2588,"pricingCode":"REG","seatCategory":746,"id":779027}],"oldBundleID":0,"qualifierID":0}'

while True:
    try:
        # Send the request
        response = requests.post(url, headers=headers, data=data, proxies=proxies, verify=False)

        # Print request status
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sent request - Status: {response.status_code}")

        # Print response for debugging (optional)
        print(response.text)

    except requests.RequestException as e:
        print(f"Error sending request: {e}")

    # Wait 15 minutes before sending again
    time.sleep(900)
