## Concurrency Programming
I kinda over thought this one. Since my relative interreptation of Last RGNs is relative to time. End of the Program, N time... I came up with a number of answers, but decided to stick with one. Also I initial used synchronised list but I began using the keyword synchronised on list to ensure mutual exclusions on the Critical Sections. i.e since removal/and adding a random number to a list must both be ensured a single operation with guaranteed exclusion from other threads, including main.

### My Solution
* Generating results for the last 30 RGNs given during the life span of the program. Main continuously prints the results of the last 30RGNs given from N threads. Again mutual exclusion guaranteed through use of synchronised. Since Collections.max and min iterate the array twice, a more optimized approach would be to iterate the array once and do the calculations for all.
  
### Prev
* Just other attempts which are similar but I decided to do differently.

##### Compiling and Execution

```
	javac CRNG.java
	jar -cvmf MANIFEST.MF CRNG.jar CRNG.class CRNG\$Numthread.class	

	# Either pass with args 
	java -jar CRNG.jar <num of threads>

```
