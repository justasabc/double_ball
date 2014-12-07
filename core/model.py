#!usr/bin/python
# encoding: utf-8

__all__ = ['Record','RecordCollection','FileReader','Stats']

from constants import *

class RedSequence:
	# 10,11,12,13,26,28
	def __init__(self,red_list):
		self.red_list = red_list

# 03001 10 11 12 13 26 28 11 10307806 0 0 898744 1 2003-2-20 2003-2-23
class Record: 
	
	def __init__(self,parts):
		self.__init(parts)
		self.__stats()
		#print self.str()
		#print self.stats_str()

	def __init(self,parts):
		self.id = parts[0]
		self.n1 = int(parts[1])
		self.n2 = int(parts[2])
		self.n3 = int(parts[3])
		self.n4 = int(parts[4])
		self.n5 = int(parts[5])
		self.n6 = int(parts[6])
		self.n7 = int(parts[7])
		self.total_money = int(parts[8])
		self.one_money = int(parts[9])
		self.one_count = int(parts[10])
		self.two_money = int(parts[11])
		self.two_count = int(parts[12])
		self.start_date = parts[13]
		self.end_date = parts[14]

	def __stats(self):
		self.__stats_red_blue()
		self.__stats_red()

	def __stats_red_blue(self):
		self.red_list = [self.n1,self.n2,self.n3,self.n4,self.n5,self.n6]
		self.blue_list = [self.n7]
		self.red_sum = 0
		self.blue_sum = 0
		self.red_01_str = ""
		self.blue_01_str = ""
		self.red_01_count = (0,0)
		self.blue_01_count = (0,0)
		self.red_prim_count = 0
		self.blue_prim_count = 0
		# 1-11, 12-22,23-33
		self.red_3zone_count = (0,0,0)
		# 1-8, 9-16
		self.blue_2zone_count = (0,0)

		# get stats
		# red
		c0 = 0
		c1 = 0
		prim = 0
		for n in self.red_list:
			self.red_sum += n 
			if n%2==0:
				self.red_01_str += '0'
				c0 += 1
			else:
				self.red_01_str += '1'
				c1 += 1
			# red prim
			if n in RED_PRIM_LIST:
				prim += 1
		self.red_01_count = (c0,c1)
		self.red_prim_count = prim

		# blue
		c0 = 0
		c1 = 0
		prim = 0
		for n in self.blue_list:
			self.blue_sum += n 
			if n%2==0:
				self.blue_01_str += '0'
				c0 += 1
			else:
				self.blue_01_str += '1'
				c1 += 1
			# blue prim
			if n in BLUE_PRIM_LIST:
				prim += 1
		self.blue_01_count = (c0,c1)
		self.blue_prim_count = prim

		# zone stats
		# red
		zone1 = 0
		zone2 = 0
		zone3 = 0
		for n in self.red_list:
			if n>=RED_ZONE1[0] and n<=RED_ZONE1[1]:
				zone1 +=1
			elif n>=RED_ZONE2[0] and n<=RED_ZONE2[1]:
				zone2 +=1
			elif n>=RED_ZONE3[0] and n<=RED_ZONE3[1]:
				zone3 +=1
		self.red_3zone_count = (zone1,zone2,zone3)

		# blue
		zone1 = 0
		zone2 = 0
		for n in self.blue_list:
			if n>=BLUE_ZONE1[0] and n<=BLUE_ZONE1[1]:
				zone1 +=1
			elif n>=BLUE_ZONE2[0] and n<=BLUE_ZONE2[1]:
				zone2 +=1
		self.blue_2zone_count = (zone1,zone2)

	def __stats_red(self):
		# (1) red shift to base
		# 2,13,17,20,25,33===>11,15,18,23,31
		self.red_shift_to_base = []
		for n in self.red_list[1:]:
			self.red_shift_to_base.append(n-self.red_list[0])

		# (2) red head-tail width 
		self.red_width = self.n6-self.n1
		# (3) red delta 
		# 2,13,17,20,25,33===> 11,4,3,5,8
		self.red_delta = []
		for i in range(1,len(self.red_list)):
			self.red_delta.append(self.red_list[i]-self.red_list[i-1])

	def stats_str(self):
		return "<stats>\n [red]  sum={0} 01_str={1} 01_count={2} prim={3}\n [blue] sum={4} 01_str={5} 01_count={6} prim={7}\n 3zone = {8}".format(self.red_sum,self.red_01_str,self.red_01_count,self.red_prim_count,
			self.blue_sum,self.blue_01_str,self.blue_01_count,self.blue_prim_count,
			self.red_3zone_count)

	def __fn(self,number):
		return "%02d" % number
		
	def long_str(self):
		return "{0} [{1} {2} {3} {4} {5} {6} {7}] {8} {9} {10} {11} {12} {13} {14}".format(self.id,self.n1,self.n2,self.n3,self.n4,self.n5,self.n6,self.n7,self.total_money,self.one_money,self.one_count,self.two_money,self.two_count,self.start_date,self.end_date)

	def short_str(self):
		#return "{0} [{1} {2} {3} {4} {5} {6} {7}] {8}/{9}".format(self.id,self.__fn(self.n1),self.__fn(self.n2),self.__fn(self.n3),self.__fn(self.n4),self.__fn(self.n5),self.__fn(self.n6),self.__fn(self.n7),self.start_date,self.end_date)
		return "{0} [{1} {2} {3} {4} {5} {6} {7}] {8}".format(self.id,self.__fn(self.n1),self.__fn(self.n2),self.__fn(self.n3),self.__fn(self.n4),self.__fn(self.n5),self.__fn(self.n6),self.__fn(self.n7),self.end_date)

	def str(self):
		return self.short_str()

	def __str__(self):
		return self.long_str()

class RecordCollection:

	def __init__(self):
		self.records = []

	def get_records(self):
		return self.records

	def get_record_count(self):
		return len(self.records)

	def add_record(self,record):
		self.records.append(record)

	def get_record_by_id(self,id):
		# 03088 
		if(len(id)!=5):
			print "Error. invalid id %s".format(id)
			return None
		for record in self.records:
			if id == record.id:
				return record
		print "Warning. can not find record id =%s".format(id)
		return None

	"""
	print record 
	"""
	def print_record(self,record):
		if record:
			print record.str()

	"""
	print record list
	"""
	def print_records(self,record_list):
		if record_list:
			for record in record_list:
				print record.str()
			print "#{0} records".format( len(record_list) )

	"""
	querying methods:
	return a list of record
	"""
	def query_by_year(self,year):
		# 2003,2009--->03,09
		# 2010,2011--->10,11	
		if(year<START_YEAR or len(str(year))!=4):
			print "Error. invalid year {0}".format(year)
			return None
		str_year = str(year)
		year = str_year[-2:]
		result = []
		for record in self.records:
			if (year == record.id[:2]):
				result.append(record)
		return result	

	def query_by_year_month(self,year,month):
		# 2003,2
		# '2003-2-23' '2003-2-27'
		if(year<START_YEAR or len(str(year))!=4):
			print "Error. invalid year {0}".format(year)
			return None
		if(month<1 or month>MONTH):
			print "Error. invalid month {0}".format(month)
			return None
		result = []
		for record in self.records:
			parts = record.end_date.split("-")
			if year==int(parts[0]) and month == int(parts[1]) :
				result.append(record)
		return result	

	def __x_query_by_date(self,date):
		# '2003-9-4'
		for record in self.records:
			if (date == record.end_date):
				return [record]
		print "Warning. can not find record id =%s".format(id)
		return None

	def query_by_year_month_day(self,year,month,day):
		# 2003,2,23
		# '2003-2-23' 
		if(year<START_YEAR or len(str(year))!=4):
			print "Error. invalid year {0}".format(year)
			return None
		if(month<1 or month>MONTH):
			print "Error. invalid month {0}".format(month)
			return None
		if(day<1 or day>31):
			print "Error. invalid day {0}".format(day)
			return None
		date = '{0}-{1}-{2}'.format(year,month,day)
		return self.__x_query_by_date(date)

	def __x_query_by_number_pos_1(self,n):
		result = []
		for record in self.records:
			if n == record.n1 :
				result.append(record)	
		return result
	def __x_query_by_number_pos_2(self,n):
		result = []
		for record in self.records:
			if n == record.n2 :
				result.append(record)	
		return result
	def __x_query_by_number_pos_3(self,n):
		result = []
		for record in self.records:
			if n == record.n3 :
				result.append(record)	
		return result
	def __x_query_by_number_pos_4(self,n):
		result = []
		for record in self.records:
			if n == record.n4 :
				result.append(record)	
		return result
	def __x_query_by_number_pos_5(self,n):
		result = []
		for record in self.records:
			if n == record.n5 :
				result.append(record)	
		return result
	def __x_query_by_number_pos_6(self,n):
		result = []
		for record in self.records:
			if n == record.n6 :
				result.append(record)	
		return result
	def __x_query_by_number_pos_7(self,n):
		result = []
		for record in self.records:
			if n == record.n7 :
				result.append(record)	
		return result

	def query_by_number_pos(self,n,pos):
		# pos = 1,2,3,4,5,6,7
		if(pos<1 or pos>7):
			print 'Error. valid pos is 1-7.'
			return None

		if(pos==7):
			if (n>BLUE_MAX_NUMBER):
				print "Error. blue number >=%s" % BLUE_MAX_NUMBER
				return None
		else:
			if (n>RED_MAX_NUMBER):
				print "Error. red number >=%s" % RED_MAX_NUMBER
				return None

		methods = {
			1:self.__x_query_by_number_pos_1,
			2:self.__x_query_by_number_pos_2,
			3:self.__x_query_by_number_pos_3,
			4:self.__x_query_by_number_pos_4,
			5:self.__x_query_by_number_pos_5,
			6:self.__x_query_by_number_pos_6,
			7:self.__x_query_by_number_pos_7
			}		
		return methods[pos](n)

	def save(self,filepath):
		with open(filepath,'w') as f:
			for record in self.records:
				line = record.str()+"\n"
				f.write(line)
		print "generated {0}.".format(filepath)

	def query_by_number_list(self,number_list):
		if(len(number_list)>7):
			print "Error. number list count>7"
			return None
		result = []
		for record in self.records:
			list7 = [record.n1,record.n2,record.n3,record.n4,record.n5,record.n6,record.n7]
			base_set = set(list7)
			query_set = set(number_list)
			if query_set.issubset(base_set):
				result.append(record)
		return result

	def test_number(self,n1,n2,n3,n4,n5,n6,n7):
		#03056 08 17 21 26 28 29 07 32664536 5000000 1 557563 3 2003-8-31 2003-9-4
		#result = query_by_number_list([n1,n2,n3,n4,n5,n6,n7])
		for record in self.records:
			if (n1==record.n1 and n2==record.n2 and n3==record.n3 and n4==record.n4
				and n5==record.n5 and n6==record.n6 and n7==record.n7):
				print 'Hit. [{0} {1} {2} {3} {4} {5} {6}] at {7} on {8}'.format(n1,n2,n3,n4,n5,n6,n7,record.id,record.end_date)
				return True
		print 'NO Hit. [{0} {1} {2} {3} {4} {5} {6}]'.format(n1,n2,n3,n4,n5,n6,n7)
		return False

class FileReader:

	def __init__(self):
		self.sep = ' '

	def process(self,filepath):
		rc = RecordCollection()
		for line in open(filepath,'r'):
			parts = line.strip('\n').split(self.sep)
			if(len(parts)!=RECORD_FIELD):
				print "ERROR. record field %d!" % len(parts)
				return None
			record = Record(parts)
			rc.add_record(record)
		return rc

class Stats:

	def __init__(self,rc):
		self.__init(rc)

	def __init(self,rc):
		self.rc = rc

		# red stats
		self.red_sum_list = []
		self.red_01_str_list = []
		self.red_01_count_list = []
		self.red_prim_count_list = []
		self.red_3zone_count_list = []
		self.__get_red_xxx_list()

		# blue stats
		self.blue_sum_list = []
		self.blue_01_str_list = []
		self.blue_01_count_list = []
		self.blue_prim_count_list = []
		self.blue_2zone_count_list = []
		self.__get_blue_xxx_list()

		# avg avg_e
		self.red_sum_avg = self.__avg_list(self.red_sum_list)
		self.blue_sum_avg = self.__avg_list(self.blue_sum_list)
		self.red_sum_avg_e = (RED_MIN_NUMBER + RED_MAX_NUMBER)*RED_COUNT/2.0
		self.blue_sum_avg_e = (BLUE_MIN_NUMBER + BLUE_MAX_NUMBER)*BLUE_COUNT/2.0

		# red only
		self.red_shift_to_base_list = []
		self.red_width_list = []
		self.red_delta_list = []
		self.__get_red_only_list()
		self.red_width_avg = self.__avg_list(self.red_width_list)

		# red/blue prim pair
		self.prim_count_list = zip(self.red_prim_count_list,self.blue_prim_count_list)

	def __avg_list(self,list):
		count = len(list)
		if(count==0):
			return 0.0
		total_sum = 0
		for n in list:
			total_sum += n
		return total_sum*1.0/count

	def __inf(self,filename):
		return "{0}{1}".format(INPUT_FOLDER,filename)

	def __outf(self,filename):
		return "{0}{1}".format(OUTPUT_FOLDER,filename)

	def __save_list(self,filename,list):
		filepath = self.__outf(filename)
		with open(filepath,'w') as f:
			for item in list:
				line = str(item)+"\n"
				f.write(line)
		print "saved {0}.".format(filepath)

	def save(self):
		self.__save_list('red_sum_list',self.red_sum_list)
		self.__save_list('blue_sum_list',self.blue_sum_list)
		self.__save_list('red_01_str_list',self.red_01_str_list)
		self.__save_list('blue_01_str_list',self.blue_01_str_list)
		self.__save_list('red_01_count_list',self.red_01_count_list)
		self.__save_list('blue_01_count_list',self.blue_01_count_list)
		self.__save_list('red_prim_count_list',self.red_prim_count_list)
		self.__save_list('blue_prim_count_list',self.blue_prim_count_list)
		self.__save_list('prim_count_list',self.prim_count_list)
		self.__save_list('red_3zone_count_list',self.red_3zone_count_list)
		self.__save_list('blue_2zone_count_list',self.blue_2zone_count_list)

		# red only
		self.__save_list('red_shift_to_base_list',self.red_shift_to_base_list)
		self.__save_list('red_width_list',self.red_width_list)
		self.__save_list('red_delta_list',self.red_delta_list)

	"""
	get red xxx list
	"""
	def __get_red_xxx_list(self):
		for record in self.rc.get_records():
			self.red_sum_list.append(record.red_sum)
			self.red_01_str_list.append(record.red_01_str)
			self.red_01_count_list.append(record.red_01_count)
			self.red_prim_count_list.append(record.red_prim_count)
			self.red_3zone_count_list.append(record.red_3zone_count)

	"""
	get blue  xxx list
	"""
	def __get_blue_xxx_list(self):
		for record in self.rc.get_records():
			self.blue_sum_list.append(record.blue_sum)
			self.blue_01_str_list.append(record.blue_01_str)
			self.blue_01_count_list.append(record.blue_01_count)
			self.blue_prim_count_list.append(record.blue_prim_count)
			self.blue_2zone_count_list.append(record.blue_2zone_count)

	def get_red_sum_avg_e(self):
		return self.red_sum_avg_e

	def get_red_sum_avg(self):
		return self.red_sum_avg

	def get_blue_sum_avg_e(self):
		return self.blue_sum_avg_e

	def get_blue_sum_avg(self):
		return self.blue_sum_avg

	"""
	red related methods
	"""
	def __get_red_only_list(self):
		for record in self.rc.get_records():
			self.red_shift_to_base_list.append(record.red_shift_to_base)
			self.red_width_list.append(record.red_width)
			self.red_delta_list.append(record.red_delta)

	def get_red_width_avg(self):
		return self.red_width_avg
