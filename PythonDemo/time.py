t = {"year": "2013", "month": "9", "day": "30", "hour": "16", "minute": "45", "second": "2"}

text ='{0}-{1}-{2} {3}:{4}:{5}'.format(t["year"],'{:0>2d}'.format(int(t["month"])),'{:0>2d}'.format(int(t["day"])),'{:0>2d}'.format(int(t["hour"])),'{:0>2d}'.format(int(t["minute"])),'{:0>2d}'.format(int(t["second"]))) 
print(text)