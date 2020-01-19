import CNBCopenpose
import pandas as pd
import subprocess
import os

# need to create getframe and out_getframe in openpose folder
# opepose folder directory
openpose_path = '/Users/xinyue/Video/openpose'

# ffmpeg use to find the video we need
video_folder = '/Users/xinyue/PycharmProjects/youtube_dl'


# ffmpeg will save frames in this place
out_path = openpose_path +'/getframe'


# ffmpeg need know video type
video_type = 'mp4'


# ffmpeg need to get frame
freq = 1/10






#testing = CNBCopenpose.CNBC(openpose_path, in_path, opout_path).openpose_body()



#################################################
# Testing Ffmpeg with multiple video
#################################################

#df = pd.read_csv('/Users/xinyue/Documents/college/SA_Work/data/video_final_output.csv')[40:45]
#for i,r in df.iterrows():
    #vid = r['video_id']
    #start_time = r['B1_music_s']
    #stop_time = int(r['time']) - int(r['E1_music_s'])
    #testing_2 = CNBCopenpose.Ffmpeg(video_folder, out_path, video_type, freq).video(vid, start_time,
    #                                                                                stop_time)


################################################
# Testing OpenPose with multiple video
################################################
#in_path_list = os.listdir(out_path)[5:]
#print(in_path_list)
#for each_dir in in_path_list:
#    if 'DS' not in each_dir:
#        oppo_inframe = out_path + '/'+ each_dir
#        each_dir = 'out_getframe/' + each_dir
#        testing3 = CNBCopenpose.CNBC(openpose_path, oppo_inframe, each_dir).openpose_facehand()




################################################
# Testing OpenPose with one video with specific
#  time ffmpeg
################################################

vid = 7000113419
time = '00:06:37'
testing4 = CNBCopenpose.Ffmpeg(video_folder, out_path, video_type, freq).video_sec(vid,time)
in_path_list = os.listdir(out_path)
print(in_path_list)
for each_dir in in_path_list:
    if 'DS' not in each_dir:
        oppo_inframe = out_path + '/'+ each_dir
        each_dir = 'out_getframe/' + each_dir
        testing3 = CNBCopenpose.CNBC(openpose_path, oppo_inframe, each_dir).openpose_facehand()


