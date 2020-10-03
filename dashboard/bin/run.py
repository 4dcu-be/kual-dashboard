# bin/python3
# encoding: utf-8

from datetime import datetime
import os
from os.path import join
from extract import get_google_scholar, get_gwent_data, get_tvmaze_data


scholar_url = "http://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
gwent_url = "http://www.playgwent.com/en/profile/sepro"
tvmaze_ids = [6,        # The 100
              79,       # The Goldbergs
              38963,    # The Mandalorian
              17128     # This Is Us
              ]

svg_path = '/mnt/base-us/extensions/dashboard/svg/' if os.name != 'nt' else '../svg'


def create_svg(svg_data, svg_template, svg_output):
    with open(svg_template, 'r') as fin:
        template = fin.read()

        for k, v in svg_data.items():
            template = template.replace(k, v)

        with open(svg_output, 'w') as fout:
            fout.write(template)


def fmt_date(date_input):
    d = datetime.strptime(date_input, '%Y-%m-%d')
    return d.strftime('%d/%m/%Y')


def is_today(date_input, fmt="%Y-%m-%d"):
    return date_input == datetime.now().strftime(fmt)


if __name__ == "__main__":
    # Get Data
    gs_data = get_google_scholar(scholar_url)
    gwent_data = get_gwent_data(gwent_url)
    tvmaze_data = get_tvmaze_data(tvmaze_ids)

    # Combine into dict
    svg_data = {"GS_HINDEX": gs_data.get("h_index"),
                "GS_CITATIONS": gs_data.get("citations"),
                "GWENT_LADDER_RANK": gwent_data.get("ladder") + (" (Rank " + gwent_data.get("rank") + ")" if "Pro" not in gwent_data.get("ladder") else ""),
                "GWENT_MMR": gwent_data.get("mmr"),
                "GWENT_POSITION": gwent_data.get("position"),
                "LASTUPDATE": "Last Update: " + datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}

    for i in range(3):
        if i < len(tvmaze_data):
            svg_data["TV_SHOW_%d" % (i + 1)] = tvmaze_data[i]["name"]
            svg_data["TV_EPISODE_%d" % (i + 1)] = tvmaze_data[i]["episode_name"]
            svg_data["TV_AIRDATE_%d" % (i + 1)] = "TODAY" if is_today(tvmaze_data[i]["airdate"]) \
                else fmt_date(tvmaze_data[i]["airdate"])
        else:
            svg_data["TV_SHOW_%d" % (i+1)] = "No upcoming episodes found"
            svg_data["TV_EPISODE_%d" % (i + 1)] = ""
            svg_data["TV_AIRDATE_%d" % (i + 1)] = ""

    # Load Data into SVG
    create_svg(svg_data, join(svg_path, "template.svg"), join(svg_path, "tmp.svg"))
