import os
import sys
config = sys.argv[1]
net_id = sys.argv[2]
path = os.getcwd();
with open(config) as f:
	count = 0
	for line in f:
		if "dc" in line:
			if "#" in line and (line.find("#") < line.find("dc")):
				#print str(line.find("#")) + " " + str(line.find("dc"))
				continue;
			index = line.find("dc")
			host = line[index : index + 4]
			#os.system("ssh -l "+'"'+net_id+'"'+" "+'"'+host+'"'+" "+ '"'+"cd $HOME/AOS_xxw130730/Project1;java Project1 "+str(count)+'"'+" &")
			os.system("ssh -l "+'"'+net_id+'"'+" "+'"'+host+'"'+" "+ '"'+"cd "+path+";"+" java Project1 "+str(count)+" "+config+'"'+" &")
			#print "ssh -l "+'"'+net_id+'"'+" "+'"'+host+'"'+" "+ '"'+"cd "+path+";"+" java Project1 "+str(count)+" "+config+'"'+" &"
			count += 1
			