#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Числа Фибоначчи
"""

class Numbers:

    def fibonachi(self, n):
        if not n:
            return 0
        elif n < 3:
            return 1

        return self.fibonachi(n - 1) + self.fibonachi(n - 2)

    def fibonachi2(self, n):
	f = [0,1] + [0] * (n-1)
	
	for i in range(2, n+1):
	    f[i] = f[i-1] + f[i-2]
	
	return '  ' + str(n) + ' -> ' + str(f[n])

if __name__ == "__main__":
    numObject = Numbers()
    
    for x in range(0, 10):
	#print(numObject.fibonachi(x))
	print(numObject.fibonachi2(x))

