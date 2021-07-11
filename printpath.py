
from os.path import join, isdir, isfile
from base_utils import INDENT_ARROW, INDENT_INCREMENT



def print_path(pathitem, indent, units):
    
    if not pathitem:
         return     
    def Auto_unit(units, x):
        
        if (units == "automatic" and x > 1024**3) or units =='g':
            return "%.1fG" % (float(x)/1024.0**3)
        elif (units == "automatic" and x > 1024**2) or units =='m':
                return "%.1fM" % (float(x)/1024.0**2)
        elif (units == "automatic" and x > 1024) or units =='k':
            return "%.1fK" % (float(x)/1024.0)
        elif units =='b':
            return "%ib" % x
        else:
            return "%ib" % x
    #--------------------------------------------------

     
    if bool(indent):
        indent_arrow = INDENT_ARROW
    else:
        indent_arrow = ""
    if pathitem.local_regfiles == 0:
        print('%s%s%s %s   ' % (indent, indent_arrow, Auto_unit(units, pathitem.bytes),
                                        pathitem.path))
    else:
        if pathitem.bytes == pathitem.local_bytes:
            #don't bother to write size a 2nd time
            print('%s%s%s %s   ' % (indent, indent_arrow, Auto_unit(units, pathitem.bytes),
                                              pathitem.path))
        else: 
            print('%s%s%s %s   ' % (indent, indent_arrow, Auto_unit(units, pathitem.bytes),
                                                  pathitem.path))
                                                  

    for p in pathitem.L:          #recursive call
        print_path(p, indent+INDENT_INCREMENT, units)