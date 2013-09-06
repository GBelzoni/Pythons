
def root2(low,high,tol):

	mid = (low + high)/2
	print mid

	val = mid**2 -2

	if val**2 < tol**2:
		return mid

	elif val < 0:
		low = mid
		res = root2(low,high,tol)
	elif val >0:
		high =mid
		res = root2(low,high,tol)
	return res
	

rt = root2(1.0,2.0,0.001)
print rt

