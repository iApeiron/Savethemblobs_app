import sys
import runpy

try:
    raw_input
except NameError:
    raw_input = input

savethemblobs = sys.argv[1] if sys.argv[1:] else 'savethemblobs.py'
ecid = raw_input("Enter ECID ").strip() or '1050808663311'
device = raw_input("Enter model (eg. iPhone3,1 or n90ap) ").strip() or 'iPhone3,1'
opt = raw_input("Optional arg (eg. --cydia-blobs) ").strip() or '--overwrite-apple'
fmt = "%s: savethemblobs %s %s %s"
print(fmt % (sys.argv[0].split('/')[-1], ecid, device, opt))
sys.argv = ['savethemblobs.py', ecid, device, opt]
with open(sys.argv[0]) as in_file:
    exec(in_file.read())
