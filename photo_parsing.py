"""work with requests"""

import requests


def download(q: str, p: str):
    header = {"Authorization": "563492ad6f9170000100000191531d4acb0e4a5eba1d002473d6ae53"}
    i = 1
    while i <= int(p):
        url = f"https://api.pexels.com/v1/search?query={q}&per_page=1&page={i}"
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get("photos"):
                print(item.get("url"))
        else:
            print(r.status_code)
        i += 1


def main() -> None:
    q = input("query  ")
    p = input("count  ")
    download(q, p)


main()
