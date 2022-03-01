#Declare filepath as simple variables
from asyncore import read


fileread_path = "pico.txt"
filewrite_path = "output.txt"
# Set i to 1
i = 1
# With close open filepath with permission as second param as <name of var>
with open(fileread_path,"r") as fileread:
    with open(filewrite_path, "w") as filewrite:
        for readLine in fileread:
            filewrite.write(str(i) + "\n")
            filewrite.write(readLine)
            i += 1
print("look inside your folder...")
# for <var> in read:

# write i add new line

# write new line and add new line

#print Look inside your folder.