WaterFont
=========

Version 1.2

Watermarking Tool with Dynamic Font selection and Multi-image Marking.

* Watermarking of Multiple Images in sequence
* Can load and choose from all available fonts. Just get the font file off the net!
* Click on the image to select the location of the watermark
* Much more.

Prerequisites:
* Python 2.7+ (Will work on the Python3 version once the project is stable) www.python.org
* Python Imaging Library. Preferably v1.1.7. www.pythonware.com/products/pil



For Windows users:

    1. The native PIL library installation has some compilation problems, hence it is recommended you install the Pillow library from www.lfd.uci.edu/~gohlke/pythonlibs/
    2. Security: The Fonts folder (C:\Windows\Fonts) is access protected. This may cause the program to be unable to display the fonts when the font selection window opens. To correct this, do the following:
        
        * Open a Command Prompt as Administrator (right click cmd, “run as administrator”).
        * Type “attrib –r –s c:\windows\fonts” (minus the quotes), hit Enter.
        * Right click on the fonts folder and choose properties.
        * Click the Security tab.
        * Click Advanced.
        * Click the Owner tab.
        * Click the Edit button.
        * Change the Current Owner to yourself.
        * Check the “Replace owner on subcontainers and objects” box
        * Click OK. As a pop-up box will tell you, you must close the window completely for the changes to take in effect.
 
   
#License

WaterFont. A Watermarking Tool With Dynamic Font Selection and Mulitple Image Marking.

    Copyright (C) 2013  Varun Agrawal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Author contact: varagrawal@gmail.com
