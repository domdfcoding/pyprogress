import time
import sys
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

def progress(downloaded, block_size, total_size):
    global download_size
    download_size = total_size
    completed = int(downloaded / (total_size//block_size) * 100)
    sys.stdout.write(f"\r|{'█' * completed}{' ' * (100-completed)}{completed}%")

def download_bar(url,filename):
    start = time.time()
    try:
        urlretrieve(url,filename,progress)
    except URLError:
        sys.stderr.write("The URL is invalid.\n")
        exit(0)
    except HTTPError as e:
        sys.stderr.write(f"Error: {e.code} {e.reason}\n")
        exit(0)
    except Exception as e:
        sys.stderr.write("An error occured\n")
        sys.stderr.write(type(e),e)
        exit(0)
    end = time.time()
    sys.stdout.write("\n")
    time_taken = end - start
    download_speed = round(download_size/(time_taken*1024),2)
    if download_speed >= 1024:
        sys.stdout.write(f"Downloaded in {(round(time_taken, 2))} s ({download_speed/1024}  MB/s)\n")
    if download_speed < 1024:
        sys.stdout.write(f"Downloaded in {(round(time_taken, 2))} s ({download_speed}  kB/s)\n")
    if download_speed < 1:
        sys.stdout.write(f"Downloaded in {(round(time_taken, 2))} s ({download_speed*1024}  B/s)\n")
