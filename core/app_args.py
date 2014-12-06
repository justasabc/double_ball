#!usr/bin/python
# encoding: utf-8

__all__ = ['usage']

import argparse
from version import * # __app__ __version__

def usage2(): 
	parser = argparse.ArgumentParser(description=__app__,epilog="Thank you for your using this application.If you find any bugs,please contact me at zunlin1234@gmail.com")
	parser.add_argument('-v','--version', action='version', version='{0} {1}'.format(__app__,__version__),help="show program's version number and exit")
	#parser.add_argument('-H','--HELP', action='help', help='show this help message and exit')

	parser.add_argument("-i", "--id",dest="ID",action="store",type=str,help="get record by given id")

	#parser.add_argument("IP", action="store",type=str,help="set ip or ip-range to scan. eg: 1)localhost 2) 192.168.1.200  3) 192.168.200-202 4)192-193.168-170.1-2.200-202")
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


def usage(): 
	parser = argparse.ArgumentParser(description=__app__,epilog="Thank you for your using this application.If you find any bugs,please contact me at zunlin1234@gmail.com")
	parser.add_argument('-v','--version', action='version', version='{0} {1}'.format(__app__,__version__),help="show program's version number and exit")


	group_mode = parser.add_mutually_exclusive_group()
	group_mode.add_argument("-i", "--id",action="store",type=str,help="query record by id [eg. 03088]")
	group_mode.add_argument("-y", "--year",action="store",type=str,help = "query record by year [eg. 2003]")
	group_mode.add_argument("-m", "--year-month", action="store",type=str,help="query record by year and month [eg. 2003,2]")
	group_mode.add_argument("-d", "--year-month-day", action="store",type=str,help="query record by year, month and day [eg. 2003,2,27]")
	group_mode.add_argument("-l", "--list", action="store",type=str,help="query record by list [eg. 10,12,20]")
	group_mode.add_argument("-t", "--test", action="store",type=str,help="test whether number hits [eg. 8,17,21,26,28,29]")

	# parse
	args = parser.parse_args()
	return args

def main():
	args = usage()
	print(args)

	# get params
	if args.id:
		print 'args.id is ok'
	if args.year:
		print 'args.year is ok'
	return

if __name__ == "__main__":
	main()
