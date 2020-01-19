#####################################
# Command-line download CNBC video
# with youtube_dl
#####################################

import pandas as pd
import subprocess


def youtube_pre(path):
    df = pd.read_csv(path)
    for i,r in df.iterrows():
        try:
            video_id = r['video_id']
            part_file = "http://video.cnbc.com/gallery/?video="
            files = part_file+str(video_id)
            subprocess.call('youtube-dl ' + files +' --verbose', shell=True)
        except:
            pass


path = ''
youtube_pre(path)
