from Cache import cache_it

@cache_it
def sum(a, b):
	return (a + b)

print "Sum is %s" % sum(2, 3)
print "Sum is %s" % sum(2, 3)
print "Sum is %s" % sum(4, 3)
print "Sum is %s" % sum(4, 3)
