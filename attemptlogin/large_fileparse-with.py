#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
posts = 0 


with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:


    for line in kfile:

        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        elif "POST" in line: 
            posts += 1
print("The number of failed log in attempts is", loginfail)

print("The number of successful POSTs is", posts)

print(line.split(" ")[-1])
