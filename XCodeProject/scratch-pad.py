#!/usr/bin/python

dir = os.getcwd();
print dir

cmd = "ls " + dir;

os.system(cmd)



script, first = argv

print "The script is called:", script
print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

if len(sys.argv) < 3:
    print "You must supply three arguements"
    sys.exit(1)


#    print 'Argument List:', str(sys.argv)


>>> import shlex, subprocess
>>> command_line = raw_input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print args
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args) # Success!