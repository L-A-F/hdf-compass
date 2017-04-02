##############################################################################
# Copyright by The HDF Group.                                                #
#              Helmholtz-Zentrum Dresden - Rossendorf,                       #
#                Computational Radiation Physics                             #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of the HDF Compass Viewer. The full HDF Compass          #
# copyright notice, including terms governing use, modification, and         #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################
from hdf_compass.adios_model.model import ADIOSStore, ADIOSGroup, ADIOSDataset, ADIOSKV

import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())