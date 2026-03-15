# Audio Analyzer

An analog audio analyzer circuit that partitions the audible frequency spectrum into a **low-frequency band** and a **high-frequency band** using two active second-order Sallen-Key filters, followed by peak detection on each band.

---

## Overview

This project implements a hardware audio analyzer that:

1. **Accepts an audio input signal** spanning the audible frequency range (20 Hz – 20 kHz).
2. **Splits the spectrum** into a low-frequency band and a high-frequency band using a pair of active second-order Sallen-Key filters.
3. **Detects the peak amplitude** of each filtered band independently, providing a simple visual or measurable indication of signal energy in each frequency region.

---

## System Architecture

```
Audio Input
     │
     ├──────────────────────┐
     │                      │
     ▼                      ▼
┌─────────────┐      ┌─────────────┐
│  Low-Pass   │      │  High-Pass  │
│ Sallen-Key  │      │ Sallen-Key  │
│   Filter    │      │   Filter    │
│ (2nd Order) │      │ (2nd Order) │
└──────┬──────┘      └──────┬──────┘
       │                    │
       ▼                    ▼
┌─────────────┐      ┌─────────────┐
│    Peak     │      │    Peak     │
│  Detector   │      │  Detector   │
└─────────────┘      └─────────────┘
       │                    │
       ▼                    ▼
  Low-Band Output    High-Band Output
```

---

## Filter Design

### Sallen-Key Topology

Both filters use the **Sallen-Key** active filter topology, which is a second-order filter built around an operational amplifier configured as a unity-gain (voltage follower) or fixed-gain buffer. Key properties:

- **Second-order** roll-off: –40 dB/decade (–12 dB/octave) beyond the cutoff frequency.
- **Active** design: uses an op-amp to achieve gain and buffering, eliminating the need for inductors.
- **Low output impedance**: the op-amp buffer ensures the filter output can drive subsequent stages without loading the filter network.

### Low-Pass Filter

The low-pass Sallen-Key filter passes frequencies **below** the chosen crossover frequency and attenuates higher frequencies. It captures the bass and lower-midrange content of the audio signal.

```
          R1          R2
Vin ──┬──/\/\/──┬──/\/\/──┬── V+ ──[Op-Amp]──┬── Vout
      │         │         │                   │
      │        C1        C2                   │
      │         │         │                   │
      └─────────┴─────────┴───────────────────┘
                        GND
```

### High-Pass Filter

The high-pass Sallen-Key filter passes frequencies **above** the crossover frequency, capturing the upper-midrange and treble content of the audio signal.

```
          C1          C2
Vin ──┬──┤├──┬──┤├──┬── V+ ──[Op-Amp]──┬── Vout
      │      │      │                   │
      │      R1     R2                  │
      │      │      │                   │
      └──────┴──────┴───────────────────┘
                   GND
```

### Design Equations

For a second-order Sallen-Key filter with Butterworth response (Q = 0.707):

| Parameter | Symbol | Relationship |
|-----------|--------|--------------|
| Cutoff frequency (general) | f₀ | f₀ = 1 / (2π √(R1·R2·C1·C2)) |
| Cutoff frequency (R1=R2=R, C1=C2=C) | f₀ | f₀ = 1 / (2πRC) |
| Quality factor | Q | Q = √(R1·R2·C1·C2) / (C2·(R1+R2)) |
| Roll-off | — | –40 dB/decade beyond f₀ |

> For a Butterworth (maximally flat) response set Q = 0.707 by choosing component values that satisfy the Q equation. A common simplification is to use equal resistors (R1 = R2 = R) and set C1 = 2C and C2 = C, which yields Q ≈ 0.707 and f₀ = 1 / (2πR√2·C).

---

## Peak Detection

Each filter output feeds an independent **peak detector** circuit. The peak detector captures and holds the maximum (peak) voltage of the filtered signal, giving a DC level proportional to the signal amplitude in that frequency band.

A basic envelope/peak detector consists of:
- A **diode** that charges a hold capacitor to the signal peak.
- A **hold capacitor** that stores the peak voltage.
- A **bleed resistor** that slowly discharges the capacitor, setting the decay time constant.
- An **op-amp buffer** at the output to prevent loading the hold capacitor.

---

## Frequency Bands

| Band | Filter Type | Typical Cutoff | Content |
|------|-------------|----------------|---------|
| Low  | 2nd-order Sallen-Key Low-Pass  | ~1 kHz | Bass, kick drum, low-mids |
| High | 2nd-order Sallen-Key High-Pass | ~1 kHz | Presence, treble, hi-hats |

> The crossover frequency can be adjusted by changing the R and C component values in each filter stage.

---

## Components

| Component | Quantity | Purpose |
|-----------|----------|---------|
| Operational Amplifier (e.g., TL072, LM358) | 4 | 2× filter buffers, 2× peak-detector buffers |
| Resistors | 8+ | Sallen-Key filter networks |
| Capacitors | 4+ | Sallen-Key filter networks |
| Diodes (e.g., 1N4148) | 2 | Peak detector rectification |
| Hold capacitors | 2 | Peak detector storage |
| Bleed resistors | 2 | Peak detector decay |

---

## Getting Started

1. **Select a crossover frequency** for your application (e.g., 1 kHz divides bass from treble).
2. **Calculate R and C values** using the design equations above for each Sallen-Key filter.
3. **Assemble the circuit** on a breadboard or PCB following the schematic for each filter and peak detector stage.
4. **Apply an audio signal** to the input (ensure signal levels are within the op-amp's supply range).
5. **Observe the peak detector outputs** — the low-band output rises with bass content; the high-band output rises with treble content.

---

## Applications

- Audio spectrum visualization (VU meters, equalizer displays)
- Crossover networks for multi-band processing
- Signal analysis and measurement
- Educational demonstration of active filter design

---

## License

This project is open source. See [LICENSE](LICENSE) for details.
