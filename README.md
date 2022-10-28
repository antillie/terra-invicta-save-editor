# terra-invicta-save-editor

A save game editor for Terra Invicta written in Python.

Supports both compressed and uncompressed save files seemlessly.

Currently allows for editing of faction resources, councilor stats, faction project progress, and global research. You can also change which faction is controlled by the player.

The windows executable is built using auto-py-to-exe. The GUI is built as a wxFormBuilder project. If you don't trust exe files and would rather run the python code directly you will need to install python 3.9 from python.org and the wxpython module via pip. Other versions of Python 3 may work, I haven't tested them.
