import os, sys, stat
path = "testfile.txt"

os.chmod(path,0o030)
#we want the group to be able to write and execute but not read
#1 = execute
#2 = write
#4 = read

print("Changed mode successfully!!")


#os.chmod(path, mode)
#write the chgperms.py to set group permissions for write and
#execute but not read

#GRADED 3.0/3.0
