
import bs4 as bs
from termcolor import colored
from urllib.error import HTTPError
import urllib.request
import time,sys,os

def LinkGrabber():
	try:
		os.system("clear")
		print(colored("""
{
                                                                     
########                                                     
##      ## *************************************             
#       ##    __Tutorial/Channel__[youtube.com/anonymousbghh]
########                                                     
########                                                     
#       ##    __Repository__[https://github.com/josifkhan/]  
##      ##    __Author_Name__[MD Josif Khan]                 
########_______________}                                     
                                                                             
     _________                    ________________________________
                                            BANgLADESH           
                                                V1.0 """, """red"""))

		targetSite=input(colored("Enter URL: ", """blue"""))
		if targetSite=="":
			print(colored("Target not specified.", "red"))
			time.sleep(2)
			sys.exit()
		print(colored("\nResulting...", "red"))
		sauce = urllib.request.urlopen(targetSite).read()
		soup = bs.BeautifulSoup(sauce, 'lxml')
		for s in soup.find_all('a'):
			save=open("./Logs.txt", "a")
			x=save.write("\n"+s.get('href'))
			print(s.get('href'))
		print(colored("\n Total Links & Directories Found: \nOpen Logs.txt for entire results.","red"))

	except urllib.error.HTTPError:
		print(colored("  Oops...Server refused request, network error:\n", "red"))
		sys.exit()

	except urllib.error.URLError:

		print("  Oops...Third party domain may not supported for this operation.\nTry another domain url.")
		sys.exit()
	except ValueError:
		print(colored(f"Invalid website link, try with http://{targetSite} or https://{targetSite}", "red"))

	except TypeError:
		print(colored("\n Total Links & Directories Found: \nOpen Logs.txt for entire results.","red"))
LinkGrabber()



