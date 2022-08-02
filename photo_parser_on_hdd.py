"""Parsing photo"""

import requests
from PIL import Image

from io import BytesIO


def download(query: str, page_count: int) -> None:
    header = {"Authorization": "563492ad6f9170000100000191531d4acb0e4a5eba1d002473d6ae53"}
    params = {"query": query, "per_page": 1}
    url = f"https://api.pexels.com/v1/search"
    i = 1
    while i <= page_count:
        params["page"] = i
        r = requests.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get("photos"):
                _img_url = item.get("src").get("original")
                resp = requests.get(_img_url)
            image = Image.open(BytesIO(resp.content))
            image.save(f'media/{query}_{i}.{_img_url.split(".")[-1]}')
        else:
            print(r.status_code)
        i += 1


def main():
    query = input("Ouery  ")
    page_count = int(input("Count_page  "))
    download(query, page_count)


main()
