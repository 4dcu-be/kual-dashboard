# KUAL Dashboard

This is a KUAL extension that turns a Kindle Paperwhite 3 into a dashboard that shows details for:

  * Google Scholar
  * Gwent (player rank)
  * TVMaze (upcoming episode for TV shows)

More details how to set up your Kindle and an overview of the code can be found on the 4DCu.be blog ([part one](http://blog.4dcu.be/diy/2020/09/27/PythonKindleDashboard_1.html), 
[part two]())

## Requirements

  * A Jailbroken Kindle Paperwhite 3
  * KUAL installed with Python 3
  * If you are looking for instructions to do this, check [here](http://blog.4dcu.be/diy/2020/09/27/PythonKindleDashboard_1.html) for details and links to additional resources.
  
## Installation

Copy the folder `dashboard` from the repository to the `/extensions` folder on the kindle (if that folder is not there
KUAL isn't installed properly).

Open the file `/extensions/dashboard/bin/run.py` and fine the following lines:

```python
scholar_url = "http://scholar.google.com/citations?user=4niBmJUAAAAJ&hl=en"
gwent_url = "http://www.playgwent.com/en/profile/sepro"
tvmaze_ids = [6,        # The 100
              79,       # The Goldbergs
              38963,    # The Mandalorian
              17128     # This Is Us
              ]
```

And add the URL to the desired scholar profile, gwent profile and show IDs from [TVMaze](https://www.tvmaze.com/) in the appropriate locations.

## Starting the Dashboard

First type `~ds` in the searchbar and hit enter. This will disable the Kindle's own deep sleep and screensaver, this is
required as this will put the device in deep sleep without the wake-up timer enabled eventually. Which in turn will 
stop the dashboard from refreshing. To disable this you will need to restart the Kindle by holding the power button for
15-20 seconds and pushing restart in the menu.

Next, open KUAL and start "Dashboard 4DCu.be", wait 30 seconds for the dashboard to appear and done!

## Acknowledgements

rsvg-convert included in this repo is derived from [https://github.com/x-magic/kindle-weather-stand-alone](https://github.com/x-magic/kindle-weather-stand-alone) as well
as the configuration files to integrate the script with KUAL.