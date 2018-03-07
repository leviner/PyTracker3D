# Minor(EV) = along (simrad) = y
# Major(EV) = Athwart (simrad) = x

# Beam compensation model for simrad Ex60/80 splitbeam systems
def BeamCompEX(uncompTS, along, athwart, BWalong, BWathwart):
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

def SingleTargetEx():
    R = r-(a*t)
    P = Ts - 40*np.log(R)- 2*alpha*R
