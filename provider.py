#provider.py
#Hides provider-specific details for the main csvtoqbo method.

class csvprovider:

	name = ''

	def __init__(self, providername):
		if providername in ('amazon'):
			self.name = providername
		else:
			raise Exception("Provider '%s' not supported." % providername)

	def getName(self):
		if self.name == 'amazon':
			return 'Amazon Payments'
		else:
			raise Exception("Provider '%s' not supported." % self.name)

	@staticmethod
	def getStatus(self,row):
		if self.name == 'amazon':
			return row.get('Status')
		else:
			raise Exception("getStatus: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getDatePosted(self, row):
		if self.name == 'amazon':
			return row.get('Date')
		else:
			raise Exception("getDatePosted: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getTxnType(self,row):
		if self.name == 'amazon':
			return row.get('Type')
		else:
			raise Exception("getTxnType: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getToFrom(self,row):
		if self.name == 'amazon':
			return row.get('To/From')
		else:
			raise Exception("getToFrom: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getTxnAmount(self,row):
		if self.name == 'amazon':
			return row.get('Amount')
		else:
			raise Exception("getTxnAmount: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getTxnName(self,row):
		if self.name == 'amazon':
			return row.get('Name')
		else:
			raise Exception("getName: Defined provider '%s' not handled." % self.name)
