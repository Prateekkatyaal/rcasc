from base_utils import Version_Number, max_depth_reached 
from checks import dir_size
from path_handler import DefineInputOptsnArgs, ProcessInputOptsnArgs
import sys
from printpath import print_path

#--------------------------------------- main -----------------------------------
if __name__=='__main__':
    
    import glob
    CLOP = DefineInputOptsnArgs(Version_Number[0]+Version_Number[1])  #Define the input command line opts and args. 
    depth, units, unitname, args = ProcessInputOptsnArgs(CLOP)

    if len(args) < 1:
        paths = ["/mnt/c/Users/Prateek/Duem"]
    else:
        
        SoFiles = set()

        for l in args:
            
            args_globbed = glob.glob(l)               #EGOF un globbing
            for l2 in args_globbed:
                SoFiles.add(l2)

        paths = list(SoFiles)
        if not len(paths):
            print("No recognizable paths supplied on command line: ", args)
            sys.exit(1)

    
    indent = ""
    
    for path in paths:
        pi1 = dir_size(path, 0, depth)      
        print_path(pi1, indent, units)

    
    if unitname: print(unitname)        
    #if max_depth_reached < depth:
     #    print("Was only necessary to go down %i levels. --depth %i was requested." % (max_depth_reached, depth))
    