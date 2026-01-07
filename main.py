import time
import signal
import sys
from datetime import datetime

# === IMPORTS DU PROJET ===
from core.decision_engine import DecisionEngine
from core.mode_controller import ModeController
from vehicle.simulated_vehicle import SimulatedVehicle
from perception.traffic_analyzer import TrafficAnalyzer
from safety.human_override import HumanOverride


# ======================================================
# GESTION PROPRE DE L’ARRÊT (Ctrl + C)
# ======================================================
running = True

def handle_exit(signum, frame):
    global running
    print("\n🛑 Interruption détectée (Ctrl + C)")
    print("🧠 CRIMM se prépare à s’arrêter proprement...")
    running = False

signal.signal(signal.SIGINT, handle_exit)


# ======================================================
# PROGRAMME PRINCIPAL
# ======================================================
def main():
    print("\n" + "=" * 55)
    print("🚗 CRIMM — COCKPIT ROUTIER INTELLIGENT MULTI-MODES")
    print("☁️  Environnement : Cloud (RunPod)")
    print(f"🕒 Démarrage : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55 + "\n")

    # Initialisation
    print("🔧 Initialisation des modules...")
    vehicle = SimulatedVehicle()
    traffic = TrafficAnalyzer()
    safety = HumanOverride()
    decision_engine = DecisionEngine()
    mode_controller = ModeController()
    print("✅ Tous les modules sont prêts.\n")

    print("▶️ Simulation ACTIVE")
    print("ℹ️  Appuyez sur Ctrl + C pour arrêter proprement\n")

    cycle = 0

    # ==================================================
    # BOUCLE PRINCIPALE (NE S’ARRÊTE PAS TOUTE SEULE)
    # ==================================================
    while running:
        cycle += 1
        print("-" * 40)
        print(f"🔁 Cycle #{cycle}")

        # Perception
        traffic_state = traffic.analyze()
        print(f"👁️  Trafic : {traffic_state}")

        # Décision IA
        decision = decision_engine.decide(traffic_state)
        print(f"🧠 Décision IA : {decision}")

        # Mode actif
        mode = mode_controller.get_current_mode(decision)
        print(f"🎛️  Mode actif : {mode}")

        # Action véhicule
        vehicle.apply_decision(decision)
        print(f"🚘 Vitesse : {vehicle.speed} km/h")

        # Sécurité humaine
        if safety.check_override():
            print("⚠️ Intervention humaine PRIORITAIRE")
            break

        print("⏱️  Attente 2 secondes avant le prochain cycle...\n")
        time.sleep(2)

    # ==================================================
    # SORTIE PROPRE
    # ==================================================
    print("\n" + "=" * 55)
    print("🏁 SIMULATION CRIMM TERMINÉE")
    print("✅ Arrêt propre et contrôlé")
    print("=" * 55)

    input("\n🔚 Appuyez sur ENTRÉE pour fermer le programme...")


# ======================================================
if __name__ == "__main__":
    main()
