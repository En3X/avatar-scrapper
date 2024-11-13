API_URL = "https://avatar.iran.liara.run/public"

import requests
import os
import threading


def download_image(i):
    r = requests.get(API_URL)
    if r.status_code == 200:
        with open(f"{i}.png", "wb") as f:
            f.write(r.content)


threads = []

numImages = int(input("Number of images: "))

for i in range(1, numImages + 1):
    t = threading.Thread(target=download_image, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
