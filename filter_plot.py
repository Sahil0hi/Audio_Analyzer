import matplotlib.pyplot as plt
import numpy as np

# Data from user simulation
freq_range = np.logspace(1, 4, 500) # 10Hz to 10kHz
lp_target_fc = 100
lp_mag_at_fc = -3.35
hp_target_fc = 700
hp_mag_at_fc = -3.08

# Simulated Magnitude Curves (Approximated for visualization)
# Replace with your exported KiCad CSV data for the final report
def butterworth_lp(f, fc):
    return -10 * np.log10(1 + (f/fc)**4)

def butterworth_hp(f, fc):
    return -10 * np.log10(1 + (fc/f)**4)

plt.figure(figsize=(8, 5))
plt.semilogx(freq_range, butterworth_lp(freq_range, 96), label='Low-Pass Filter', color='blue')
plt.semilogx(freq_range, butterworth_hp(freq_range, 695), label='High-Pass Filter', color='red')

# Markers for your specific measurements
plt.plot(lp_target_fc, lp_mag_at_fc, 'bo')
plt.annotate(f'{lp_mag_at_fc} dB @ {lp_target_fc} Hz', (lp_target_fc, lp_mag_at_fc), 
             textcoords="offset points", xytext=(-20,10), ha='center', fontsize=9)

plt.plot(hp_target_fc, hp_mag_at_fc, 'ro')
plt.annotate(f'{hp_mag_at_fc} dB @ {hp_target_fc} Hz', (hp_target_fc, hp_mag_at_fc), 
             textcoords="offset points", xytext=(40,-15), ha='center', fontsize=9)

# Formatting
plt.axhline(-3, color='black', linestyle='--', alpha=0.5, label='-3 dB Threshold')
plt.title('Sallen-Key Filter Magnitude Response (KiCad Simulation)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.ylim(-40, 5)
plt.tight_layout()

# Save for Overleaf
plt.savefig('filter_response.pdf')
plt.show()
