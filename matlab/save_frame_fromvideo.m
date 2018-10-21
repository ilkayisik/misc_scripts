% Script to save still images from the first frames of the videos

rootdir = '/Users/ilkay.isik/Desktop/ContinuousRatingAnimation';
cd(rootdir)

video_paths = dir('*.mp4');
savepath = [rootdir, '/framesFromVideo/'];
% pick the 3rd video
video_paths = video_paths(3)
nr_movies = length(video_paths);


for m = 1 : nr_movies
    video_name = strcat(video_paths(m).name);
    % Create a video object and establish the number of frames
    video = VideoReader(video_name);
    
    % Load the first frame
    first_frame = read(video, 1); 
    % name of the file
    image_name = [savepath, video_name(1:end-4), '.png'];
    % write it out
    imwrite(first_frame, image_name)
end
