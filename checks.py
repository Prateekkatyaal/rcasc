#recursively size check

from base_utils import max_depth_reached
from path_handler import PathItem
import os
from os.path import join, isdir, isfile


def dir_size(start, start_depth=0, max_depth=0):
    """ Get a list and size of all names of files and subdirectories in directory start
        Recursively go down
    """
    global max_depth_reached
    max_depth_reached = max(start_depth, max_depth_reached)
    PI1 = PathItem(start)
    try:
        dir_list = os.listdir(start)
    except:
        
       pass
        

    total = 0
    for item in dir_list:
    
        path = join(start, item)
        try:
            stats = os.stat(path)       
        except:
            
            pass
        else:
            
            if isfile(path):
                PI1.local_regfiles += 1
                PI1.local_bytes += stats[6]

            total += stats[6]

            
            #if isdir(path) and (follow_links or not islink(path)):
            if isdir(path):
                PI2 = dir_size(path, start_depth+1, max_depth)
                try:
                    total += PI2.bytes
                except :    
                    pass
                else:
                    if max_depth and (start_depth < max_depth):
                        PI1.L.append(PI2)
    PI1.bytes = total
    return PI1