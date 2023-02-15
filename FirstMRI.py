"""FirstMRI.pFirstMRI.pyy
Startup Code

#@author:    Yolanda Vives

"""
import os
import sys
import platform
from PyQt5.QtWidgets import QApplication
import cgitb
#*****************************************************************************
# Add path to the working directory
path = os.path.realpath(__file__)
ii = 0
for char in path:
    if (char=='\\' or char=='/') and path[ii+1:ii+14]=='PhysioMRI_GUI':
        sys.path.append(path[0:ii+1]+'PhysioMRI_GUI')
        sys.path.append(path[0:ii+1]+'marcos_client')
    ii += 1
#******************************************************************************

VERSION = "0.2.0"
AUTHORA = "Yolanda Vives"
AUTHORB = "J.M. Algarín"
print("****************************************************************************************")
print("Graphical User Interface for MaRCoS                                                    *")
print("Dr. Y. Vives, Department of Electronic Engineering, Universitat de València, Spain     *")
print("Dr. J.M. Algarín, mriLab @ i3M, CSIC, Spain                                            *")
print("https://www.i3m-stim.i3m.upv.es/research/magnetic-resonance-imaging-laboratory-mrilab/ *")
print("https://github.com/yvives/PhysioMRI_GUI                                                *")
print("****************************************************************************************")

from controller.session_controller import SessionController

cgitb.enable(format = 'text')


# Run the gui
app = QApplication(sys.argv)
gui = SessionController()
sys.exit(app.exec_())

    
    
