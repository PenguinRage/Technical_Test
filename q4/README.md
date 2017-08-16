## Concurrency Programming
I kinda over thought this one. Since my relative interreptation of Last RGNs is relative to time. End of the Program, N
time... I came up with a number of answers. Also I initial used synchronised list but I began using the keyword synchronised on list to ensure mutual exclusion
on the Critical Sections. i.e since removal/and adding a random number to a list should be both ensured single operation with guaranteed exclusion from other threads, including main.


### Solution 1
* first solution: just generates the random numbers and when you wish to get the results just type # and press enter to stop threads and will generate the results of min,max,freq and avg of the last 30 RGNs.

### Solution 2

* second solution concurrently generates the min,max,freq and avg for the last 30 numbers for any N time where N is the time of the program running. Type # and enter prints the results for the list while threads will wait since mutual exclusion must be guaranteed and then resume generating more RGNs.

### Solution 3
* I don't want to talk about him. He just keeps generating results for the last 30 RGNs given.


##### Compiling and Execution

```
	javac CRNG.java
	jar -cvmf MANIFEST.MF CRNG.jar CRNG.class CRNG\$Numthread.class	

	# Either pass with args or java Scanner will ask for number of threads
	java -jar CRNG.jar <num of threads>

```
