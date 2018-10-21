% Script to save all frames frames of a video
clear all
rootdir = '/Users/ilkay.isik/Desktop/ContinuousRatingAnimation';
cd(rootdir)
savepath = [rootdir, '/framesFromVideo/'];
videos = dir('*.mp4');

% pick the 3rd video
video_name = videos(3).name

% nr_movies = length(video_paths);

% Create a video object and establish the number of frames
video = VideoReader(video_name);
dur = video.Duration;
frame_rate = video.FrameRate;
nr_frames = dur * frame_rate;

% write out all the frames as png
for i = 1:nr_frames
    frame = read(video, i); 
    % name of the file
    image_name = [savepath, video_name(1:end-9), 'frame_', num2str(i), '.png'];
    % write it out
    imwrite(frame, image_name)
end

disp(i)