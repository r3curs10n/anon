import cPickle
import os.path

# A decorator to cache the function output values
def cache_it(func):
	def hit_or_miss(*args):

		# hashDict = {'Hashed_value_of_arguments' : 'Corresponding_function_output'}
		hashDict = {}

		sargs = cPickle.dumps(args)

		# Checking whether some cached values exist or not
		# Load the cached values in hashDict
		# The filename storing the dictionary dump
		# will have the same name as the function
		if os.path.isfile(func.__name__):
			with open(func.__name__) as f:
				hashDict = cPickle.load(f)

		# Computing the hash value corresponding to the current
		# function arguments and storing it in curHash
		curHash = hash(sargs)


		# Checking whether the hash exists apriori or not
		# If yes, simply return the output
		if curHash in hashDict:
			return hashDict[curHash]

		# Otherwise, compute the values corresponding to the
		# current input and append it into the dictionary
		# And, finally dump it into the appropriate file
		ret = func(*args)
		hashDict[curHash] = ret
		with open(func.__name__, 'w') as f:
			cPickle.dump(hashDict, f)

		return ret

	return hit_or_miss