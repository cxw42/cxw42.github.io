#!/bin/bash
# mod.sh: Make some global mods

# Make a sed script that will insert links
script=''
for f in *.html
do
  base=${f%.html} # no files have sed special chars, so this is OK.
  script="$script
2,$ s/${base}/<a href=\"${f}\">${base}<\/a>/g"  # skip line 1, the title
done

for f in *.html
do
  sed -i.bak "$script" "${f}"
done

# vi: set ts=2 sts=2 sw=2 et ai: #

