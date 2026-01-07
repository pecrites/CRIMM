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
# GESTION PROPRE DE CTRL + C
# ======================================================
running = True

def handle_exit(signum, frame):
    global running
    print("\n🛑 Interruption clavier détectée (Ctrl + C)")
    print("🧠 CRIMM va s’arrêter proprement après ce cycle…")
    running = False

signal.signal(signal.SIGINT, handle_exit)


# ======================================================
# PROGRAMME PRINCIPAL
# ======================================================
def main():
    print("\n" + "=" * 60)
    print("🚗 CRIMM — COCKPIT ROUTIER INTELLIGENT MULTI-MODES")
    print("☁️  Environnement : Cloud (RunPod)")
    print(f"🕒 Démarrage : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")

    # ==================================================
    # INITIALISATION DES MODULES
    # ==================================================
    print("🔧 Initialisation des modules…")

    vehicle = SimulatedVehicle()
    traffic = TrafficAnalyzer()
    safety = HumanOverride()

    # 🔴 CORRECTION IMPORTANTE ICI
    decision_engine = DecisionEngine(human_override=safety)

    mode_controller = ModeController()

    print("✅ Tous les modules sont prêts.\n")

    print("▶️ Simulation ACTIVE")
    print("ℹ️  Ctrl + C = arrêt propre\n")

    cycle = 0

    # ==================================================
    # BOUCLE PRINCIPALE (CONTINUE)
    # ==================================================
    while running:
        cycle += 1
        print("-" * 45)
        print(f"🔁 Cycle #{cycle}")

        # --- PERCEPTION ---
        traffic_state = traffic.analyze()
        print(f"👁️  Trafic détecté : {traffic_state}")

        # --- DÉCISION IA ---
        decision = decision_engine.decide(traffic_state)
        print(f"🧠 Décision IA : {decision}")

        # --- MODE ACTIF ---
        mode = mode_controller.get_current_mode(decision)
        print(f"🎛️  Mode actif : {mode}")

        # --- ACTION VÉHICULE ---
        vehicle.apply_decision(decision)
        print(f"🚘 Vitesse actuelle : {vehicle.speed} km/h")

        # --- SÉCURITÉ HUMAINE ---
        if safety.check_override():
            print("⚠️ Intervention humaine détectée — priorité chauffeur")
            break

        print("⏱️  Attente 2 secondes avant le prochain cycle...\n")
        time.sleep(2)

    # ==================================================
    # SORTIE PROPRE
    # ==================================================
    print("\n" + "=" * 60)
    print("🏁 SIMULATION CRIMM TERMINÉE")
    print("✅ Arrêt propre et contrôlé")
    print("=" * 60)

    input("\n🔚 Appuyez sur ENTRÉE pour fermer le programme...")


# ======================================================
if __name__ == "__main__":
    main()
