
import optparse

class PathItem(object):
    
    def __init__(self, p):
        self.path = p
        self.bytes = 0
        self.local_bytes = 0       
        self.local_regfiles = 0    
        self.L = []

    def __str__(self):
        S = "%s %i" % (self.path, self.bytes)
        return S


USAGE_MESSAGE = """
python duem.py [-bkmg] [-d depth] [directory path]
"""

def DefineInputOptsnArgs(Version_Number_Date):
    
    CmdLineOpt = optparse.OptionParser(version=Version_Number_Date,usage=USAGE_MESSAGE)     #command line options
    CmdLineOpt.add_option("-d", "--depth", action="store", type="int", dest = "depth", default=0,
                    help="# of directories down for print display (default=0)")
    CmdLineOpt.add_option("-b", action="store_true", default=False, help="Display in Bytes")
    CmdLineOpt.add_option("-k", action="store_true", default=False, help="Display in Kiloytes")
    CmdLineOpt.add_option("-m", action="store_true", default=False, help="Display in Megaytes")
    CmdLineOpt.add_option("-g", action="store_true", default=False, help="Display in Gigabytes")
    


    return CmdLineOpt


   # ----------------------------------------------------------------------------

def ProcessInputOptsnArgs(CmdLineOpt):
    
    opts,args = CmdLineOpt.parse_args()

    units = "automatic"           
    
    if opts.b: units = 'b'
    if opts.k: units = 'k'
    if opts.m: units = 'm'
    if opts.g: units = 'g'     
    D_units = {"b": "bytes", "k": "Kilobytes", "m": "Megabytes", "g": "Gigabytes", "automatic":""}
    unitname = D_units[units]

    try:
        depth = int(opts.depth)
    except:
        print("-d arg not a valid integer: (%s)" % opts.depth)
        raise

    return depth, units, unitname, args
#--------------------------------------------------------------------------
