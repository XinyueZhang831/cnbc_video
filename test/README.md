# Testing code

This code is used to test openpose and ffmpeg function, inlude:

- Testing 1: ffmpeg get frames from multiple CNBC videos (exclude the beginng music and end music)

- Testing 2: run openpose to get analyze result from multiple folders (result from the previous test)

- Testing 3: ffmpeg get one frame at specific second and run openpose analysis it.


### Input

- openpose_path: opepose folder directory

- video_folder: input video folder's dir

- out_path: where you want to save the result from ffmpeg and openpose

- video_type: input video type (e.g. mp4)

- freq: the number of frames from specific time (e.g. 1/10 means 1 frame from each 10 sec)

- vid: the video is, which will be used to run testing3 (e.g. 7000113419)

- time: a frame at the specific time (e.g. '00:06:37')

