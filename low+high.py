import numpy as np
import matplotlib.pyplot as plt

# Sallen-Key Low-Pass Filter Parameters
R1 = 10e3  # 10k Ohm
R2 = 10e3  # 10k Ohm
C1 = 22.5e-9 # 22.5 nF
C2 = 11.25e-9 # 11.25 nF

# Frequency vector
f = np.logspace(0, 5, 1000)
s = 2j * np.pi * f

# Transfer Function: H(s) = 1 / (1 + s*C2*(R1+R2) + s^2*C1*C2*R1*R2)
H = 1 / (1 + s*C2*(R1+R2) + s**2*C1*C2*R1*R2)

mag = 20 * np.log10(np.abs(H))
phase = np.angle(H, deg=True)
fc = 1 / (2 * np.pi * np.sqrt(R1 * R2 * C1 * C2))

# Global Formatting
plt.rcParams.update({'font.size': 12, 'font.family': 'serif', 'text.usetex': False})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Magnitude Response
ax1.semilogx(f, mag, color='#1f77b4', linewidth=2, label='Transfer Function $H(s)$')
ax1.axvline(fc, color='darkred', linestyle='--', label=f'$f_c = {fc/1000:.2f}$ kHz')
ax1.axhline(-3, color='gray', linestyle=':', alpha=0.6)
ax1.set_ylabel('Magnitude (dB)')
ax1.set_ylim([-60, 5])
ax1.grid(True, which="both", ls="-", alpha=0.3)
ax1.legend(loc='lower left')
ax1.set_title('Sallen-Key Second-Order Low-Pass Filter Bode Plot')

# Phase Response
ax2.semilogx(f, phase, color='#ff7f0e', linewidth=2)
ax2.axvline(fc, color='darkred', linestyle='--')
ax2.set_ylabel('Phase (Degrees)')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_yticks([0, -45, -90, -135, -180])
ax2.grid(True, which="both", ls="-", alpha=0.3)

plt.tight_layout()
plt.savefig('professional_bode_plot.png', dpi=300)
plt.show()
