# bin/python3
# encoding: utf-8

from datetime import datetime
import os
from os.path import join
from extract import get_google_scholar, get_gwent_data, get_tvmaze_data


scholar_url = "http://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
gwent_url = "http://www.playgwent.com/en/profile/sepro"
tvmaze_ids = [6,  # The 100
              79,  # The Goldbergs
              38963,  # The Mandalorian
              ]

svg_path = '/mnt/base-us/extensions/dashboard/svg/' if os.name != 'nt' else '../svg'


def create_svg(svg_data, svg_template, svg_output):
    with open(svg_template, 'r') as fin:
        template = fin.read()

        for k, v in svg_data.items():
            template = template.replace(k, v)

        with open(svg_output, 'w') as fout:
            fout.write(template)


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
                "LASTUPDATE": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}

    # Load Data into SVG
    create_svg(svg_data, join(svg_path, "template.svg"), join(svg_path, "tmp.svg"))
