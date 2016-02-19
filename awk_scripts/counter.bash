for i in {1..58};
do
	awk -f ../awk_scripts/data_drawer.awk ../necker/patients/LEEDS_p$i* > ../necker/forJava/LEEDS_p$i

	#echo $i
done

for i in {0..9};
do
	awk -f ../awk_scripts/data_drawer.awk ../necker/controls/LEEDS_c2$i* > ../necker/forJavaControl/LEEDS_c2$i
	#echo $i
done