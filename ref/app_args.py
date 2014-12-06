# provide app argument parsing values

__all__ = ['usage']

import argparse
from version import * # __app__ __version__

def usage(): 
	parser = argparse.ArgumentParser(description=__app__,epilog="Thank you for your using this application.If you find any bugs,please contact me at zunlin1234@gmail.com")
	parser.add_argument('-v','--version', action='version', version='{0} {1}'.format(__app__,__version__),help="show program's version number and exit")
	#parser.add_argument('-H','--HELP', action='help', help='show this help message and exit')
	parser.add_argument("IP", action="store",type=str,help="set ip or ip-range to scan. eg: 1)localhost 2) 192.168.1.200  3) 192.168.200-202 4)192-193.168-170.1-2.200-202")
	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-c", "--console",action="store_true", help = "run application in console mode(default)" )
	group_mode.add_argument("-g", "--gui", action = "store_true", help="run application in gui mode(to be done in the future...)")

	parser.add_argument("-f", "--file",dest="FILE",action="store",type=str,help="save scan result to FILE")
	parser.add_argument("-p", "--progress-bar",dest="progress_bar",action="store_true",help="show progress bar while processing")
	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-w", "--well-known",dest="well_known",action="store_true", help = "scan port which is less than well-known port 1024 (default)" )
	group_mode.add_argument("-m", "--max-port",dest="max_port", action = "store_true", help="scan port which is less than max-port 65535(may be slow)")
	args = parser.parse_args()
	return args

def main():
	args = usage()
	print(args)

if __name__ == "__main__":
	main()
