#!/usr/bin/env python

"""
This is a way to save the startup time when running img2py on lots of
files...
"""

import os
from wx.tools import img2py

command_lines = [
    "-a -F -i -n Icon images/icon-256.png images.py",
    "-a -F -i -n Open_Link images/open-link.png images.py",
    "-a -F -i -n Advanced_Config images/advanced-config.png images.py",
    "-a -F -i -n Exit images/exit.png images.py",
    "-a -F -i -n Bug images/bug.png images.py",
    "-a -F -i -n Feature images/feature.png images.py",
    "-a -F -i -n Github images/github.png images.py",
    "-a -F -i -n Forum images/forum.png images.py",
    "-a -F -i -n Config_Folder images/folder.png images.py",
    "-a -F -i -n Update_Check images/update-check.png images.py",
    "-a -F -i -n About images/about.png images.py",
    "-a -F -i -n Patch images/patch.png images.py",
    "-a -F -i -n Patched images/patched.png images.py",
    "-a -F -i -n Lock images/lock-24.png images.py",
    "-a -F -i -n Unlock images/unlock-24.png images.py",
    "-a -F -i -n Guide images/guide-24.png images.py",
    "-a -F -i -n Sos images/sos-24.png images.py",
    "-a -F -i -n Magisk images/magisk-24.png images.py",
    "-a -F -i -n Add images/add-24.png images.py",
    "-a -F -i -n Delete images/delete-24.png images.py",
    "-a -F -i -n Scan images/scan-24.png images.py",
    "-a -F -i -n Flash images/flash-32.png images.py",
    "-a -F -i -n Splash images/splash.png images.py",
    "-a -F -i -n Process_File images/process_file-24.png images.py",
    "-a -F -i -n Support_Zip images/support-24.png images.py",
    "-a -F -i -n Paste images/paste-24.png images.py",
    "-a -F -i -n Patched_Small images/patched-16.png images.py",
    "-a -F -i -n Boot images/boot-24.png images.py",
    "-a -F -i -n InstallMagisk images/install-magisk-24.png images.py",
    "-a -F -i -n InstallApk images/install-apk-24.png images.py",
    "-a -F -i -n Official images/official-24.png images.py",
    "-a -F -i -n Official_Small images/official-16.png images.py",
    "-a -F -i -n Wifi_ADB images/wifi-adb-24.png images.py",
    "-a -F -i -n PackageManager images/packages-24.png images.py",
    "-a -F -i -n FlashBoot images/flash-24.png images.py",
    "-a -F -i -n BackupManager images/backup-24.png images.py",
    "-a -F -i -n Shell images/shell-24.png images.py",
    "-a -F -i -n PartitionManager images/partition-24.png images.py",
    "-a -F -i -n CustomPatch images/custom-patch-24.png images.py",
    ]

if __name__ == "__main__":
    # first delete the existing images.py
    if os.path.exists("images.py"):
        os.remove("images.py")

    # create images.py with proper header
    with open('images.py', "w", encoding="ISO-8859-1", errors="replace") as f:
        header = """
#----------------------------------------------------------------------
# This file was generated by encode-bitmaps.py
#
from wx.lib.embeddedimage import PyEmbeddedImage

#----------------------------------------------------------------------
SmallUpArrow = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAADxJ"
    b"REFUOI1jZGRiZqAEMFGke2gY8P/f3/9kGwDTjM8QnAaga8JlCG3CAJdt2MQxDCAUaOjyjKMp"
    b"cRAYAABS2CPsss3BWQAAAABJRU5ErkJggg==")

#----------------------------------------------------------------------
SmallDnArrow = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAEhJ"
    b"REFUOI1jZGRiZqAEMFGke9QABgYGBgYWdIH///7+J6SJkYmZEacLkCUJacZqAD5DsInTLhDR"
    b"bcPlKrwugGnCFy6Mo3mBAQChDgRlP4RC7wAAAABJRU5ErkJggg==")

        """
        # header = "#----------------------------------------------------------------------\n"
        # header += "# This file was generated by encode-bitmaps.py\n"
        # header += "#\n"
        # header += "from wx.lib.embeddedimage import PyEmbeddedImage\n\n"
        f.write(header)

    # add all the images
    for line in command_lines:
        args = line.split()
        img2py.main(args)

