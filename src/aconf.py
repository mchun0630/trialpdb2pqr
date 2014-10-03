"""
    Autoconf'ed variables for PDB2PQR

    This is an module for storing all autoconf'ed variables.

    ----------------------------
   
    PDB2PQR -- An automated pipeline for the setup, execution, and analysis of
    Poisson-Boltzmann electrostatics calculations

    Copyright (c) 2002-2011, Jens Erik Nielsen, University College Dublin; 
    Nathan A. Baker, Battelle Memorial Institute, Developed at the Pacific 
    Northwest National Laboratory, operated by Battelle Memorial Institute, 
    Pacific Northwest Division for the U.S. Department Energy.; 
    Paul Czodrowski & Gerhard Klebe, University of Marburg.

	All rights reserved.

	Redistribution and use in source and binary forms, with or without modification, 
	are permitted provided that the following conditions are met:

		* Redistributions of source code must retain the above copyright notice, 
		  this list of conditions and the following disclaimer.
		* Redistributions in binary form must reproduce the above copyright notice, 
		  this list of conditions and the following disclaimer in the documentation 
		  and/or other materials provided with the distribution.
        * Neither the names of University College Dublin, Battelle Memorial Institute,
          Pacific Northwest National Laboratory, US Department of Energy, or University
          of Marburg nor the names of its contributors may be used to endorse or promote
          products derived from this software without specific prior written permission.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
	IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
	INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
	BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
	DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
	LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
	OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
	OF THE POSSIBILITY OF SUCH DAMAGE.

    ----------------------------
"""

__date__   = "8 July 2008"
__author__ = "Yong Huang"

""" PDB2PQR version string"""
PDB2PQR_VERSION = "master BRANCH"

""" The maximum number atoms to be handled on the server"""
MAXATOMS = 10000

""" The absolute path to root HTML directory"""
SRCPATH = "C:\Users\chun320\Documents\GitHub\apbs-pdb2pqr\pdb2pqr/"

""" The path to the web site *directory* """
WEBSITE     = "http://WE19812/pdb2pqr/"

""" The stylesheet to use """
STYLESHEET  = WEBSITE + "pdb2pqr.css"

""" The OPAL service URL """
PDB2PQR_OPAL_URL = ""

""" The HAVE_PDB2PQR_OPAL flag """
HAVE_PDB2PQR_OPAL = PDB2PQR_OPAL_URL != ""

""" The HAVE_APBS flag """
APBS_LOCATION = ""

""" The HAVE_APBS flag """
HAVE_APBS = APBS_LOCATION != ""

""" The APBS_OPAL_URL flag """
APBS_OPAL_URL = ""

""" The installation directory """
INSTALLDIR = "C:/Users/chun320/pdb2pqr/"

""" The temporary directory """
TMPDIR = "tmp/"
