from vehicle.simulated_vehicle import SimulatedVehicle
from safety.human_override import HumanOverride
from modes.autopilot_mode import AutopilotMode
from modes.safety_assist_mode import SafetyAssistMode
from modes.advisory_mode import AdvisoryMode
from modes.autopark_mode import AutoParkMode
from core.decision_engine import DecisionEngine
from core.mode_controller import ModeController
import time


print("\n[CRIMM] Initialisation du Cockpit Routier Intelligent...\n")

vehicle = SimulatedVehicle()
override = HumanOverride()

autopilot = AutopilotMode(vehicle)
safety = SafetyAssistMode(vehicle)
advisory = AdvisoryMode()
autopark = AutoParkMode(vehicle)

engine = DecisionEngine(override)

controller = ModeController(
    autopilot=autopilot,
    safety=safety,
    advisory=advisory,
    engine=engine,
    autopark=autopark
)

# ==============================
# ACTIVATION DES MODES
# ==============================

autopilot.activate()
safety.activate()

# ==============================
# SCÉNARIO 1 : CONDUITE + TRAFIC
# ==============================

print("\n--- SCÉNARIO 1 : Trafic & Conseils ---")

traffic_scenarios = {
    1: 0,  # fluide
    2: 1,  # dense
    3: 2,  # embouteillage
    4: 0,  # retour fluide
}

for step in range(1, 5):
    print(f"\n[TICK {step}]")
    controller.update(
        danger_level=0,
        traffic_level=traffic_scenarios[step]
    )
    time.sleep(1)

# ==============================
# SCÉNARIO 2 : STATIONNEMENT
# ==============================

print("\n--- SCÉNARIO 2 : Stationnement ---")
autopark.activate()

for _ in range(3):
    controller.update(danger_level=0, traffic_level=0)
    time.sleep(1)

# ==============================
# TEST OVERRIDE HUMAIN
# ==============================

print("\n--- TEST OVERRIDE HUMAIN ---")
override.activate()
controller.update(danger_level=2, traffic_level=2)

print("\n[CRIMM] Fin de la simulation.\n")
