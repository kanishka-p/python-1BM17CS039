class callDetail:
	def __init__(self,caller,called,duration,calltype):
		self.c1=caller
		self.c2=called
		self.d1=duration
		self.ct1=calltype
	def disp(self):
		print(self.c1,self.c2,self.d1,self.ct1)

class util:
	def __init__(self):

		self.list_of_call_objects=[]

	def parse_customer(self,list_of_call_string):

		
		
		for i in list_of_call_string:
			x=i.split(",")
			callobj=callDetail(x[0],x[1],x[2],x[3])
			self.list_of_call_objects.append(callobj)
	def print_details(self):
		for x in self.list_of_call_objects:
			x.disp()
			
			

call='9990000001,9330000001,23,STD'

call2='9990000001,9330000002,54,Local'

call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]

util().parse_customer(list_of_call_string)
ob=util()
ob.parse_customer(list_of_call_string)
ob.print_details()
