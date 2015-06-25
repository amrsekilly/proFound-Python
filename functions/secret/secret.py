# reveals a secret message

import os

def rename_file():
	flist = os.listdir("/Users/amr/Documents/pyFoundation/functions/secret/prank")

	# make sure it's working
	print flist

	# change the WD
	os.chdir("/Users/amr/Documents/pyFoundation/functions/secret/prank")

	# loop over all the files 
	for fl in flist:
		print "old name:", fl, "new name:", fl.translate(None, "0123456789")
		os.rename(fl, fl.translate(None, "0123456789"))

# call the fn
rename_file()