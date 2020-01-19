import CNBCopenpose
import pandas as pd
import subprocess
import os


#################################################
# Testing Ffmpeg with multiple video
#################################################
def ff_mult(video_folder, out_path, video_type, freq):
    df = pd.read_csv('/Users/xinyue/Documents/college/SA_Work/data/video_final_output.csv')[40:45]
    for i,r in df.iterrows():
        vid = r['video_id']
        start_time = r['B1_music_s']
        stop_time = int(r['time']) - int(r['E1_music_s'])
        CNBCopenpose.Ffmpeg(video_folder, out_path, video_type, freq).video(vid, start_time,
                                                                                        stop_time)


################################################
# Testing OpenPose with multiple video
################################################
def oppo_mult(out_path,openpose_path):
    in_path_list = os.listdir(out_path)
    for each_dir in in_path_list:
        if 'DS' not in each_dir:
            oppo_inframe = out_path + '/'+ each_dir
            each_dir = 'out_getframe/' + each_dir
            CNBCopenpose.CNBC(openpose_path, oppo_inframe, each_dir).openpose_facehand()


################################################
# Testing OpenPose with one video with specific
#  time ffmpeg
################################################
def ffop_sec(video_folder, out_path, video_type, freq, vid, time, openpose_path):
    CNBCopenpose.Ffmpeg(video_folder, out_path, video_type, freq).video_sec(vid,time)
    oppo_mult(out_path, openpose_path)


# opepose folder directory
openpose_path = '/Users/xinyue/Video/openpose'

subprocess.call('cd ' + openpose_path + ' && ' + 'mkdir ' + "getframe", shell=True)
subprocess.call('cd ' + openpose_path + ' && ' + 'mkdir ' + "out_getframe", shell=True)

# ffmpeg use to find the video we need
video_folder = '/Users/xinyue/PycharmProjects/youtube_dl'


# ffmpeg will save frames in this place
out_path = openpose_path +'/getframe'


# ffmpeg need know video type
video_type = 'mp4'


# ffmpeg need to get frame
freq = 1/10


vid = 7000113419
time = '00:06:37'
#ffop_sec(video_folder, out_path, video_type, freq, vid, time, openpose_path)
#ff_mult(video_folder, out_path, video_type, freq)
#oppo_mult(out_path,openpose_path)