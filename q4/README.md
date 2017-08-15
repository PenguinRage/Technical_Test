## Concurrency Programming

There are two solutions in this problem:

### Solution 1

* first solution concurrently generates the min,max,freq and avg for the last 30 numbers for any N time where N is the time of the program running.


### Solution 2
* second solution: just generates the random numbers and when you wish to get the results just type # and press enter to leave and generate the results of min,max,freq and avg of the last 30 RGNs.

##### Compiling and Execution

```
	javac CRNG.java
	jar -cvmf MANIFEST.MF CRNG.jar CRNG.class CRNG\$Numthread.class	

	# Either pass with args or java Scanner will ask for number of threads
	java -jar CRNG.jar <num of threads>

```