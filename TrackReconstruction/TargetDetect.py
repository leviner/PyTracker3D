'''
This will serve as a library of functions for conducting
single target detection on Simrad Ex format split-beam data.

The dataformat goal is to be able to provide all of the information
from a single ping (as vectors) and be able to return beam compensated
target strength and a logic mask of single targets in the same shape
as input data.  For single target detection, user defined parameters can
be defined or defaults will be assigned

The code below is based on the algorithms for single target detection
utlized by Echoview (Echoview Software Pty Ltd).

Note on angles:
y = Minor (EV) = Along (Simrad)
x = Major (EV) = Athwart (Simrad)
'''

def BeamCompEX(uncompTS, along, athwart, BWalong, BWathwart):
# Beam compensation model for simrad Ex60/80 splitbeam systems
    #α is the minor-axis angle of the single target+ (degrees)
    #β is the major-axis angle of the single target+ (degrees)
    #TS(0,0) is the TS derived from received power measurements - valid at α=0, β=0 (dB re 1 m2) - see uncompensated_TS
    #TS(α,β) is the TS predicted for a target at position α, β in the beam (dB re 1 m2) - see compensated_TS
    #B(α,β) is the beam compensation function (dB).
    x = (2*along)/BWalong
    y = (2*athwart)/BWathwart
    B = 6.0206*( x**2 + y**2 - 0.18*(x**2)*(y**2))
    compTS = uncompTS+B
    return compTS

def SingleTargetEx(TSMin=-50, PLDL=6, MinPL=.7, MaxPL=1.5, MaxBeamComp=4.0, MaxStdevAlong=.6, MaxStdevAthwart=.6):
    # Limits from the user:
    # - TS threshold (min TS)
    # - Pulse Length Determination Level
    # - Minimum normalized pulse length
    # - Maximum normalized pulse length
    # - Maximum beam compensati on
    # - Maximum stdev of minor/along angle
    # - Maximum stdev of major/athwart angle
    R = r-(a*t)
    P = Ts - 40*np.log(R)- 2*alpha*R
