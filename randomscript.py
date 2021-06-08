import time
import traceback

from random import uniform

import beepy as beep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

USERNAME = ""
PASSWORD = ""

date_not_found = True

while date_not_found:

	try:

		driver = webdriver.Firefox()

		driver.get("https://sachsen.impfterminvergabe.de/civ.public/start.html?oe=00.00.IM&mode=cc&cc_key=IOAktion")

		warteschlange = True

		while warteschlange:
			try:
				driver.find_element_by_xpath("//*[contains(text(), 'Aufgrund der vielen Anfragen')]")
				print("Waiting patiently")
				time.sleep(10)
			except NoSuchElementException:
				warteschlange = False
			
		time.sleep(uniform(3,7))

		username_field = driver.find_element_by_xpath("(//input)[1]")
		username_field.send_keys(USERNAME)

		password_field = driver.find_element_by_xpath("(//input)[2]")
		password_field.send_keys(PASSWORD)

		time.sleep(uniform(0.5,1.5))

		step1_button = driver.find_element_by_xpath("//button")
		step1_button.click()

		time.sleep(uniform(3,7))

		select = driver.find_element_by_xpath('//span[contains(@class,"gwt-RadioButton")]')
		select.click()


		step2_button = driver.find_element_by_xpath('//button[@class="right btn"]')
		step2_button.click()

		time.sleep(uniform(3,7))

		impfcenter = driver.find_element_by_xpath('//span[contains(@class, "select2")]')
		impfcenter.click()

		time.sleep(uniform(3,7))

		dresden_option = driver.find_element_by_xpath("//li[contains(text(), 'Dresden')]")
		dresden_option.click()


		time.sleep(uniform(3,7))

		while True:

			step3_button = driver.find_element_by_xpath('//button[@class="right btn"]')
			step3_button.click()
			
			time.sleep(uniform(5,15))

			try:
				driver.find_element_by_xpath("//*[contains(text(), 'leider keinen Termin')]")
				step3_button = driver.find_element_by_xpath('//button[@class="btn"]')
				step3_button.click()
			except NoSuchElementException:
				# Success!
				beep.beep(6)
				date_not_found = False
				break

			time.sleep(uniform(30,90))

		driver.close()

	except NoSuchElementException:
		# Loggedout
		pass # beep.beep(7)

