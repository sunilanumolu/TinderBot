from selenium import webdriver
from time import sleep
from random import random


class TinderBot():
		def __init__(self):
			self.driver = webdriver.Chrome()
			sleep(8)

		def login(self):
			self.driver.get('https://tinder.com') #opens tinder webpage
			sleep(6)
			accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span')
			accept.click()	#accept cookies
			google_login = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button') 
			#finding google login button
			google_login.click() #opens gmail login page
			main_window = self.driver.window_handles[0] #storing main window id like [CDwindow-B6E413DE38BB4DC355C3B74BB7C243A3]
			popup_window = self.driver.switch_to_window(self.driver.window_handles[1]) #change to popup window
			email_input = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
			email_input.send_keys('sunilanumolu11') #enter mailid
			next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
			next_btn.click()
			sleep(2)
			main_window2 = self.driver.window_handles[0]
			self.driver.switch_to_window(self.driver.window_handles[1]) #change to popup window
			passwd_inp= self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
			passwd_inp.send_keys('linussunil')	#enter password
			next2_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
			next2_btn.click() #login button

			self.driver.switch_to_window(main_window2)
			sleep(10)
			allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
			allow.click()	#allowing location access(uses current location)
			sleep(5)
			notallow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
			notallow.click() #declining notifications
			sleep(5)
			# accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span')
			# accept.click()	#accept cookies
			no_thanks = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button/span')
			no_thanks.click() #declining location settings


		def like(self):
			liked = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
			Iliked.click()

		def dislike(self):
			disliked = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
			Idisliked.click()


		def auto_swipe(self):
			left_cnt,right_cnt = 0,0
			sleep(5)
			while True:
				sleep(2)
				if (left_cnt + right_cnt) > 50:
					return -1
				try:
					rand = random()
					if rand < .67:
						self.like()
						right_cnt = right_cnt + 1
						print('{}th right swipe'.format(right_cnt))
					else:
						self.dislike()
						left_cnt = left_cnt + 1
						print('{}th left swipe'.format(left_cnt))
				except Exception:
					try:
						self.close_popup()
					except Exception:
						self.close_match()

		def close_popup(self):
			sayno = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
			#add xpath (from inspect element) of "no" button
			sayno.click()

		def close_match(self):
			keepon = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
			keepon.click()

		def auto_message(self):
			matches = self.driver.find_element_by_class_name('')[1:]
			if len(matches) < 5:
				return -2
			matches[0].click()
			sleep(1)
			msg_box = self.driver.find_element_by_class_name('')
			msg_box.send_keys('heyahh')
			sleep(1)
			send_btn = self.driver.find_element_by_xpath('')
			send_btn.click()
			sleep(1)
			matches_tab = self.driver.find_element_by_xpath('')
			matches_tab.click()
			sleep(1)

bot = TinderBot()
bot.login()
bot.auto_swipe()
bot.auto_message()









