import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    text = BeautifulSoup(requests.get(url).text, "html.parser").get_text("\n")

    rows = [i.strip() for i in text.splitlines() if i.strip()]

    data = []
    for i in range(len(rows)-2):
        if rows[i].isdigit() and rows[i+2].isdigit():
            data.append((int(rows[i]), rows[i+1], int(rows[i+2])))

    w = max(x for x,_,_ in data)+1
    h = max(y for _,_,y in data)+1

    grid = [[" "]*w for _ in range(h)]

    for x,ch,y in data:
        grid[y][x] = ch

    for row in grid:
        print("".join(row))


# Test
decode_secret_message("https://docs.google.com/document/u/0/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub?pli=1")