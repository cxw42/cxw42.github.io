#!/bin/bash
# mod2.sh: Make some global mods

# Add paragraphs
for f in *.html
do
  sed -i.bak '1 s/$/<p>/
$ s/^/<\/p>/
/^\s*$/s/^/<\/p><p>/' "${f}"
done

# vi: set ts=2 sts=2 sw=2 et ai: #

