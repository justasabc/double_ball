#!/usr/bin/env python
"""Python Port Scanner: scan given address for open ports."""

import sys
import os
# user defined
from settings import *
from core.app_args import *
from core.utils import *
from core.port_config import PortConfig
from core.ipparser import IPParser
from core.progressbar import ProgressBar

# show usage
args = None
args = usage()

def process_one(ip,maxport,filename,con,progress_bar):
	"""
	process give ip
	"""
	lines = ""
	# Check if the host is up first
	if (is_host_up(ip) == False):
		msg = ("DOWN: {0} is down").format(ip)
		lines = lines + msg + os.linesep
		print(msg)
		return	

	msg = ('Starting scan on host: {0}'.format(ip))
	lines = lines + msg + os.linesep
	print(msg)
	open_ports = {}
	if progress_bar:
		pb = ProgressBar(maxport)
		for i in range(maxport+1):
			pb.update_time(i)
			if(scan_port(ip, i)):
				# right justify for sorting
				open_ports[str(i).rjust(5, '0')] = con.get(i)
	else:
		for i in range(maxport+1):
			if(scan_port(ip, i)):
				# right justify for sorting
				open_ports[str(i).rjust(5, '0')] = con.get(i)

	for port in sorted(open_ports.iterkeys()):
		p5 = str(int(port)).rjust(5,' ')
		msg = ("Port ({0}): {1}".format( p5, open_ports[port]))
		lines = lines + msg + os.linesep
		print(msg)

	# save results to file
	if filename:
		with open(filename,'a') as f:
			f.write(lines)

def console_main():
	# get params
	IP = args.IP
	progress_bar = args.progress_bar
	maxport = WELL_KNOWN 
	if args.max_port:
		maxport = MAX_PORT
		# if use MAX_PORT, then show progress bar
		progress_bar = True
	filename = None
	if args.FILE and args.FILE.strip():
		filename = args.FILE.strip()
		if not inside('.',filename):
			sys.stderr.write("ERROR: file must be inside current folder"+os.linesep)
			sys.exit(1)
	# Load Configuration
	# use path relative ROOT_DIR
	portfile = 'core/ports.ini'
	portpath = os.path.join(ROOT_DIR,portfile)
	con = PortConfig(portpath)

	parser = IPParser(IP)
	ips = parser.parse()
	if len(ips)<1:
		sys.stderr.write("ERROR: invaid ips"+os.linesep)
		sys.exit(1)

	for ip in ips:
		process_one(ip,maxport,filename,con,progress_bar)

def run():
	console_main()

if __name__ == "__main__":
	run()
