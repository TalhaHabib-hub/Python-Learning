#creating command line utilities in python
# command line utilities are programs that can be run from the termnal fo command line interface, and they are an essential part of many development workflows. In python you can create your own command line utilites using the buil in argparse module
import argparse
import requests
# Source - https://stackoverflow.com/q/16694907
# Posted by Roman Podlinov, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-28, License - CC BY-SA 4.0

import requests

def DownloadFile(url, local_file_name):
    # Note the stream = True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file_name, 'wb')as f:
            for chunk in r.iter_content(chunk_size=8192):
                # if you have chunk encoded response uncomment if
                # and set chunck_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_file_name

parser = argparse.ArgumentParser()

# add comman line arguments
parser.add_argument('url',help='url of the file to download')
parser.add_argument('out',help='which name do you want to save your file')

#parse the arguments
args = parser.parse_args()

#use the arguments in your code
print(args.url)
print(args.output)
DownloadFile(args.url, args.output)