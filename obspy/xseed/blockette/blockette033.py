# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from obspy.xseed.blockette import Blockette
from obspy.xseed.fields import Integer, VariableString


class Blockette033(Blockette):
    """
    Blockette 033: Generic Abbreviation Blockette.

    Sample:
    0330055001(GSN) Global Seismograph Network (IRIS/USGS)~
    """
    id = 33
    name = "Generic Abbreviation"
    fields = [
        Integer(3, "Abbreviation lookup code", 3),
        VariableString(4, "Abbreviation description", 1, 50, 'UNLPS')
    ]
