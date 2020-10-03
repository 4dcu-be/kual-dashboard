import json
import os
from datetime import datetime
from functools import wraps

cache_dir = '/mnt/base-us/extensions/dashboard/cache/' if os.name != 'nt' else '../cache'


def hours_since_last_modification(file_path):
    """"
    Returns the number of hours since a file was modified. -1 indicates the file doesn't exists
    """
    if os.path.exists(file_path):
        last_modification = os.stat(file_path).st_mtime
        return (datetime.now().timestamp() - last_modification) / 3600
    else:
        return -1


def cache(cache_file, cache_time):
    """
    Decorator that combine two things:
        * if the decorated function fails (for any reason) it will pull the most recent data
        from cache and return those.
        * if the cache file is more recent than cache_time and return the
        cached data if the file is recent enough

    :param cache_file: File to write cache to
    :param cache_time: How long (in hours) a file should be cached
    """

    def deco_cache(f):
        @wraps(f)
        def f_cache(*args, **kwargs):
            hslm = hours_since_last_modification(cache_file)
            if 0 <= hslm < cache_time:
                with open(cache_file, 'r') as fin:
                    output = json.load(fin)
                return output

            try:
                output = f(*args, **kwargs)
                with open(cache_file, 'w') as fout:
                    json.dump(output, fout)
            except:
                with open(cache_file, 'r') as fin:
                    output = json.load(fin)
            return output

        return f_cache

    return deco_cache
