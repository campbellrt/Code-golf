'''
Auther: Campbell Reid-Tait

Language: Python 2.7.3

#http://codegolf.stackexchange.com/questions/45056/shortest-unique-substrings
'''


def count2(string, sub):
	count = 0
	for x in xrange(len(string)):
		if sub == string[x:x+len(sub)]:
			count +=1
	return count

def number (s, num):
	out = []
	if num <= len(s):
		for i in xrange(len(s)):
			if i+num <= len(s):
				sub = s[i:i+num]
				count = count2(s,sub)
				if count == 1:
					out.append( sub )
	else:
		out.append("")

	if out ==[]:
		number(s, num+1)
	else:
		print out


#"" -> [""]
#"abcaa" -> ["b","c"]
#"rererere" -> ["ererer"]
#"asdfasdfd" -> ["fa","fd"]
#"ffffhhhhfffffhhhhhfffhhh" -> ["hffff","fffff","hhhhh","hfffh"]
#"asdfdfasddfdfaddsasadsasadsddsddfdsasdf" -> ["fas","fad","add","fds"]

number("", 1)
number("abcaa", 1)
number("rererere", 1)
number("asdfasdfd", 1)
number("ffffhhhhfffffhhhhhfffhhh", 1)
number("asdfdfasddfdfaddsasadsasadsddsddfdsasdf", 1)
