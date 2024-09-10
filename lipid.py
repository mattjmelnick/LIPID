from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import shutil
import time
import glob

# global dl_path
# global dest_path

# def login():
# 	global driver
# 	driver = webdriver.Chrome()
# 	url = "https://www.linkedin.com/login"
# 	driver.get(url)
# 	username_entry = driver.find_element_by_id("username")
# 	password_entry = driver.find_element_by_id("password")
# 	user = u_entry.get()
# 	pw = p_entry.get()
# 	username_entry.send_keys(user)
# 	password_entry.send_keys(pw)
# 	si_button = driver.find_element_by_class_name("login__form_action_container")
# 	si_button.click()
# 	try:
# 		error = driver.find_element_by_id("error-for-username")
# 		tryagain = Label(signin, text = "Try Again")
# 		tryagain.place(x = 50, y = 120)
# 		time.sleep(2)
# 		driver.close()

# 	except NoSuchElementException:
# 		main_window()

# def main_window():
# 	signin.destroy()
# 	mw = Frame(root, width = 300, height = 150)
# 	mw.grid()

# 	def browse_dl():
# 		foldername = filedialog.askdirectory(title = "Select Downloads Folder")
# 		dl_path.set(foldername)

# 		def browse_dest():
# 			foldername2 = filedialog.askdirectory(title = "Select Destination Folder")
# 			dest_path.set(foldername2)
# 			dest_label = Label(mw, textvariable = dest_path)
# 			dest_label.place(x = 20, y = 85)
# 			download = Button(mw, text = "Download A Profile", command = lipd)
# 			download.place(x = 30, y = 110)

# 		dest_folder = Button(mw, text = "Select Destination Folder", command = browse_dest)
# 		dest_folder.place(x = 30, y = 60)

# 	dl_path = StringVar()
# 	dest_path = StringVar()
# 	dl_label = Label(mw, textvariable = dl_path)
# 	dl_label.place(x = 20, y = 35 )	
# 	dl_folder = Button(mw, text = "Select Downloads Folder", command = browse_dl)
# 	dl_folder.place(x = 30, y = 10)

# 	def quit_chrome():
# 		driver.quit()
# 		root.destroy()

# 	quit_button = Button(mw, text = "Quit", command = quit_chrome)
# 	quit_button.place(x = 250, y = 110)

# 	def lipd():
# 		top = Toplevel()
# 		top.title("Download Profile")
# 		top.geometry("300x150+800+250")
# 		top.resizable(width = False, height = False)
# 		top.attributes("-topmost", True)

# 		open_url = Label(top, text = "Enter URL:")
# 		open_url.place(x = 30, y = 20)

# 		global url_entry

# 		url_entry = Entry(top)
# 		url_entry.place(x = 100, y = 20, width = 150)
		
# 		def dl_profile():
# 			dl_path_string = dl_path.get() + "/"
# 			dest_path_string = dest_path.get() + "/"
# 			os.chdir(dl_path_string)
# 			before_click = after_click = len(os.listdir(dl_path_string))
# 			driver.get(url_entry.get())
# 			more = driver.find_element_by_class_name("ml2.pv-s-profile-actions__overflow-toggle.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view")
# 			more.click()
# 			save_to_pdf = WebDriverWait(driver, 10).until(
# 				EC.element_to_be_clickable((By.CLASS_NAME, "pv-s-profile-actions.pv-s-profile-actions--save-to-pdf.pv-s-profile-actions__overflow-button.full-width.text-align-left.ember-view")))
# 			save_to_pdf.click()
# 			profile_name = driver.find_element_by_class_name("inline.t-24.t-black.t-normal.break-words").text
# 			person_name = str(profile_name + ".pdf")
# 			extra_characters = '\/:*?"<>|'
# 			for c in extra_characters:
# 				if c in person_name:
# 					person_name = person_name.replace(c, ".")
# 			while before_click == after_click:
# 				time.sleep(1)
# 				after_click = len(os.listdir(dl_path_string))

# 			for file in os.listdir(dl_path_string):
# 				file_path = dl_path_string + "*.pdf"
# 				file_list = glob.iglob(file_path)
# 				newest_file = max(file_list, key = os.path.getmtime)
# 			shutil.move(newest_file, dest_path_string + person_name)
			
# 			rw = Frame(top, width = 300, height = 150)
# 			rw.grid()

# 			def download_another():
# 				lipd()
# 				top.destroy()

# 			download_another_button = Button(rw, text = "Download Another", command = download_another)
# 			download_another_button.place(x = 30, y = 30)

# 			name_area = person_name
			
# 			name = Label(rw, text = name_area) #First file name with profile name
# 			name.place(x = 120, y = 60)

# 			rename_entry = Entry(rw)
# 			rename_entry.place(x = 30, y = 90)

# 			def rename():
# 				for file in os.listdir(dest_path_string):
# 					file_path = dest_path_string + "*.pdf"
# 					file_list = glob.iglob(file_path)
# 					old_file = max(file_list, key = os.path.getmtime)
# 				rename = rename_entry.get()
# 				name_area = rename + ".pdf"
# 				name.configure(text = name_area)
# 				shutil.move(old_file, dest_path_string + name_area)
			 	
# 			rename_file_button = Button(rw, text = "Rename File", command = rename)
# 			rename_file_button.place(x = 30, y = 60)

# 		download_profile_button = Button(top, text = "Download Profile", command = dl_profile)
# 		download_profile_button.place(x = 30, y = 66)

# root = Tk()
# root.title("LIPD")
# root.geometry("300x150+500+250")
# root.resizable(width = False, height = False)
# root.attributes("-topmost", True)
# signin = Frame(root, width = 300, height = 150)
# signin.grid()

# username = Label(signin, text = "Email")
# username.place(x = 30, y = 20)

# u_entry = Entry(signin)
# u_entry.place(x = 100, y = 20, width = 150)

# password = Label(signin, text = "Password")
# password.place(x = 30, y = 50)

# p_entry = Entry(signin, show = "*")
# p_entry.place(x = 100, y = 50, width = 150)

# sign_in = Button(signin, text = "Sign In", command = login)
# sign_in.place(x = 50, y = 80)

# root.mainloop()

class App(Tk):
	def __init__(self):
		super().__init__()
		self.title("LIPID")
		self.geometry("300x150+500+250")
		self.resizable(width=False, height=False)
		self.signin = Frame(self, width=300, height=150)
		self.signin.grid()

		self.create_signin()
	
		self.driver = webdriver.Chrome()

	def create_signin(self):
		username = Label(self.signin, text="Email")
		username.place(x=30, y=20)

		self.u_entry = Entry(self.signin)
		self.u_entry.place(x=100, y=20, width=150)

		password = Label(self.signin, text="Password")
		password.place(x=30, y=50)

		self.p_entry = Entry(self.signin, show="*")
		self.p_entry.place(x=100, y=50, width=150)

		sign_in = Button(self.signin, text="Sign In", command=self.login)
		sign_in.place(x=50, y=80)

	def login(self):
		login_url = "https://www.linkedin.com/login"
		self.driver.get(login_url)
		username_entry = self.driver.find_element(By.XPATH, "//*[@id='username']")
		password_entry = self.driver.find_element(By.XPATH, "//*[@id='password']")
		user = self.u_entry.get()
		pw = self.p_entry.get()
		username_entry.send_keys(user)
		password_entry.send_keys(pw)
		signin_button = self.driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
		signin_button.click()

		self.folder_window()

	def folder_window(self):
		self.signin.destroy()
		self.dl_path = StringVar()
		self.dest_path = StringVar()
		self.folder_frame = Frame(self, width=300, height=150)
		self.folder_frame.grid()
		download_label = Label(self.folder_frame, textvariable=self.dl_path)
		download_label.place(x=20, y=35)
		dl_folder_button = Button(self.folder_frame, text="Select Downloads Folder", command=self.browse_download_folder)
		dl_folder_button.place(x=30, y=10)

	def browse_download_folder(self):
		dl_foldername = filedialog.askdirectory(title="Select Downloads Folder")
		self.dl_path.set(dl_foldername)
		dest_folder = Button(self.folder_frame, text="Select Destination Folder", command=self.browse_destination_folder)
		dest_folder.place(x=30, y=60)
	
	def browse_destination_folder(self):
		dest_foldername = filedialog.askdirectory(title="Select Destination Folder")
		self.dest_path.set(dest_foldername)
		dest_label = Label(self.folder_frame, textvariable=self.dest_path)
		dest_label.place(x=20, y=85)
		download_button = Button(self.folder_frame, text="Download A Profile", command=self.lipid)
		download_button.place(x=30, y=110)
	
	def lipid(self):
		pass

if __name__ == "__main__":
	app = App()
	app.mainloop()