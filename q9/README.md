## Memory Management

##### Explain the difference between CMS and G1GC in java and discuss when it is appropriate to use each method
The main difference between the two garbage collectors is how they approach collecting garbage. CMS uses a mark and then sweep approach where G1GC basically scans regions of MemBlock sizes for the most Garbage to clean out. More formal definitions given below.

**Concurrent Mark Sweep Collector**

CMS uses a concurrent algorithm using multiple threads to scan through the heap (“mark”) for unused objects that can be recycled (“sweep”). This algorithm will enter “stop the world” (STW) mode in two cases: when initializing the initial marking of roots (objects in the old generation that are reachable from thread entry points or static variables) and when the application has changed the state of the heap while the algorithm was running concurrently, forcing it to go back and do some final touches to make sure it has the right objects marked.

**G1 Collector**

The Garbage first collector (G1) introduced in JDK 7 update 4 was designed to better support heaps larger than 4GB. The G1 collector utilizes multiple background threads to scan through the heap that it divides into regions, spanning from 1MB to 32MB (depending on the size of your heap). G1 collector is geared towards scanning those regions that contain the most garbage objects first, giving it its name (Garbage first).
The Garbage-First (G1) garbage collector is a server-style garbage collector, targeted for multiprocessor machines with large memories. It attempts to meet garbage collection (GC) pause time goals with high probability while achieving high throughput. Whole-heap operations, such as global marking, are performed concurrently with the application threads. This prevents interruptions proportional to heap or live-data size.

**When to use:**

Dependent on the following:
- Application Throughput
- Pause time
- Footprint

G1 is designed to be a low configuration, low pause collector for large heaps. You do sacrifice some application throughput and of course some heap space in order to meet those low pause time goals. A major design goal is that hopefully you can do this with almost zero configuration.

CMS was also designed to be a fairly low pause collector for small --> large(r) heaps, but arguably it wasn't designed up front for the larger heaps we see today in the wild. It's seen by many to require much more configuration than G1 (or any other collector) and has some nasty 'blow out' failure cases.

So, when to use G1?  When configuring CMS gets too hard and/or your heaps are large (2-4GB+) and/or you want to be able to explicitly set pause time goals.

##### Ext: Briefly explain how you might diagnose and fix java application that is failing with *OutOfMemoryError*
Obviously dependent on the causes as discussed in the Oracle link below and could be attributed to a number of things.
[Oracle Documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/memleaks002.html)

Increasing heap size is more or less temporay fix. One way of fixing these issues is to produce high-performance code and to not get lazy.
* Use local variables wherever possible.
* Make sure you select the correct object (EX: Selection between String, StringBuffer and StringBuilder)
* Use a good code system for your program (EX: Using static variables VS non static variables)
* Try to move with multi threading.

If I was to discuss this with other languages my main statement would be "Pass by Reference, Not copy" obviously unless you need a copy of an object :P
