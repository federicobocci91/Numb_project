# Numb-prevents-a-complete-EMT-by-modulating-Notch-signalling

Supplementary material for Bocci, Kumar, Tripathi, Aguilar, Hanash, Levine and Onuchic, "Numb prevents a complete EMT by modulating Notch signalling"

To run the following code on your computer, you need:
(i) Python (not older than 2.6)
(ii) The following numerical packages:
  (ii-a) Numpy (http://www.numpy.org/)
  (ii-b) Matplotlib (https://matplotlib.org/)
  (ii-c) Scipy (https://www.scipy.org/)
  (ii-d) PyDSTool (http://www.ni.gsu.edu/~rclewley/PyDSTool/FrontPage.html)
  
The files are:

(1) functions.py - auxiliary functions
(2) single_cell.py - methods for the single cell simulations
(3) multi_cell.py - methods for the multi-cell simulations

single_cell.py contains the code for the single cell simulation, while multi_cell.py contains the code for tissue-level simulations. Both programs rely on auxiliary functions contained in functions.py, so functions.py must be in the same folder when compiling single_cell.py/multi_cell.py (otherwise, the path .../functions.py must be indicated).

To compile, run python single_cell.py (or python multi_cell.py) on your terminal after entering in your work directory.

For further questions about the code, please contact me (Federico Bocci - fb20@rice.edu).
