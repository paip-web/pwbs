def md5(fname):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def findFiles(path_to_watch, arg_files):
    import os, fnmatch
    matches = []
    for root, dirnames, filenames in os.walk(path_to_watch):
        for filename in fnmatch.filter(filenames, arg_files):
            matches.append(os.path.join(root, filename))
    return matches
def HashFiles(path_to_watch, filenames_to_watch, excluded=[]):
    #print("PWCIW: Hashing Files...")
    from datetime import datetime
    print("\rPWCIW[{0}]: Hashing Files...".format(datetime.now().strftime("%H:%M:%S")),end="")
    watch_files = findFiles(path_to_watch, filenames_to_watch)
    watch_files = [item for item in watch_files if item not in excluded]
    hash_table = []
    for x in watch_files:
        hash_table.append(md5(x))
    return hash_table
def watchFile(path_to_watch, filenames_to_watch, excluded={}, function=print):
    ex2 = []
    for ex, ex1 in excluded.items():
        ex3 = findFiles(ex, ex1)
        ex2 += ex3
    excluded = ex2
    while True:
        lastHash = HashFiles(path_to_watch, filenames_to_watch, excluded)
        print("\nPWCIW: Waiting for trigger")
        while lastHash == HashFiles(path_to_watch, filenames_to_watch, excluded):
            #from time import sleep
            from datetime import datetime
            print("\rPWCIW[{0}]: Waiting ........".format(datetime.now().strftime("%H:%M:%S")),end="")
            #sleep(0.05)
            try:
                with open("stop.watching.file.1234567890", "r") as f:
                    print("PWCIW: Locking File Exist")
                    raise Exception("STOP")
                    break
            except FileNotFoundError:
                continue
        try:
            with open("stop.watching.file.1234567890", "r") as f:
                print("PWCIW: Locking File Exist")
                raise Exception("STOP")
                break
        except FileNotFoundError:
            pass
        print("\nPWCIW: Hash Changed")
        function()
def execute(command):
    """Function to execute command line commands

    Args:
        command (object): Command

    Returns:
        :obj:`str`: Returning Output of Command
    """
    from subprocess import run
    if isinstance(command, list):
        retval = ""
        for cmd in command:
            retval += str(run(cmd, shell=True).stdout)
        return retval
    else:
        return run(command, shell=True).stdout
def SystemVersion():
    #from sys import platform as _platform
    import platform
    #import os
    from collections import namedtuple
    ver = namedtuple("ver", [
        "machine",
        "network_name",
        "processor_name",
        "python_compiler",
        "python_implementation",
        "python_version",
        "python_version_tuple",
        "system_release",
        "system_system",
        "system_version",
        "system_tuple",
        "system_uname",
        "platform_info"
    ])
    platform_information = ""
    try: # Java Platform
        platform_information = platform.java_ver()
        if platform_information[0] == '':
            raise Exception()
    except:
        try: # Windows Platform
            platform_information = platform.win32_ver()
            if platform_information[0] == '':
                raise Exception()
        except:
            try: # Mac OS Platform
                platform_information = platform.mac_ver()
                if platform_information[0] == '':
                    raise Exception()
            except: # Unknown
                platform_information = ()
    osversion = ver(
        machine=platform.machine(),
        network_name=platform.node(),
        processor_name=platform.processor(),
        python_compiler=platform.python_compiler(),
        python_implementation=platform.python_implementation(),
        python_version=platform.python_version(),
        python_version_tuple=platform.python_version_tuple(),
        system_system=platform.system(),
        system_release=platform.release(),
        system_version=platform.version(),
        system_tuple=platform.system_alias(
            platform.system(),
            platform.release(),
            platform.version()
        ),
        system_uname=platform.uname(),
        platform_info=platform_information
    )
    return osversion
from threading import Thread
import sys
print(
    "PAiP Web CI Watcher v.0.0.0.1 running in",
    SystemVersion().python_implementation,
    "{0}.{1}.{2}-{3}{4}".format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
        sys.version_info.releaselevel,
        sys.version_info.serial),
    "[{0}]".format(
        SystemVersion().python_compiler,
    ),
    "on {0} with {1} {2} [{3}]".format(
        SystemVersion().network_name,
        SystemVersion().system_system,
        SystemVersion().system_version,
        SystemVersion().machine)
    )
works = {
    "Work #1" : lambda: watchFile(
        "C:\\Users\\patry\\OneDrive\\Projects\\paip-web-build-system Edition 2\\",
        '[!.~]*',
        {},
        lambda: execute(["cd src/pwbs", "echo GREEN", "green -vvv --run-coverage", "echo PYTEST", "pytest"])
    )
}
while True:
    try:
        for k, v in works.items():
            print("Starting", k)
            t = Thread(target=v, args=())
            t.start()
            t.join()
    except FileNotFoundError:
        for k, v in works.items():
            print("Starting", k)
            t = Thread(target=v, args=())
            t.start()
            t.join()
        continue
    except Exception as e:
        break
        raise e
