import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# -------------------------------------------------
# Model is a spring-mass-damper system
# m*h_ddot + c*h_dot + k*h = u
# -------------------------------------------------

m = 1.0      # effective mass
c = 1.2      # damping
k = 1.0      # virtual restoring stiffness

s = ctrl.TransferFunction.s
G = 1 / (m*s**2 + c*s + k)

# -------------------------------------------------
# Controllers
# -------------------------------------------------

# P control
C_P = 10.0

# PI control
#C_PI = 4.0 + 0.8/s
C_PI = 10.0 + 1.8/s

# PID control with derivative filter
N = 20
C_PID = 10.0 + 1.8/s + (1.5*N*s)/(s + N)

# -------------------------------------------------
# Closed-loop transfer functions
# -------------------------------------------------

T_P = ctrl.feedback(C_P * G, 1)
T_PI = ctrl.feedback(C_PI * G, 1)
T_PID = ctrl.feedback(C_PID * G, 1)

# -------------------------------------------------
# Step response: target height = 1 unit
# -------------------------------------------------

t = np.linspace(0, 20, 1000)

t_P, y_P = ctrl.step_response(T_P, t)
t_PI, y_PI = ctrl.step_response(T_PI, t)
t_PID, y_PID = ctrl.step_response(T_PID, t)

# -------------------------------------------------
# Plot
# -------------------------------------------------

plt.figure(figsize=(9, 5))
plt.plot(t_P, y_P, label="P Control- Kp =10")
plt.plot(t_PI, y_PI, label="PI Control- Kp =10, Ki = 1.8")
#plt.plot(t_PID, y_PID, label="PID Control")
plt.axhline(1, linestyle="--", label="Target Height")

plt.xlabel("Time (s)")
plt.ylabel("Height")
plt.title("Iron Man Hovering System: P, PI and PID Control")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()