#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Поиск в глубину

import time

class depthSearch:

    def timing(f):
        def wrap(*args):
            time_start = time.time()
            ret = f(*args)
            time_end = time.time()
            print '%s function took %0.5f ms' % (f.func_name, (time_end - time_start) * 1000.0)
            return ret
        return wrap
    #end def

    @timing
    def countAreas(self, data = []):
        count = 0

        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] == 1:
                        count += 1
                        self.moveArea(data, i, j)

        return count
    #end def

    def moveArea(self, data, i, j):
        data[i][j] = 2;

        if (j + 1 < len(data[i])) and (data[i][j + 1] == 1):
            self.moveArea(data, i, j + 1)
        elif (j - 1 >= 0) and (data[i][j - 1] == 1):
            self.moveArea(data, i, j - 1)
        elif (i + 1 < len(data)) and (data[i + 1][j] == 1):
            self.moveArea(data, i + 1, j)
        elif (i - 1 >= 0) and (data[i - 1][j] == 1):
            self.moveArea(data, i - 1, j)
    #end def
#end class

searchObject = depthSearch()

data = [
	[1,1,0,0,0],
	[0,1,1,0,0],
	[0,0,0,0,1],
	[0,0,0,0,1],
	[0,0,0,1,0],
	[1,1,0,0,0]
]
print searchObject.countAreas(data)
