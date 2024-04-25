import sys
import os
from api import Api
from geetest import dealCode

if not os.path.exists("config.txt"):
	print("config.txt文件缺失。已自动创建。")
	f = open("config.txt","w")
	f.write("proxies = None\nspecificID = None\nsleep = 0.1\ntoken = None")
	f.close()

a = open("config.txt","r").readlines()
proxies = None if a[0].split("=")[1].strip() == "None" else a[0].split("=")[1].strip()
specificID = None if a[1].split("=")[1].strip() == "None" else a[1].split("=")[1].strip()
sleep = eval(a[2].split("=")[1].strip())
token = None if a[3].split("=")[1].strip() == "None" else a[3].split("=")[1].strip()

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("--headless", action="store_true",
						help="run in headless mode")
	args = parser.parse_args()
	if not os.path.exists("url"):
		with open("url","w") as f:
			f.write("")
	api=Api(proxies=proxies,specificID=specificID,sleepTime=sleep,token=token,headless=args.headless)
	try:
		api.start()
	except KeyboardInterrupt:
		api.life=False
		print("退出")
