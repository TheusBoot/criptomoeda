import hashlib
import binascii


class Transaction:
	def __init__(self):
		self.id = None
		self.inputs = None
		self.outputs = None

class Output:
	def __init__(self, address, amount):
		self.address = address
		self.amount = amount

class Input:
	def __init__(self):
		self.outputID = None
		self.outputIndex = None
		self.signature = None


def iDtTransaction(transaction):
	inputContents = ""
	outputContents = ""
	for inpt in transaction.inputs:
		inputContents += (inpt.outputId + inpt.outputsIndex)

	for output in transaction.outputs:
		outputContents += (output.address + output.amount)

	return hashlib.sha256((str(inputContents) + str(outputContents)).enconde('utf-8')).hexdigest()
