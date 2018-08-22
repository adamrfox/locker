# locker
This is an interactive script to lock and unlock files.  The idea here is for testing other projets against locked files.
This script uses the portalocker module so you'll need to get that.  I used it because it's cross-platform and so should lock files properly regardless of where the data lives (local, SMB, NFS, etc.).

It's an interactive shell with simple commands:

<lock | l> file : Locks a file based on the lock type set (Exclusive [EX] is the default)
<unlock | u> file : Unlocks a file.  NB: File must have been locked by locker.
<type | t> [type] : Views or sets the lock type.  Types are EX (Exclusive), SH (Shared), and NB (Non-Blocking)
<list | ls> : Lists the files locked by locker as well as the type of lock
<help | h | ?> : prints a help message similar to this one.
<exit | e | quit | q> : Exits the shell, all files are closed and unlocked on exit.

