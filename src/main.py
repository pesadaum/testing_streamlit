import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
from workers.create_wave import create_wave
from layouts.wave_sliders import wave_sliders

plt.style.use('dark_background')

st.title('Meu primeiro app Streamlit')
c1, c2 = st.columns(2)


omega_range = np.arange(-10*2*np.pi, 10*2*np.pi, np.pi/4).round(2)

'''
Primeira coluna
'''
c1.subheader('Primeira onda')
labels = [
    "Selecione um valor de amplitude para a primeira onda",
    "Selecione um valor de frequência angular $$[rad/s]$$ para  a primeira onda",
    "Selecione um valor de fase $$[\, ^\circ \,]$$ para  a primeira onda",]
amp, omega, phase = wave_sliders(labels, c1, omega_range)
t, y1 = create_wave(amp, omega, phase)

'''
Segunda Coluna
'''
c2.subheader('Segunda onda')
labels = [label.replace('primeira', 'segunda') for label in labels]
amp, omega, phase = wave_sliders(labels, c2, omega_range)
_, y2 = create_wave(amp, omega, phase)

'''
Gráficos
'''
data = pd.DataFrame({
    't': t,
    'y_1': y1,
    'y_2': y2,
    'Soma': y1 + y2
})

st.subheader('Resultado: ')


# f, ax = plt.subplots(figsize=(7, 4))

# ax.plot(data['t'], data['y_1'])
# ax.plot(data['t'], data['y_2'])
# ax.plot(data['t'], data['Soma'], '--')
# ax.legend(['$y_1$', '$y_2$', '$y_1 + y_2$'])

# st.pyplot(f)

fig = px.line(
    data,
    x="t",
    y=['y_1', 'y_2', 'Soma'],
)
st.plotly_chart(fig)
