#!usr/bin/python
# encoding: utf-8

from pprint import pprint
from core.model import *
from core.app_args import *

input_folder = './data/input/'
output_folder = './data/output/'
# show usage
args = None
args = usage()

def get_rc():
	fr = FileReader()
	filepath = "{0}{1}".format(input_folder,"new_data.txt")
	rc = fr.process(filepath)
	print rc.get_record_count()
	return rc

def test_query(rc):
	record = rc.get_record_by_id('03088')
	if record:
		print record.str()
	print "="*50
	print "geting x records by year,month,day..."
	result = rc.query_by_year(2003)
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	result = rc.query_by_year_month(2003,2)
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	result = rc.query_by_year_month_day(2003,2,27)
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	"""
	print "="*50
	print "geting x record by pos..."
	result = rc.query_by_number_pos(1,1)
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	result = rc.query_by_number_pos(33,6)
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	"""
	print "="*50
	print "geting x record by list..."
	result = rc.query_by_number_list([10,12,20])
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	print "="*50
	print "test numbers..."
	rc.test_number(8,17,21,26,28,29,7)
	rc.test_number(3,7,10,12,20,25,12)
	result = rc.query_by_number_list([8,17,21,26,28,29])
	if result:
		for record in result:
			print record.str()
		print "#{0} records".format( len(result) )
	print "="*50
	print "save results..."
	filepath = "{0}{1}".format(input_folder,"standard_data.txt")
	rc.save(filepath)

def test_stats(rc):
	print "="*50
	st = Stats(rc)
	print "[red]  real:%f, expected:%f " % (st.get_red_sum_avg(),st.get_red_sum_avg_e())
	print "[blue] real:%f, expected:%f " % (st.get_blue_sum_avg(),st.get_blue_sum_avg_e())
	st.save()

def main():
	rc = get_rc()
	#test_query(rc)
	test_stats(rc)

if __name__ == "__main__":
	main()
