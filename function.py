#!/usr/bin/python

#Required arguments are the arguments passwd to a function in correct positional order
print "Required arguments are the arguments passwd to a function in correct positional order."
def printme(str):
        print str
        return;
printme("Welcome to Python World!\n")

#Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the argument by the parameter name
print "Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the argument by the parameter name."
def platorm(operating_system,platform_type):
        print "Operating System:",operating_system
        print "Platform:",platform_type
        return;
platorm(platform_type="Linux",operating_system="Red Hat Enterprise Linux Server release 7.2 (Maipo)")
