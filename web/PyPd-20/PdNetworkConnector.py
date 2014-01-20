from Pd import PdSend, PdReceive, poll

class PdNetworkConnector:
	""" Connect to an existing Pd process. """
	def __init__(self, port=30321):
		self.port = port
		self._map = {}
		self._pdSend = PdSend(map=self._map)
		self._pdReceive = PdReceive(self, map=self._map)

	def Update(self):
		poll(map=self._map)
	
	def Send(self, msg):
		"""
		Send an array of data to Pd.
		It will arrive at the [python-interface] object as a space delimited list.
		
		p.Send(["my", "test", "yay"])
		"""
		self._pdSend.Send(msg)
	
	def PdMessage(self, data):
		"""
		Override this method to receive messages from Pd.
		"""
		print "untrapped message:", data
	
	def Connect(self, addr):
		self._pdSend.Connect((addr[0], self.port))
	
	def Error(self, error):
		"""
		Override this to catch anything sent by Pd to stderr (e.g. [print] objects).
		"""
		errors = error.split(" ")
		method = getattr(self, 'Error_' + errors[0], None)
		if method:
			method(errors)
		elif error in self.errorCallbacks:
			self.errorCallbacks[error]()
		else:
			print 'untrapped stderr output: "' + error + '"'

if __name__ == "__main__":
	from time import sleep
	connector = PdNetworkConnector()
	
	counter = 0
	while 1:
		sleep(0.01)
		connector.Update()
		if not counter % 500:
			connector.Send(["this", "is", "a", "test"])
		counter += 1
