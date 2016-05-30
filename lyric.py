import sys


def word_counter(line):
	word_count={};
	for j in range(len(line)):		
		k =0;
		count =1;
		for k in range(len(line)):
			if j!=k:
				if line[j] == line[k]:
					count +=1;
		#print line[j] + ": %r" %count;
		word_count[line[j]] = count;
		
	print "word count: %r" %word_count ;		#displays word count for each word by use of a dictionary
	print "-"*40;

def line_reader(song_lyrics):		#Inividual line/bars processing.
	for i in range(len(song_lyrics)):
			line=song_lyrics[i].split(' ');			#splits individual lines into separate strings for further processing
			print "\nLine%r :"%(i+1) + " %r" %line+ "\nlength: %r " %len(line) +" words";
			print "\n"+"*"*10;
			word_counter(line);
			#print type(line);

def song_reader(song_lyrics):		#whole song processing
	all_lines=[]
	for i in range (len(song_lyrics)):
		line=song_lyrics[i].split(' ');
		all_lines.extend(line);
	print all_lines; 		#for debugging needs 
	print "\n"+"*"*10 +"*";
	word_counter(all_lines)

def main():
	filename = raw_input("Input file name: ");
	#filename="example.txt";		#for debugging needs 
	song=open(filename, "r");
	print "-"*40;
	print  "file name is: %s" %song.name;
	print "-"*40;
	print "File contents:\n";
	song_lyrics=song.read().split('\n'); #list that holds each line as an individual string1
	print song_lyrics;    #test point
	print "Total no. of lines: %r" %len(song_lyrics);  
	print "-"*40;
	print "Options:\nAnalyse song as a whole(A) or analyse song per line(B):"
	user_input = raw_input('What would you like to do? ');
	if user_input =='A' or user_input=='a':
		song_reader(song_lyrics);
	elif user_input=="B" or user_input=='b':
		line_reader(song_lyrics);
	else:
		print "You had 2 choices FAM! 2 bloody choices! \n Here's another chance.";
		main();
	song.close()	

if __name__=="__main__":
	main();
