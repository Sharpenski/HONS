BEGIN {
	FS = " ";
	count = 0;
}
{
	if($6 !~ 0.0) {
		count++;
		data[count,1] = $2;
		data[count,2] = $3;
	} 
}
END {
	for(i = 1; i <= count; i++) {
		printf "%.2f %.2f\n", (406 * data[i,1]), (650 * data[i,2]);
	}
}