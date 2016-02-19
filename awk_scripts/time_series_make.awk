BEGIN {
	FS = " "; # field separator
	count = 0; # track the number of records
}
{
	for(f = 2; f <= NF; f++) { # start at second attr, timestamp not needed 
		data[count,f-2] = $f;
	}
	count++;
}
END {
	for(i = 0; i < count-6; i+=20) { # iterate through all the acquired records
		for(rec = i; rec < i+6; rec++) { # move the window so that it captures 6 consecutive records
			for(j=0; j < 5; j++) { # print out the required contents of a single record
				printf "%f ", data[rec,j];
			}
		}
		printf "\n";
	}
}