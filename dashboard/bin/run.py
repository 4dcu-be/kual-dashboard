# bin/python3
# encoding: utf-8

from datetime import datetime
import os
from extract import get_google_scholar, get_gwent_data, get_tvmaze_data

scholar_url = "http://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
gwent_url = "http://www.playgwent.com/en/profile/sepro"

tvmaze_ids = [6,  # The 100
              79,  # The Goldbergs
              38963,  # The Mandalorian
              ]

if __name__ == "__main__":
    # Load data. printing text here is for debugging only, should be removed later
    os.system('eips -c')

    os.system('eips 15  4 \'Loading Data ...\'')
    os.system('eips 15  6 \'Google Scholar ...\'')
    gs_data = get_google_scholar(scholar_url)
    os.system('eips 15  7 \'Gwent ...\'')
    gwent_data = get_gwent_data(gwent_url)
    os.system('eips 15  8 \'TVMaze ...\'')
    tvmaze_data = get_tvmaze_data(tvmaze_ids)

    # All data is loaded, let's put it on the screen
    os.system('eips -c')
    os.system('eips -c')
    os.system('eips 15  2 \'Google Scholar\'')
    os.system('eips 15  4 \'H-index   : %s\'' % gs_data.get('h_index', 'NA'))
    os.system('eips 15  5 \'Citations : %s\'' % gs_data.get('citations', 'NA'))

    os.system('eips 15  9 \'Gwent (%s)\'' % gwent_data.get('ladder', 'error'))
    os.system('eips 15  11 \'Player    : %s\'' % gwent_data.get('player', 'NA'))
    os.system('eips 15  12 \'MMR       : %s\'' % gwent_data.get('mmr', 'NA'))
    os.system('eips 15  13 \'Position  : %s\'' % gwent_data.get('position', 'NA'))

    os.system('eips 15  17 \'TVMaze\'')
    for line, episode in enumerate(tvmaze_data[:3], start=19):
        os.system('eips 15  %d \'%s: %s %s\'' % (line, episode['name'], episode['episode_name'], episode['airdate']))

    os.system('eips 15  26 \'Last Update  : %s\'' % datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
