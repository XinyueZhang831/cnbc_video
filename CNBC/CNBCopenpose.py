import glob
import subprocess

def modify_dir_name(path, vid, part_op, isfolder,type):

    first_file = ('/').join(path.split('/')[:-1])
    second_file = path.split('/')[-1]
    if isfolder:
        vid = second_file.split('-')[-1].replace('.' + type, '')
    third_file = ('\ ').join(second_file.split(' '))
    third_file = third_file.replace("'", "\\'")
    third_file = third_file.replace("$", "\\$")
    third_file = third_file.replace("&", "\\&")
    file = first_file + '/' + third_file

    output_dir = part_op + '/' + vid
    return output_dir, file, vid

def check_str(input):
    if type(input) != str:
        input = str(input)
    return input


def get_video(input1, input2, input3):
    video = glob.glob(input1 + '/' + '*' + input2 + '.' + input3)
    if len(video) > 1:
        print('Duplicate')
    video = video[0]
    return video





class CNBC():


    def __init__(self, openpose_path, in_path, out_path):
        self.opp = openpose_path
        self.ip = in_path
        self.op = out_path

    def openpose_facehand(self):
        extra_cmd = 'cd ' + self.opp + '&& '
        cmd = extra_cmd + './build/examples/openpose/openpose.bin --image_dir ' + self.ip + ' --write_images ' + self.op+ ' --face --hand'
        subprocess.call(cmd, shell=True)

    def openpose_body(self):
        extra_cmd = 'cd ' + self.opp + '&& '
        cmd = extra_cmd + './build/examples/openpose/openpose.bin --image_dir ' + self.ip + ' --write_images ' + self.op
        subprocess.call(cmd, shell=True)


class Ffmpeg():

    def __init__(self,video_folder, out_path, video_type, freq):
        self.op = out_path
        self.vtype = video_type
        self.vfolder = video_folder
        self.freq = freq


    def videos(self):
        videos = glob.glob(self.vfolder + '/'+ '*.'+self.vtype)
        print(self.vfolder + '/ '+ '*.'+self.vtype)
        for file in videos:
            output_dir,file, video_id = modify_dir_name(file, None, self.op, True, self.vtype)

            subprocess.call('cd ' + self.op + ' && ' + 'mkdir ' + '"' + video_id +'"', shell=True)
            subprocess.call('cd ..')

            subprocess.call('ffmpeg -i ' + file + ' -r ' + str(self.freq) +' ' + output_dir + '/output_%0d5.png', shell=True)

    def video(self, vid, start_time = 0, stop_time = 0):
        start_time = check_str(start_time)
        stop_time = check_str(stop_time)
        vid = check_str(vid)

        video = get_video(self.vfolder, vid, self.vtype)
        output_dir,file, vid = modify_dir_name(video, vid, self.op, False,self.vtype)

        subprocess.call('cd ' + self.op + ' && ' + 'mkdir ' + '"' + vid + '"', shell=True)
        subprocess.call('ffmpeg -i ' + file + ' -ss ' + start_time + ' -to ' + stop_time + ' -r ' + str(self.freq) + ' ' + output_dir + '/output_%0d5.png',
                        shell=True)

    def video_sec(self, vid, time):
        vid = check_str(vid)
        time = check_str(time)

        video = get_video(self.vfolder, vid, self.vtype)
        output_dir, file, vid = modify_dir_name(video, vid, self.op, False,self.vtype)

        subprocess.call('cd ' + self.op + ' && ' + 'mkdir ' + '"' + vid + '"', shell=True)
        subprocess.call(
            'ffmpeg -ss ' + time + ' -i ' + file + ' -vframes 1 ' + output_dir + '/output_%0d5.png',shell=True)

