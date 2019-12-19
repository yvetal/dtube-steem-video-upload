import dtube_handler as dh
import time, os

chromedriver_path="C:\\software\\chromedriver\\chromedriver.exe"
video_path='C:\\Users\\Neel\\coderepo\\repositories\\dtube-account-creation-selenium\\video_folder'
username='brianstorm'
password='5JikyjfsTR4YLwg7wpqFPjCRpmqskRwRdkUpyhMJZEapTgxbwTu'

if __name__ == "__main__":
	dh.initialise_driver(chromedriver_path)
	dh.login(username, password)
	time.sleep(10)
	dh.upload_video(video_path)