#!/usr/bin/python
import sys
import os
import ftplib
import glob
import datetime
import shutil
from ftplib import FTP
from sys import platform as _platform

def usage():
    print("Usage: " + sys.argv[0] + " OLD|NEW");
    sys.exit();

def allFile(pattern):
    s = "";
    for file in glob.glob(pattern):
        s += file + " ";
    return s;

def allFolderFile(pattern, ext):
    s = "";
    for dirpath, dirnames, filenames in os.walk(pattern):
        for filename in [f for f in filenames if f.endswith(ext)]:
            s+= os.path.join(dirpath, filename) + ' '
    return s;

if (len(sys.argv) != 2):
    usage();


if _platform == "darwin":
    DEVKITARM     = 'opt/devkitPro/devkitARM'
elif _platform == "win32":
    DEVKITARM     = 'c:/devkitPro/devkitARM'

TID     = "0004000000000000"
FTP_FOLDER    = "plugin/"
PORT        = 5000
ARCH         = ' -march=armv6k -mlittle-endian -mtune=mpcore -mfloat-abi=hard '
if (sys.argv[1] == "OLD") or (sys.argv[1] == "old"):
    NAME         = "plugin-old3DS"
    COPYTOPATH    = NAME + ".plg"
    CFLAGS        = ' -Os -c -D OLD ' + ARCH
elif (sys.argv[1] == "NEW") or (sys.argv[1] == "new"):
    NAME         = "plugin-new3DS"
    COPYTOPATH    = NAME + ".plg"
    CFLAGS        = ' -Os -c ' + ARCH
else:
    usage();
CC             = "arm-none-eabi-gcc"
CP             = "arm-none-eabi-g++"
OC            = "arm-none-eabi-objcopy"
LD             = "arm-none-eabi-ld"
CTRULIB     = '../libctru'
LIBPATH     = '-L ./lib '
ASFLAGS        = ' -Os -c -s ' + ARCH
LIBFLAGS     = " -lntr -lShark2NTR_dev -lctr -lg -lsysbase -lc -lgcc "
LDFLAGS        = ' -pie --gc-sections -T 3ds.ld -Map=' + NAME +'.map '
INCLUDES     = " -I Includes -I Sources -I Includes/libntrplg -I Sources/helpers "
CFILES        = allFolderFile("./Sources/", ".c")
ASFILES        = allFolderFile("./Sources/", ".s")
OFILES      = allFolderFile("./ofiles/", ".o")
ftp         = FTP()
FILE        = COPYTOPATH

def connect(host, port):
    ftp.connect(host, port);

def disconnect():
    ftp.quit();

def ls():
    ftp.dir();

def send(path, FILE2):
    file = open(FILE, 'rb');
    try:
        ftp.mkd("/" + path);
    except Exception as e:
        pass
    ftp.cwd("/" + path);
    ftp.storbinary('STOR '+ FILE2, file);
    file.close();

def printf(string):
    print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S') + " : " + string);

def run(cmd):
    #print(cmd);
    return (os.system(cmd));

def error():
    print("\n\n");
    printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
    printf("There's some errors on your code.");
    printf("Correct them and try again, for now I'm exiting the compilation.\n");
    printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n");
    sys.exit();

cwd = os.getcwd()
print("\n\n");
printf("Hello AnalogMan!\n");
printf("How are you?\n");
printf("I'm preparing to compile your " + COPYTOPATH + " plugin.\n");
printf("Please just wait a second...\n");
if (os.path.isfile("obj/cheats.o")):
    run("rm obj/*.o")
if (os.path.isfile(COPYTOPATH)):
    run("rm *.plg")
printf("Compiling C files");
result = run(CC +  CFLAGS + INCLUDES + CFILES);
if (result != 0):
    error();

printf("Compiling S files");
result = run(CC + ASFLAGS + ASFILES);
if (result != 0):
    error();

OFILES += allFile("*.o") + " " + allFile("lib/*.o")
printf("Linking all files into " + COPYTOPATH);
result = run(LD + LDFLAGS + ' ' + LIBPATH  + OFILES + LIBFLAGS )
if (result != 0):
    error();

if (os.path.isfile("config.o")):
    run("cp -r *.o obj/ ")
    run("rm *.o")
if (os.path.isfile("a.out")):
    run(OC +" -O binary a.out payload.bin -S")
if (os.path.isfile("a.out")):
    run("rm *.out")
if (os.path.isfile("payload.bin")):
    shutil.copy2("payload.bin", COPYTOPATH);
    run("rm payload.bin");
if (os.path.isfile(NAME + ".map")):
    run("rm *.map");

printf("Copying the plugin in each folder...");
try:
    run("mkdir -p " + FTP_FOLDER + TID);
except Exception as e:
    pass
shutil.copy2(COPYTOPATH, "./" + FTP_FOLDER + TID + "/" + NAME + ".plg");
if (os.path.isfile("./" + FTP_FOLDER + "/.DS_Store")):
    run("rm ./" + FTP_FOLDER + "/.DS_Store")
printf("Creating the zip folder...");
shutil.make_archive(NAME, 'zip', "./plugin");
printf("Should I send the plugin on your console? (y/N)");
try: user = raw_input();
except NameError:
    user = input();
if (user == "yes" or user == "y"):
    print("");
    printf("You got it!");
    printf("What is the IP address?");
    try: HOST = raw_input();
    except NameError:
        HOST = input();
    printf("Sending the plugin right now...\n");
    connect(HOST, PORT);
    send(FTP_FOLDER + TID, NAME + ".plg");
    disconnect();
else:
    printf("As you want sir.\n");
print("\n\n");
printf("Done, enjoy your plugin!\n\n");
