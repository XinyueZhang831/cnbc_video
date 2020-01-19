####################################
# Command-line get basic info
# with ffmpeg
####################################
import glob
import pandas as pd
import subprocess

def ffmpeg_pre(path):
    videos = glob.glob(path)
    df = pd.DataFrame()

    for file in videos:
        first_file = ('/').join(file.split('/')[:-1])
        second_file = file.split('/')[-1]

        third_file = ('\ ').join(second_file.split(' '))
        third_file = third_file.replace("'", "\\'")
        third_file = third_file.replace("$", "\\$")
        third_file = third_file.replace("&", "\\&")
        file = first_file + '/' + third_file
        return_info = subprocess.Popen('ffprobe -select_streams v -show_streams ' + file, shell=True,
                                       stdout=subprocess.PIPE)
        find_frame = return_info.communicate()[0]
        find_frame = find_frame.decode("utf-8")
        find_frame = find_frame.split('\n')
        frame = 0
        width = 0
        height = 0
        duration = 0
        for i in find_frame:
            if 'nb_frames' in i:
                frame = i.split('=')[1]
            if i[:6] == 'width=':
                width = i.split('=')[1]
            if i[:7] == 'height=':
                height = i.split('=')[1]
            if i[:9] == 'duration=':
                duration = i.split('=')[1]

        video_id = second_file.split('-')[-1]
        video_id = video_id.split('.')[0]
        data = {'video_id': video_id, 'nb_frames': frame, 'width': width, 'height': height, 'time': duration}
        df = df.append(data, ignore_index=True)
    df.to_csv('video_info.csv')