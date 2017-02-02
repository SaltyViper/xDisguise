import os

print('''

         _____  _                 _          
        |  __ \(_)               (_)         
 __  __ | |  | |_ ___  __ _ _   _ _ ___  ___ 
 \ \/ / | |  | | / __|/ _` | | | | / __|/ _ \\
  >  <  | |__| | \__ \ (_| | |_| | \__ \  __/
 /_/\_\ |_____/|_|___/\__, |\__,_|_|___/\___|
                       __/ |                 
                      |___/                                                     

''')
# ^ Make the "x" color['MAGENTA'] & the "Disguise" color['RED'] (add the color list so I can experiment with colors and see what looks best :)

filename = input("Filename to add extension to (exclude .extension): ")
o_extension = input("Filename's original extension: .")
d_extension = input("Extension to disguise as: .")

target = 0
while not int(target) in [1,2]:
	print("")
	print("Choose a Target OS that the file will be viewed in")
	print("1) Mac OS")
	print("2) Windows\n")
	target = input("Target OS that the file will be viewed in [1,2]: ")
	if target == "1":
		print("1")
		os.rename(filename+"."+o_extension,filename+"."+d_extension+""+"."+o_extension)
		print("File successfully disguised as "+filename+"."+d_extension+"!")
	if target == "2":
		print("2")
		X = u"\u202E"
		o_extension = o_extension[::-1]
		d_extension = d_extension[::-1]
		os.rename(filename+"."+o_extension,filename+X+d_extension+"."+o_extension)
