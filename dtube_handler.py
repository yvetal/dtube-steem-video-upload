from selenium import webdriver
from selenium.webdriver.common import keys
import time, os
driver=''

def initialise_driver(chromedriver_path):
	global driver
	driver = webdriver.Chrome(chromedriver_path)
	driver.implicitly_wait(15)
	
def login(username, password):
	print('Logging in')
	driver.get('https://d.tube/#!/login/steem')
	time.sleep(1)
	usernamebox=driver.find_element_by_id('username')
	usernamebox.send_keys(username)
	time.sleep(1)
	passwordbox=driver.find_element_by_name('privatekey')
	passwordbox.send_keys(password)
	time.sleep(1)
	button=driver.find_element_by_name('button')
	button.click()
	print('Logged in')
		
def _upload_video(details):
	print('Uploading Video')
	driver.get('https://d.tube/#!/upload')
	time.sleep(1)
	video=driver.find_elements_by_xpath("//input[@type='file']")[0]
	video.send_keys(details['Video Path'])
	time.sleep(1)
	
	snap=driver.find_elements_by_xpath("//input[@type='file']")[1]
	snap.send_keys(details['Snap Path'])
	time.sleep(1)
	state=0
	
	print('Waiting For Uploads')
	while(state<2):
		num=len(driver.find_elements_by_class_name('indicating'))
		if state==0:
			if num>2:
				state=1
		elif state==1:
			if num==2:
				state=2
		time.sleep(0.05)
	
	titl=driver.find_element_by_id('uploadTitle')
	titl.clear()
	titl.send_keys(details['Title'])
	
	adv_tab=driver.find_element_by_class_name('advanced')
	adv_tab.click()
	time.sleep(1)
	
	steem_post=driver.find_element_by_name('body')
	steem_post.send_keys(details['Steem Content'])
	time.sleep(1)
	
	button=driver.find_element_by_class_name('uploadsubmit')
	button.click()
	time.sleep(1)
	
	print('Upload successfully!')
	

def get_details(video_path):
	files=os.listdir(video_path)
	details={
		
	}
	for file in files:
		if '.mp4' in file:
			details['Title']=file.replace('.mp4','')
			details['Steem Content']=file.replace('.mp4','')
			details['Video Path']=video_path+'\\'+file
		elif 'jpg' in file:
			details['Snap Path']=video_path+'\\'+file
	return details
	
def upload_video(video_path):
	details=get_details(video_path)
	_upload_video(details)
	#upload_video('C:\\Users\\Neel\\coderepo\\repositories\\abc.mp4', 'C:\\Users\\Neel\\coderepo\\repositories\\de869e6c9fd5c739da60b1222d3c30d4.jpg', 'Test', 'Steem Test')
	
if __name__ == "__main__":
	video_path='C:\\Users\\Neel\\coderepo\\repositories\\dtube-account-creation-selenium\\video_folder'
	print(get_details(video_path))