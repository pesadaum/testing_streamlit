import numpy as np


def create_wave(amp, omega, phase, _npoints=2000, _from=-2*np.pi, _to=2*np.pi):
    t = np.linspace(_from, _to, _npoints)
    return t, amp * np.sin(omega*t + np.radians(phase))
