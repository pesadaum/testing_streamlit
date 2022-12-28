

def wave_sliders(labels, col, omega_range):
    amp = col.slider(
        labels[0], 0, 10, step=1)
    omega = col.select_slider(
        labels[1], omega_range)
    phase = col.slider(
        labels[2], -360, 360, step=45, )

    return amp, omega, phase
