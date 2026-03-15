import math

Rvals = [10000, 12000, 15000, 18000, 22000, 27000, 33000, 39000, 47000, 56000, 68000, 82000, 100000,
         120000, 150000, 180000, 220000, 270000, 330000, 390000, 470000, 560000, 680000, 820000, 1000000]

CVals = [
    10*10**-12, 47*10**-12, 0.1*10**-9, 0.22*10**-9, 0.33*10**-9, 0.47*10**-9,
    0.68*10**-9, 1*10**-9, 1.5*10**-9, 2.2*10**-9, 3.3*10**-9, 4.7*10**-9,
    6.8*10**-9, 10*10**-9, 15*10**-9, 22*10**-9, 33*10**-9, 47*10**-9,
    68*10**-9, 0.1*10**-6, 0.15*10**-6, 0.47*10**-6, 1*10**-6, 4.7*10**-6
]

def lp_fc(C1, C2, R1, R2):
    return 1/(2*math.pi * math.sqrt(R1*R2*C1*C2))

def lp_q(C1, C2, R1, R2):
    return math.sqrt(R1*R2*C1*C2) / (C2 * (R1 + R2))

def hp_fc(C1, C2, R1, R2):
    return 1/(2*math.pi * math.sqrt(R1*R2*C1*C2))

def hp_q(C1, C2, R1, R2):
    return math.sqrt(R1*R2*C1*C2) / (R1 * (C1 + C2))

hp_results = []
lp_results = []

for r1 in Rvals:
    for r2 in Rvals:
        for c1 in CVals:
            for c2 in CVals:
                # low pass filter targeting 100Hz
                f_lp = lp_fc(c1, c2, r1, r2)
                q_lp = lp_q(c1, c2, r1, r2)
                if 95 <= f_lp <= 105 and 0.69 <= q_lp <= 0.724:
                    cost = abs(f_lp - 100)/100 + abs(q_lp - 0.707)/0.707 * 2
                    lp_results.append((cost, f_lp, q_lp, r1, r2, c1, c2))
                
                # high pass filter targeting 700Hz
                f_hp = hp_fc(c1, c2, r1, r2)
                q_hp = hp_q(c1, c2, r1, r2)
                if 685 <= f_hp <= 715 and 0.69 <= q_hp <= 0.724:
                    cost = abs(f_hp - 700)/700 + abs(q_hp - 0.707)/0.707 * 2
                    hp_results.append((cost, f_hp, q_hp, r1, r2, c1, c2))

lp_results.sort()
hp_results.sort()

print("Top Low Pass (100 Hz, Q~0.707):")
for res in lp_results[:5]:
    print(f"FC={res[1]:.1f}Hz, Q={res[2]:.3f} | R1={res[3]}, R2={res[4]}, C1={res[5]:.2e}, C2={res[6]:.2e}")

print("\nTop High Pass (700 Hz, Q~0.707):")
for res in hp_results[:5]:
    print(f"FC={res[1]:.1f}Hz, Q={res[2]:.3f} | R1={res[3]}, R2={res[4]}, C1={res[5]:.2e}, C2={res[6]:.2e}")
