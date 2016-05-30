import sys

def main():
	song=open('example.txt', "r");
	print "-"*40;
	print  "file name is: %s" %song.name;
	print "-"*40;
	print "File contents:\n";
	song_lyrics=song.read().split('\n'); #list that holds each line as an individual string1
	print song_lyrics;    #test point
	print "Total no. of lines: %r" %len(song_lyrics);  

	print "-"*40;
	print song_lyrics[1];
	for i in range(len(song_lyrics)):         #beginning of line processing.
		line=song_lyrics[i].split(' ');			#splits individual lines into separate strings for further processing
		print "\nLine%r :"%(i+1) + " %r" %line+ "\nlength: %r " %len(line) +" words";
		print "*"*10;
		word_count={};
		for j in range(len(line)):		
			k =0;
			count =1;
			for k in range(len(line)):		#allows for iteration through the the line itself to facilitate word_count
				if j!=k:		#prevents double counting of one word  
					if line[j] == line[k]:
						count +=1;
			word_count[line[j]] = count;		#updates dictionary accordingly 
			
		print "word count: %r" %word_count ;		#displays word count for each word by use of a dictionary
		print "-"*40;
	song.close()	

if __name__=="__main__":
	main();
