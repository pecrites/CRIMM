import time
import signal
from datetime import datetime
import random

from vehicle.simulated_vehicle import SimulatedVehicle


# ======================================================
# GESTION PROPRE DE CTRL + C (INFAILLIBLE)
# ======================================================
running = True

def handle_exit(signum, frame):
    global running
    print("\n🛑 Arrêt demandé par l'utilisateur (Ctrl + C)")
    running = False

signal.signal(signal.SIGINT, handle_exit)


# ======================================================
# MOTEUR DE DÉCISION LOCAL (AUCUNE DÉPENDANCE)
# ======================================================
def safe_decision(traffic_level):
    if traffic_level < 30:
        return "ACCELERATE"
    elif traffic_level < 60:
        return "MAINTAIN"
    else:
        return "SLOW_DOWN"


# ======================================================
# PROGRAMME PRINCIPAL
# ======================================================
def main():
    print("\n" + "=" * 70)
    print("🚗 CRIMM — MODE STABLE ABSOLU (NO-FAIL)")
    print("☁️  Environnement : Cloud (RunPod)")
    print("🛡️  Objectif : AUCUNE ERREUR POSSIBLE")
    print(f"🕒 Démarrage : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")

    # Initialisation minimale et sûre
    print("🔧 Initialisation du véhicule…")
    vehicle = SimulatedVehicle()
    print("✅ Véhicule prêt.\n")

    print("▶️ Simulation ACTIVE")
    print("ℹ️  Ctrl + C = arrêt propre")
    print("ℹ️  Aucun module externe instable utilisé\n")

    cycle = 0

    # ==================================================
    # BOUCLE PRINCIPALE (INCASSABLE)
    # ==================================================
    while running:
        cycle += 1
        print("-" * 50)
        print(f"🔁 Cycle #{cycle}")

        traffic_level = random.randint(0, 100)
        print(f"👁️  Trafic simulé : niveau {traffic_level}")

        decision = safe_decision(traffic_level)
        print(f"🧠 Décision système : {decision}")

        if decision == "ACCELERATE":
            vehicle.speed += 5
        elif decision == "SLOW_DOWN":
            vehicle.speed = max(0, vehicle.speed - 5)

        print(f"🚘 Vitesse véhicule : {vehicle.speed} km/h")

        print("⏱️  Attente 2 secondes...\n")
        time.sleep(2)

    # ==================================================
    # SORTIE PROPRE
    # ==================================================
    print("\n" + "=" * 70)
    print("🏁 FIN DE LA SIMULATION CRIMM")
    print("✅ ZÉRO ERREUR — SYSTÈME STABLE")
    print("=" * 70)
    input("\n🔚 Appuyez sur ENTRÉE pour quitter...")


# ======================================================
if __name__ == "__main__":
    main()
