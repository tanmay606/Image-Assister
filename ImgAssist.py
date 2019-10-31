"""

This program will help you to download all your favourite photos, quotes or any image media all at once , all you need to do is to copy links in your clipboard, to understand the usage please watch the full video.

This program requires additional module 'pyperclip' to capture your clipboard.
To Install : pip install pyperclip

My Facebook : https://www.facebook.com/tanmayupadhyay91
Short Tutorial : https://www.youtube.com/watch?v=fPv0kaOMnA8


"""

import pyperclip
import requests
import random
import time
from os import getcwd,chdir

class PicsHower(object):
	#pyperclip.copy('') #To Empty Clipboard at first.
	extentions = ['.jpg','.jpeg','.png','.bmp','.svg','.ico']
	Media_links = []
	default_savelocation = "settings.conf" #change this to change location of downloaded images.
	def __init__(self):
		try:
			with open(PicsHower.default_savelocation,'r') as configuration:
				self.config_location = configuration.readlines()
			for eachline in self.config_location:
				if "download_folder_location" in eachline:
					PicsHower.default_savelocation = eachline.split('[')[1]
					PicsHower.default_savelocation = PicsHower.default_savelocation.split(']')[0]
		except OSError:
			PicsHower.default_savelocation = getcwd()
		print('Written By : Tanmay Upadhyay')
		print('Email : kevinthemetnik@gmail.com')
		print('Python Version : 3.x\n')
		print('[note] links should be direct ie.ends with image file extention')
		print('[Download Images Folder : %s ]'%PicsHower.default_savelocation)
		print('\n[!] Just Press CTRL+C to download all the captured links.')
		print('\n\n((Realtime Mode Activated , Now Capturing Upcomming Images Link . .)) \n')
		pass

	def CaptureClipboard(self):
		if len(pyperclip.paste()) > 0:
			link = pyperclip.paste()
			count_items = len(PicsHower.extentions)
			for item in range(count_items):
				if PicsHower.extentions[item] in link:
					print('[>>] Image link captured and ready to download.')
					if 'http:' not in link and 'https:' not in link:
						link = r'https://'+ link
					else:
						pass
					PicsHower.Media_links.append(link)
				else:
					pass
			for check in PicsHower.extentions:
				if check in pyperclip.paste():
					pyperclip.copy('')
				else:
					pass
		pass
	def AttemptDownload(self):
		global decision
		if len(PicsHower.Media_links) == 0:
			self.cmd = input('Enter [Q] for quit. (Any Key To Continue ) > ')
		else:
			self.cmd=input('Are you sure to download %s images ? [Y/N] or [Q] for quit. > '%len(PicsHower.Media_links))
		decision = self.cmd
		if self.cmd == 'y' or self.cmd == 'Y':
			#yes user wants to download all the images.
			for eachimagefile in PicsHower.Media_links:
				PicsHower.Media_links.remove(eachimagefile)
				img_data = requests.get(eachimagefile)
				imagefile = img_data.content
				imagename = eachimagefile.split('/')
				imagecount = len(imagename)-1
				image_name = imagename[imagecount]
				

				if "?" in image_name or "%" in image_name or "=" in image_name:
					#we will give our random name here.
					image_name = str(random.randint(1,1000))+".jpg"
				if getcwd() == PicsHower.default_savelocation:
					pass
				else:
					chdir(PicsHower.default_savelocation)
				iname = image_name
				with open(image_name,'wb') as Image:
					Image.write(imagefile)
				print('[+] File %s saved in %s successfully.'%(image_name,PicsHower.default_savelocation))
			#PicsHower.Media_links.clear()

			pass
		elif self.cmd == 'n' or self.cmd == 'N':
			#no user doesnt want to download all the images.
			pass
		elif self.cmd == 'Q' or self.cmd == 'q':
			quit(1)
		else:
			print('Program will continue..')
		pass
	

Program=PicsHower()
while True:
	try:
		Program.CaptureClipboard()
		time.sleep(2)
	except KeyboardInterrupt:
		try:
			Program.AttemptDownload()
		except requests.exceptions.ConnectionError:
			if decision == 'n' or decision == 'N':
				pass
			else:
				print("[error] Unable To Download Image File From Captured Link.")
	except ImportError:
		print('\n[-] Import Error : This Program requires pyperclip module to operate.')
		print('[!] type-> pip install pyperclip in command line to install that module.')
	except:
		print('\n [unknown error]\n')
		input()
		quit()