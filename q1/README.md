
## Bash Scripting

##### Subdirectory
Computers store data in a series of directories. Each directory, or folder, may contain files or other directories. If a directory is located within another directory, it is called a subdirectory (or subfolder) of that folder. Subdirectories may refer to folders located directly within a folder, as well as folders that are stored in other folders within a folder. For example, the main directory of a file system is the root directory. Therefore, all other folders are subdirectories of the root folder.

##### Shell script
Runnable script named "q1.sh"
```
#!/bin/bash

# Argument is a sub-directory name

# finds -name : the directory name at any subdirectory level
# find -type f : recursively finds all the files, excluding directories
# wc -w  : counts all the words

find . -name $1 | xargs -I dir find dir -type f | xargs wc -w

```

##### Executable
``` bash
    
    ./q1.sh <directory name>

```

### Extension
Used awk to create a mapping of alphabetical letters ignoring upper and lowercase size. Alphabetical characters are counted and then printed out to give results and histogram.
##### Executable
``` bash
    
    ./q1ext.sh <file name>

```


