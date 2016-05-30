import sys

song=open('example.txt', "r");
print "-"*40;
print  "file name is: %s" %song.name;
print "-"*40;
song_lyrics=song.read().split('\n'); #list that holds each line as an individual string1
print song_lyrics;    #test point
print len(song_lyrics);  #for testing purposes
print type(song_lyrics); #for testing purposes
print "-"*40;
print song_lyrics[1];
for i in range(len(song_lyrics)):
	line=song_lyrics[i].split(' ');
	print "Line%r :"%i + " %r" %line+ "\n and is of length:%r " %len(line);
	print type(line);
	count =1;
	for j in range(len(line)):
		k =0;
		for k in range(len(line)):
			if j!=k:
				if line[j] == line[k]:
					count +=1;
		print "for " + line[j] + " count is: %r" %count;
	print "-"*40;
song.close()	
print song_lyrics;
