# dtube-steem-video-upload
This is a selenium-based python script to upload a video to dtube and post on steem.

## Prerequisites:

### Python Packages:
**Python3 needs to be installed. Use pip install for following packages.**
- requests
- selenium

### Installations:

- Chromedriver download is required, and it **MUST BE COMPATIBLE** to chrome browser. The path to the same must be assigned to chromedriver_path in main.py. 
Example: chromedriver_path="C:\\software\\chromedriver\\chromedriver.exe"

## Execution Instructions:

1. Place single video file and image file into the video_folder folder beside the script, or in configured video folder.
2. Run the file main.py, preferably through command line.

## Algorithm:

1. Login
2. Upload video, and wait for upload to complete
3. Add title, steem post details and submit

##Note:

File name is duplicated as title and steem post content. Please contact for change in the same.

Please inform me regarding any other issues/requirements, I will handle them and update here.
