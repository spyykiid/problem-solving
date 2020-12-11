from __future__ import division
from math import atan2, degrees
AB = int(raw_input())
BC = int(raw_input())
print str(int(round(degrees(atan2(AB, BC))))) + '°'
