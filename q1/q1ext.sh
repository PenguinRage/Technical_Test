#!/bin/sh



awk -vFS="" '{
for (i=1; i<=NF; i++) 
    {
    if ($i~/[a-zA-Z]/) 
        { w[toupper($i)]++ } 
    } 
} 
END{ 
for(i in w) {
    printf i " " w[i] "\t";
    for(j=1; j<w[i]; j++) { printf "#" } 
        printf "\n" 
    } 
}' $1 | sort
