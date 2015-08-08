#!/bin/bash

for f in *.html ; do 
sed -i.bak "1 i <html><head><title>${f%.html}</title></head><body>
$ a </body></html>" "$f" 
done
