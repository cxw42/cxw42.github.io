#!/usr/bin/env python
#layernav.py Copyright (c) 2014 Chris White.  CC-BY-SA 4.0 International.
#   2014/03/19  Initial version
#   2014/03/20  Added hide/show all layers
#   2014/03/31  When moving up or down a layer, select the newly-
#               visible layer.
#   2019/12/31  Minor cleanup.  Happy New Year!

from gimpfu import *

# use these for debugging
#import sys
#sys.stderr = open( r'pyerr.txt', 'a')
#sys.stdout = open( r'pylog.txt', 'a')

#print('Running layernav.py')   #debug

def _find_first_visible(img):
    """ Returns the index of the topmost visible layer, or -1 if
        all layers are hidden."""
    retval = -1
    for idx in range(len(img.layers)):
        if img.layers[idx].visible==1:
            retval = idx
            break
    return retval   # -1 if nothing is visible
# end _find_first_visible

def _showone_helper(img, to_prev):
    """ The function that actually does the work.  Moves to the previous
        layer if to_prev is True, otherwise moves to the next layer."""

    # See what's visible
    #print('In show_helper') #debug
    nlayers = len(img.layers)
    firstidx = _find_first_visible(img)
    #print('Of %d layers, %d is the first visible'%(nlayers,firstidx)) #debug

    # Decide which way to move
    if firstidx==-1:    # nothing was visible - turn on layer 1
        newidx = 0
    elif to_prev:       # move up, with wraparound
        newidx = firstidx-1 if firstidx>0 else nlayers-1
    else:               # move down, with wraparound
        newidx = firstidx+1 if firstidx<(len(img.layers)-1) else 0

    # Update the visibility.  Hide everything but the one of interest so
    # the behaviour is consistent regardless of what's hidden or not.

    try:
        img.undo_freeze()
        for idx in range(nlayers):
            img.layers[idx].visible = 1 if idx==newidx else 0
            if idx==newidx: pdb.gimp_image_set_active_layer(img,img.layers[idx])
    finally:
        img.undo_thaw()

# end _showone_helper

def _showall_dolayers(layers, make_visible):
    """Recursive worker function for showing or hiding all.
        layers: array of layers
        make_visible: True to show, False to hide."""
    for l in layers:
        l.visible = 1 if make_visible else 0
        if isinstance(l, gimp.GroupLayer):  # regular layers are gimp.Layer
            _showall_dolayers(l.layers, make_visible)
    #end foreach layer
# end _showall_dolayers

##########################################################################
# Top-level functions

def show_previous(img):
    #print('In show_previous') #debug
    _showone_helper(img, True)

def show_next(img):
    #print('In show_next') #debug
    _showone_helper(img, False)

def show_all(img):
    try:
        img.undo_freeze()
        _showall_dolayers(img.layers, True)
    finally:
        img.undo_thaw()

def hide_all(img):
    try:
        img.undo_freeze()
        _showall_dolayers(img.layers, False)
    finally:
        img.undo_thaw()

##########################################################################
# Registration

register(
    proc_name=("python-fu-layernav-show-previous"),
    blurb=("Cycle visibility towards the top"),
    help=("Shows the top-level layer or group before the visible layer."+
            "  Hides all other layers."),
    author=("Christopher White"),
    copyright=("Copyright (c) 2014 Christopher White"),
    date=("2014"),
    label=("Show _previous layer"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
           ],
    results=[],
    function=(show_previous),
    menu=("<Image>/View/La_yer"),
    )

register(
    proc_name=("python-fu-layernav-show-next"),
    blurb=("Cycle visibility towards the bottom"),
    help=("Shows the top-level layer or group after the visible layer."+
            "  Hides all other layers."),
    author=("Christopher White"),
    copyright=("Copyright (c) 2014 Christopher White"),
    date=("2014"),
    label=("Show _next layer"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
           ],
    results=[],
    function=(show_next),
    menu=("<Image>/View/La_yer"),
    )

register(
    proc_name=("python-fu-layernav-show-all"),
    blurb=("Make all layers visible"),
    help=("Make all layers visible"),
    author=("Christopher White"),
    copyright=("Copyright (c) 2014 Christopher White"),
    date=("2014"),
    label=("_Show all layers"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
           ],
    results=[],
    function=(show_all),
    menu=("<Image>/View/La_yer"),
    )

register(
    proc_name=("python-fu-layernav-hide-all"),
    blurb=("Make all layers hidden"),
    help=("Make all layers hidden"),
    author=("Christopher White"),
    copyright=("Copyright (c) 2014 Christopher White"),
    date=("2014"),
    label=("_Hide all layers"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
           ],
    results=[],
    function=(hide_all),
    menu=("<Image>/View/La_yer"),
    )

main()  # this call is required by GIMP

# vi: set ts=4 sts=4 sw=4 expandtab ai: #
