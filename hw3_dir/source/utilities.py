import re
import transitionState

class Utilities:
	def __init__(self):
		self.what = 'what'

	def cleanseInput(self, strVal):
		return re.sub(r'\"', '', re.sub(r'\'', '', strVal))

	def valsBeforeParen(self, strVal):
		parenIdx = len(strVal)

		for i in range(0, len(strVal)):
			if(strVal[i] == '('):
				parenIdx = i
				break

		subStr = strVal[0:parenIdx]
		return re.split("\s+", subStr)

	def parenIndex(self, strVal):
		parenStart = -1
		leftParenCount = 0

		for i in range(0, len(strVal)):
			currentChar = strVal[i]

			if(currentChar == '('):
				
				if(parenStart == -1):
					parenStart = i
				
				leftParenCount = leftParenCount + 1
			elif(currentChar == ')'):
				leftParenCount = leftParenCount - 1

				if(leftParenCount == 0):
					# dictionary fine
					return { 'start': parenStart+1, 'end': i }

		return { 'start': -1, 'end': -1 }

	def createTransitionState(self, strVal):
		parenIndexes = self.parenIndex(strVal)

		if(parenIndexes['start'] == -1):
			return {}

		# business rules
		# 1) identify where the paren is
		# 2) get the first item
		# 3) get the next paren list
		# 4) get list of those items, they will be in the second level

		fromStateSubStr = strVal[parenIndexes['start']:parenIndexes['end']]
		fromStateValues = self.valsBeforeParen(fromStateSubStr)

		otherParenIndexes = self.parenIndex(fromStateSubStr)

		toStateSubStr = fromStateSubStr[otherParenIndexes['start']:otherParenIndexes['end']]
		toStateValues = self.valsBeforeParen(toStateSubStr)

		return transitionState.TransitionState(
			fromStateValues.pop(0),
			toStateValues.pop(0), 
			self.cleanseInput(toStateValues.pop(0)), 
			toStateValues)