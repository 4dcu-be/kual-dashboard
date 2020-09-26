# bin/python3
# encoding: utf-8

from datetime import datetime
import os
from extract import get_google_scholar, get_gwent_data

scholar_url = "http://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
gwent_url = "http://www.playgwent.com/en/profile/sepro"

if __name__ == "__main__":
    os.system('eips -c')

    os.system('eips 15  4 \'Loading Data ...\'')
    os.system('eips 15  6 \'Google Scholar ...\'')
    gs_data = get_google_scholar(scholar_url)
    os.system('eips 15  7 \'Gwent ...\'')
    gwent_data = get_gwent_data(gwent_url)

    os.system('eips -c')
    os.system('eips -c')
    os.system('eips 15  2 \'Google Scholar\'')
    os.system('eips 15  4 \'H-index   : %s\'' % gs_data.get('h_index', 'NA'))
    os.system('eips 15  5 \'Citations : %s\'' % gs_data.get('citations', 'NA'))

    os.system('eips 15  9 \'Gwent (%s)\'' % gwent_data.get('ladder', 'error'))
    os.system('eips 15  11 \'Player    : %s\'' % gwent_data.get('player', 'NA'))
    os.system('eips 15  12 \'MMR       : %s\'' % gwent_data.get('mmr', 'NA'))
    os.system('eips 15  13 \'Position  : %s\'' % gwent_data.get('position', 'NA'))

    os.system('eips 15  18 \'Last Update  : %s\'' % datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
