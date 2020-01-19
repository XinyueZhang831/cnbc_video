# CNBC_VideoData
## Package
```bash
pip install selenium
pip install difflib
pip install pandas
```


## Code

### CNBC_videoid.py
WebScrapy video id and url from [CNBC CEO Interviews](https://www.cnbc.com/video-ceo-interviews/)

### CNBC_videodetail.py
WebScrapy video information, include name of the show, potential host(s)

### CNBC_youtubdl.py
Download CNBC video with [youtube_dl](https://github.com/ytdl-org/youtube-dl)

### CNBC_videodetail.py
Get baic infomation of video, includes number of frames. video width, video length and video duration

### CNBC_cleandata.py
Clean all data, count numbers of CEOs, Companies and Hosts

### CNBCopenpose.py
Analyze with ffmpeg and openpose

### testing.py
Inside test, test basic analysis

## Data

### video_info.csv
Output from CNBC_videodetail.py, also input for CNBC_cleandata.py

### video_data.csv
Input csv file for CNBC_cleandata.py

### video_final_output.csv
Final outputs.

Include:

#### - video_id
Each video has an unique id

#### - Interviewer
Host(s) of this video, *can be no host

#### - Company
Company(s) which attent this show

#### - CEO
CEO(s) who attent this show

#### - Tparty
If there is more than 2 people in the video. 

Y means yes, N means no

#### - B_music_s
When the host(s) speak first sentence, from 0 to 9999

 - 0: speak from beginning

 - 8888: video not be downloaded

 - 9999: this video has all music at the same time the host(s) may or may not speak

 - other number: host(s) starts speaking at this second

#### - B1_music_s
When the beginning music stops, from 0 to 9999

 - 0: There is no music
 
 - 8888: video not be downloaded

 - 9999: this video has all music at the same time the host(s) may or may not speak

 - other number: music stops at this second

#### - E_music_s
When the ending music starts, from 0 to 9999

 - 0: There is no music

 - 8888: video not be downloaded

 - 9999: this video has all music at the same time the host(s) may or may not speak

 - other number: ending music starts, and there is this number of seconds until this video stop

#### - E1_music_s
When the host(s) finish talk, from 0 to 9999

 - 0: host(s) keeps talking until the last second

 - 8888: video not be downloaded

 - 9999: this video has all music at the same time the host(s) may or may not speak

 - other number: the host(s) finish talk, and there is this number of seconds until this video stop

#### - hosts_count
Number of host(s) in this video

If missing, either video not be downloaded or there is no host for this show

#### - CEO_count
Number of CEO(s) in this video

If missing, either video not be downloaded or there is no CEO for this show

#### - height
Video height

#### - nb_frames
Number of frames in this video

#### - time
Duration of this video (in second)

#### - width
Video width

#### - CEO_origin
CEO name when manually recoded.

#### - Company_origin
Company name when manually recoded.

#### - Interviewer_origin
Host name when manually recoded.

#### - *Special notations:
  - (*): not sure about this person's name

  - (call): no movement in this video

  - (cannot download): video did notdownload

  - (only appears shortly): cannot catch people's face

  - (Guest Host)

  - (slugger)

  - (Chinese): this person speak Chinese, and there is two sounds track, one is Chinese and the other is English

  - (record): this person is recorder

### CEOscount.csv
CEOs' name and how many videos they appeared

### Companyscount.csv
Companies' name and how many videos they appeared

### Hostscount.csv
Hosts' name and how many videos they appeared

## Statistics on current videos:
Number of Host: 39, Number of CEO: 592, Number of Company: 572, Nunmber of Potential Video: 1138, Number of Download Video 
1134

## Author
Xinyue Zhang
