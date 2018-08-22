import portalocker
import getopt
import sys

class Locker():
    def __init__(self, type, fh):
        self.type = type
        self.fh = fh

    def get_type(self):
        return self.type

    def get_fh(self):
        return self.fh

def help():
    print "Commands in the interpreter:"
    print "lock | l file : Lock the specified file"
    print "unlock | u file: Unlock the spciefied file.  File must be locker by locker"
    print "type | t [lock_type] : View or change the lock type.  Types are EX, SH, and NB"
    print "list | ls : List files locked by locker"
    print "quit | q | exit | e : Quit/Exit"
    print "help | h | ? : Print this message"

LOCK_TYPE = "EX"
lock_list = {}
file = []
done = False
index = 0

while done == False:
    cmd_s = raw_input("locker> ")
    cmd = cmd_s.split()
    if len(cmd) == 0:
        continue
    if cmd[0] in ['exit', 'e', 'quit', 'q']:
        done = True
    elif cmd[0] in ['?', 'help', 'h']:
        help()
    elif cmd[0] in ['list', 'ls']:
        for lf in lock_list.keys():
            print lf + " : " + lock_list[lf].get_type()
    elif cmd[0] in ['lock', 'l']:
        if cmd[1] in lock_list.keys():
            print "File " + cmd[1] + " is already locked"
            continue
        try:
            file_handle = open (cmd[1], 'r+')
        except IOError:
            sys.stderr.write ("Error attempting to lock " + cmd[1])
            print ""
        else:
            lock_list[cmd[1]] = Locker(LOCK_TYPE, file_handle)
            if LOCK_TYPE == "EX":
                portalocker.lock(file_handle, portalocker.LOCK_EX)
            elif LOCK_TYPE == "SH":
                portalocker.lock(file_handle, portalocker.LOCK_SH)
            elif LOCK_TYPE == "NB":
                portalocker.lock(file_handle, portalocker.LOCK_NB)
            print "Locked"
    elif cmd[0] in ['unlock', 'u']:
        if cmd[1] in lock_list.keys():
            portalocker.unlock(lock_list[cmd[1]].get_fh())
            print "Unlocked"
            del(lock_list[cmd[1]])
        else:
            print cmd[1] + " is not locked by locker"
    elif cmd[0] in ['type', 't']:
        try:
            cmd[1]
        except IndexError:
            print "Lock Type is " + LOCK_TYPE
        else:
            if cmd[1].upper() == "EX" or cmd[1].upper() == "SH" or cmd[1].upper() == "NB":
                LOCK_TYPE = cmd[1].upper()
                print "Lock type set to " + cmd[1].upper()
            else:
                print "Accepted Lock types are EX (Exclusive), SH (Shared), and NB (Non-Blocking)"
    else:
        print "Command not recognized.  Try help for a list of commands"



