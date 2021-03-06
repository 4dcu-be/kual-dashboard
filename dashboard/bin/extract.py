import ssl
import urllib.request
import re
import json
from os.path import join

from dashboard.bin.cache import cache_dir, cache


@cache(join(cache_dir, 'scholar.json'), 8)
def get_google_scholar(url):
    ssl_context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=ssl_context) as response:
        html = response.read()

    hits = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', str(html))
    fields = ['citations', 'citations_recent', 'h_index', 'h_index_recent', 'i10_index', 'i10_index_recent']

    return dict(zip(fields, hits))


@cache(join(cache_dir, 'gwent.json'), 1)
def get_gwent_data(url):
    ssl_context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=ssl_context) as response:
        html = response.read()

    output = {
        'player': ''.join(re.findall(r'<strong class="l-player-details__name">\\n\s+(.*?)</strong>', str(html))),
        'mmr': ''.join(
            re.findall(r'<div class="l-player-details__table-mmr">.*?<strong>(.*?)</strong></div>', str(html))).replace(
            ',', ''),
        'position': ''.join(re.findall(r'<div class="l-player-details__table-position">.*?<strong>(.*?)</strong></div>',
                                       str(html))).replace(',', ''),
        'rank': ''.join(re.findall(r'<span class="l-player-details__rank"><strong>(.*?)</strong></span>', str(html))),
        'ladder': ''.join(
            re.findall(r'<div class="l-player-details__table-ladder" ><span>(.*?)</span></div>', str(html))),
    }

    return output


@cache(join(cache_dir, 'tvmaze.json'), 8)
def get_tvmaze_data(ids):
    output = []

    ssl_context = ssl._create_unverified_context()
    for id in ids:
        url = 'http://api.tvmaze.com/shows/%d' % id
        with urllib.request.urlopen(url, context=ssl_context) as response:
            data = json.load(response)
            links = data.get('_links', {})
            if 'nextepisode' in links.keys():
                with urllib.request.urlopen(links['nextepisode']['href'], context=ssl_context) as episode_response:
                    episode_data = json.load(episode_response)
                    output.append(
                        {
                            'name': data.get('name', 'error'),
                            'episode_name': episode_data.get('name', 'error'),
                            'airdate': episode_data.get('airdate', 'error'),
                        }
                    )

    return sorted(output, key=lambda x: x['airdate'])


if __name__ == "__main__":
    scholar_url = "http://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
    gwent_url = "http://www.playgwent.com/en/profile/sepro"

    tvmaze_ids = [6,  # The 100
                  79,  # The Goldbergs
                  38963,  # The Mandalorian
                  17128  # This Is Us
                  ]

    gs_data = get_google_scholar(scholar_url)
    gwent_data = get_gwent_data(gwent_url)
    tvmaze_data = get_tvmaze_data(tvmaze_ids)

    print(gs_data)
    print(gwent_data)
    print(tvmaze_data)
