import time
import signal
from datetime import datetime
import random

# ===== IMPORTS DU PROJET =====
from core.decision_engine import DecisionEngine
from core.mode_controller import ModeController

from modes.autopilot_mode import AutopilotMode
from modes.safety_assist_mode import SafetyAssistMode
from modes.advisory_mode import AdvisoryMode
from modes.autopark_mode import AutoParkMode

from vehicle.simulated_vehicle import SimulatedVehicle
from perception.traffic_analyzer import TrafficAnalyzer
from safety.human_override import HumanOverride


# ======================================================
# GESTION PROPRE DE CTRL + C
# ======================================================
running = True

def handle_exit(signum, frame):
    global running
    print("\n🛑 Interruption clavier détectée (Ctrl + C)")
    print("🧠 CRIMM va s’arrêter proprement…")
    running = False

signal.signal(signal.SIGINT, handle_exit)


# ======================================================
# PROGRAMME PRINCIPAL
# ======================================================
def main():
    print("\n" + "=" * 65)
    print("🚗 CRIMM — COCKPIT ROUTIER INTELLIGENT MULTI-MODES")
    print("☁️  Environnement : Cloud (RunPod)")
    print(f"🕒 Démarrage : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65 + "\n")

    # ==================================================
    # INITIALISATION DES MODULES
    # ==================================================
    print("🔧 Initialisation des modules…")

    vehicle = SimulatedVehicle()
    traffic = TrafficAnalyzer()
    safety = HumanOverride()

    decision_engine = DecisionEngine(human_override=safety)

    autopilot = AutopilotMode(vehicle)
    safety_mode = SafetyAssistMode(vehicle)
    advisory = AdvisoryMode()
    autopark = AutoParkMode(vehicle)

    mode_controller = ModeController(
        autopilot=autopilot,
        safety=safety_mode,
        advisory=advisory,
        engine=decision_engine,
        autopark=autopark
    )

    print("✅ Tous les modules sont prêts.\n")

    print("▶️ Simulation ACTIVE")
    print("ℹ️  Ctrl + C = arrêt propre\n")

    cycle = 0

    # ==================================================
    # BOUCLE PRINCIPALE
    # ==================================================
    while running:
        cycle += 1
        print("-" * 45)
        print(f"🔁 Cycle #{cycle}")

        # 🔹 SIMULATION DU NIVEAU DE TRAFIC (0 à 100)
        traffic_level = random.randint(0, 100)

        # 🔹 PERCEPTION
        traffic_state = traffic.analyze(traffic_level)
        print(f"👁️  Trafic (niveau {traffic_level}) : {traffic_state}")

        # 🔹 DÉCISION IA
        decision = decision_engine.decide(traffic_state)
        print(f"🧠 Décision IA : {decision}")

        # 🔹 MODE ACTIF
        active_mode = mode_controller.get_current_mode(decision)
        print(f"🎛️  Mode actif : {active_mode}")

        # 🔹 EXÉCUTION DU MODE
        active_mode.execute(decision)

        print(f"🚘 Vitesse actuelle : {vehicle.speed} km/h")

        # 🔹 SÉCURITÉ HUMAINE
        if safety.check_override():
            print("⚠️ Intervention humaine détectée — priorité chauffeur")
            break

        print("⏱️  Attente 2 secondes avant le prochain cycle...\n")
        time.sleep(2)

    # ==================================================
    # SORTIE PROPRE
    # ==================================================
    print("\n" + "=" * 65)
    print("🏁 SIMULATION CRIMM TERMINÉE")
    print("✅ Arrêt propre et contrôlé")
    print("=" * 65)

    input("\n🔚 Appuyez sur ENTRÉE pour fermer le programme...")


# ======================================================
if __name__ == "__main__":
    main()
