# Install OpenPose command-line tool

## Install environment:

 - Python: 3.7

 - macOS: Catalina 10.15

 - OpenCV: 4.2.0

 - Homebrew: 2.2.3

 - Boost-python3: 1.72.0

## Dependencies:

#### - Install Xcode from App Store

#### - Install CMake 3.16.2 from App Store

#### - Homebrew (if you don't have brew in your command-line)

Copy this line into your terminal and press Enter key

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

####  - Other dependencies:

Copy each line into your terminal and press Enter key

```bash
brew install -vd snappy leveldb gflags glog szip lmdb

brew install openblas

brew install hdf5 opencv

brew install boost boost-python3

brew install automake libtool
```

## Install Openpose

Open terminal tool and cd to the dir you want to install openpose

Copy this line into your terminal and press Enter key

```bash
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
```

Under Openpose, go to 3rdparty folder

```bash

cd ./openpose/3rdparty

git clone https://github.com/CMU-Perceptual-Computing-Lab/caffe.git

git clone https://github.com/pybind/pybind11.git

```

## Modify Cmake

![Cmake](/doc/Cmake.jpg)

### - Where is the source code: your openpose directory

### - Where to build the binaries: a subdir under openpose directory. If you don’t have build folder under openpose, there will be a pop-up ask you to create dir, just click yes.

### - Check the following:
 
 BUILD_CAFFE
 
 BUILD_EXAMPLES
 
 BUILD_PYTHON
 
 BUILD_SHARED_LIBS
 
 DOWNLOAD_BODY_25_MODEL
 
 DOWNLOAD_FACE_MODEL
 
 DOWNLOAD_HAND_MODEL
 
 WITH_EIGEN

### - Make sure cmake find the following:
 
 CMAKE_OSX_SYSROOT (example: /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk)
 
 Caffe_INCLUDE_DIRS (example: /Users/xinyue/Video/openpose/build/caffe/include)
 
 Caffe_LIBS (example: /Users/xinyue/Video/openpose/build/caffe/lib/libcaffe.dylib)
 
 GPU_MODE ============ CPU_ONLY
 
 OpenCV_DIR (example: /usr/local/lib/cmake/opencv4)
 
 vecLib_INCLUDE_DIR (example: /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/vecLib.framework/Headers)


### - Almost done

Click Configure Butter, if everything correct there will be no read either in the list of items or in the text box.

If configure successed, there will be a Configure Done message in the text box.

Then click Generate

### Install everything

For Mac:

```bash
cd build/
make -j`sysctl -n hw.logicalcpu`
```

## Test OpenPose:

- Check this [link](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/quick_start.md#quick-start)

In your terminal under openpose your can test, this code will display the result but not save

```bash
# Ubuntu and Mac
./build/examples/openpose/openpose.bin --image_dir examples/media/
# With face and hands
./build/examples/openpose/openpose.bin --image_dir examples/media/ --face --hand
```

This code will save to the place you want to save it.

```bash
# Ubuntu and Mac
./build/examples/openpose/openpose.bin --image_dir examples/media/ --write_images output/
# With face and hands
./build/examples/openpose/openpose.bin --image_dir examples/media/ --write_images output/ --face --hand'
```

- Inside the [test folder](https://github.com/XinyueZhang831/cnbc_video/tree/master/test), I wrote a code to test if the openpose work or not.


## Common Error

### * Install

#### Could NOT find vecLib

open openpose/build/caffe/src/openpose_lib-build/CMakeCache.txt

under line 438 paste:

//vecLib include directory

vecLib_INCLUDE_DIR:PATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/vecLib.framework/Headers

### * Run openpose

### - model not found

When use openpose on command line, it must be inside openpose dir

### - no such directory (cannot save output)

you need to build output folder under openpose dir first


# Install ffmpeg

Chech [ffmpeg link](http://macappstore.org/ffmpeg/)

## test ffmpeg

In command-line tool

```bash
# 1 frame from each 10 sec and save to out put, not limite start and end time
ffmpeg -i /video_dir.mp4 -r 1/10 /output_dir/output_%0d5.png

# 1 frame from each 10 sec and save to out put, limite start and end time
ffmpeg -i /video_dir.mp4 -ss start_time(sec) -to end_time(sec) -r 1/10 /output_dir/output_%0d5.png

# 1 frame from a specific time, time format 00:00:00
ffmpeg -ss time -i /video_dir.mp4 -vframes 1 /output_dir/output_%0d5.png
```
ffmpeg screenshot [How to extract 1 screenshot for a video with ffmpeg at a given time?](https://stackoverflow.com/questions/27568254/how-to-extract-1-screenshot-for-a-video-with-ffmpeg-at-a-given-time)

## Reference

 - [OpenPose Install](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md#installation)
 
 - [Install Caffe on Mac Python CPU only](https://www.dazhuanlan.com/2019/08/15/5d5514f5efcdc/)
 
 - [Install ffmpeg](http://macappstore.org/ffmpeg/)
 
 - [OpenPose Quick Start](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/quick_start.md#quick-start)

 - [How to extract 1 screenshot for a video with ffmpeg at a given time?](https://stackoverflow.com/questions/27568254/how-to-extract-1-screenshot-for-a-video-with-ffmpeg-at-a-given-time)
