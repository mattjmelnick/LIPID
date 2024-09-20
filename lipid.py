from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import time
import glob

class App(Tk):
	def __init__(self):
		super().__init__()
		self.driver = webdriver.Chrome()

		self.title("LIPID")
		self.geometry("350x250+500+250")
		self.resizable(width=False, height=False)
		self.signin = Frame(self, width=350, height=250)
		self.signin.grid()

		self.create_signin()
	
	def create_signin(self):
		username = Label(self.signin, text="Email")
		username.place(x=30, y=30)

		self.u_entry = Entry(self.signin)
		self.u_entry.place(x=100, y=30, width=175)

		password = Label(self.signin, text="Password")
		password.place(x=30, y=70)

		self.p_entry = Entry(self.signin, show="*")
		self.p_entry.place(x=100, y=70, width=175)

		sign_in = Button(self.signin, text="Sign In", command=self.login)
		sign_in.place(x=50, y=110)

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

		self.folder_frame = Frame(self, width=350, height=250)
		self.folder_frame.grid()

		dl_folder_button = Button(self.folder_frame, text="Select Downloads Folder", command=self.browse_download_folder)
		dl_folder_button.place(x=30, y=30)

		download_label = Label(self.folder_frame, textvariable=self.dl_path)
		download_label.place(x=30, y=70)

	def browse_download_folder(self):
		dl_foldername = filedialog.askdirectory(title="Select Downloads Folder")
		self.dl_path.set(dl_foldername)

		dest_folder = Button(self.folder_frame, text="Select Destination Folder", command=self.browse_destination_folder)
		dest_folder.place(x=30, y=100)
	
	def browse_destination_folder(self):
		dest_foldername = filedialog.askdirectory(title="Select Destination Folder")
		self.dest_path.set(dest_foldername)

		dest_label = Label(self.folder_frame, textvariable=self.dest_path)
		dest_label.place(x=30, y=140)

		download_button = Button(self.folder_frame, text="Download A Profile", command=self.lipid)
		download_button.place(x=30, y=180)
	
	def lipid(self):
		self.top = Toplevel()
		self.top.title("Download Profile")
		self.top.geometry("350x250+850+250")
		self.top.resizable(width=False, height=False)
		self.top.attributes("-topmost", True)

		open_url = Label(self.top, text="Enter URL:")
		open_url.place(x=30, y=20)

		self.url_entry = Entry(self.top)
		self.url_entry.place(x=120, y=20, width=200)

		self.download_profile_button = Button(self.top, text="Download Profile", command=self.dl_profile)
		self.download_profile_button.place(x=30, y=60)

	def dl_profile(self):
		self.dl_path_string = self.dl_path.get() + '/'
		self.dest_path_string = self.dest_path.get() + '/'

		os.chdir(self.dl_path_string)
		before_click = after_click = len(os.listdir(self.dl_path_string))
		self.driver.get(self.url_entry.get())

		more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button")))
		more.click()

		save_to_pdf = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[2]/div")))
		save_to_pdf.click()

		profile_name = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1").text

		extra_characters = r'\/:*?"<>|'

		for c in profile_name:
			if c in extra_characters:
				profile_name = profile_name.replace(c, '.')

		person_name = str(profile_name + ".pdf")

		while before_click == after_click:
			time.sleep(1)
			after_click = len(os.listdir(self.dl_path_string))

		for _ in os.listdir(self.dl_path_string):
			file_path = self.dl_path_string + "*.pdf"
			file_list = glob.iglob(file_path)
			newest_file = max(file_list, key=os.path.getmtime)

		shutil.move(newest_file, self.dest_path_string + person_name)

		download_another_window = Frame(self.top, width=350, height=250)
		download_another_window.grid()

		download_another_button = Button(download_another_window, text="Download Another", command=self.download_another)
		download_another_button.place(x=30, y=30)

		name_area = person_name

		self.name = Label(download_another_window, text=name_area)
		self.name.place(x=130, y=80)

		self.rename_entry = Entry(download_another_window)
		self.rename_entry.place(x=30, y=120, width=175)

		rename_button = Button(download_another_window, text="Rename File", command=self.rename)
		rename_button.place(x=30, y=80)
	
	def download_another(self):
		self.top.destroy()
		self.lipid()
	
	def rename(self):
		for _ in os.listdir(self.dest_path_string):
			file_path = self.dest_path_string + "*.pdf"
			file_list = glob.iglob(file_path)
			newest_file = max(file_list, key=os.path.getmtime)

		rename = self.rename_entry.get()
		name_area = rename + ".pdf"
		self.name.configure(text=name_area)

		shutil.move(newest_file, self.dest_path_string + name_area)
		
if __name__ == "__main__":
	app = App()
	app.mainloop()