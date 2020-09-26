import ssl
import urllib.request
import re


def get_google_scholar(url):
    ssl_context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=ssl_context) as response:
        html = response.read()

    hits = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', str(html))
    fields = ['citations', 'citations_recent', 'h_index', 'h_index_recent', 'i10_index', 'i10_index_recent']

    return dict(zip(fields, hits))


def get_gwent_data(url):
    ssl_context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=ssl_context) as response:
        html = response.read()

    output = {
        'player':   re.findall(r'<strong class="l-player-details__name">\\n\s+(.*?)</strong>', str(html))[0],
        'mmr':      re.findall(r'<div class="l-player-details__table-mmr">.*?<strong>(.*?)</strong></div>', str(html))[0],
        'position': re.findall(r'<div class="l-player-details__table-position">.*?<strong>(.*?)</strong></div>', str(html))[0],
        'rank':     re.findall(r'<span class="l-player-details__rank"><strong>(.*?)</strong></span>', str(html))[0],
        'ladder':   re.findall(r'<div class="l-player-details__table-ladder" ><span>(.*?)</span></div>', str(html))[0],
    }

    return output


if __name__ == "__main__":
    scholar_url = "https://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
    gwent_url = "http://www.playgwent.com/en/profile/sepro"

    #gs_data = get_google_scholar(scholar_url)
    gwent_data = get_gwent_data(gwent_url)

    #print(gs_data)
    print(gwent_data)
