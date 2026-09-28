import numpy as np
import matplotlib.pyplot as plt
import control as ct

# ---------------------------------------------------------
# Define the open-loop transfer function
#
#              10
# G(s) = -----------------
#              s+10
# ---------------------------------------------------------

s = ct.TransferFunction.s
#G = 10 / (s * (s + 1) * (s + 5))
G = 10/ (s + 10)

print("Transfer Function:")
print(G)

# ---------------------------------------------------------
# Calculate stability margins
# ---------------------------------------------------------

gm, pm, wcg, wcp = ct.margin(G)

# Gain margin in dB
gm_db = 20 * np.log10(gm)

print("\n----- Stability Margins -----")
print(f"Gain Margin       = {gm_db:.2f} dB")
print(f"Phase Margin      = {pm:.2f} deg")
print(f"Phase crossover   = {wcg:.2f} rad/s")
print(f"Gain crossover    = {wcp:.2f} rad/s")

# ---------------------------------------------------------
# Bode plot with margins
# ---------------------------------------------------------

ct.bode_plot(
    G,
    dB=True,
    Hz=False,
    deg=True,
    grid=True,
    margins=True
)

plt.show()