import pypreprocessor #Download pypreprocessor on raspberry pi being used
import sys

#This script provides a way to use #idef on python

pypreprocessor.defines.append('define')
pypreprocessor.defines.append('ifdef')
pypreprocessor.defines.append('endif')

pypreprocessor.run = True / False
pypreprocessor.resume = True / False
pypreprocessor.save = True / False

pypreprocessor.input = 'Parser.py'
pypreprocessor.removeMeta = True
pypreprocessor.output = 'Parser.py' 
#If output file is the same, maybe it pre-processes in-place???

pypreprocessor.readEncoding = sys.stdin.encoding
pypreprocessor.writeEncoding = sys.stdout.encoding

