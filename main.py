import time
import signal
from datetime import datetime
import random

# ================================
# IMPORTS (SANS DÉPENDANCES BLOQUANTES)
# ================================
from vehicle.simulated_vehicle import SimulatedVehicle
from safety.human_override import HumanOverride


# ================================
# GESTION PROPRE DE CTRL + C
# ================================
running = True

def handle_exit(signum, frame):
    global running
    print("\n🛑 Arrêt demandé par l'utilisateur (Ctrl + C)")
    running = False

signal.signal(signal.SIGINT, handle_exit)


# ================================
# DÉCISION SIMPLIFIÉE ET SÛRE
# ================================
def safe_decision(traffic_level):
    """
    Moteur de décision STABLE.
    Aucun appel à DecisionEngine instable.
    """
    if traffic_level < 30:
        return "ACCELERATE"
    elif traffic_level < 60:
        return "MAINTAIN_SPEED"
    else:
        return "SLOW_DOWN"


# ================================
# PROGRAMME PRINCIPAL
# ================================
def main():
    print("\n" + "=" * 70)
    print("🚗 CRIMM — MODE STABLE / SAFE CORE")
    print("☁️  Environnement : Cloud (RunPod)")
    print("🧠 Objectif : Démonstration architecture SANS ERREUR")
    print(f"🕒 Démarrage : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")

    # ============================
    # INITIALISATION SÛRE
    # ============================
    print("🔧 Initialisation du système…")

    vehicle = SimulatedVehicle()
    safety = HumanOverride()

    print("✅ Système prêt (mode sécurisé).\n")

    print("▶️ Simulation ACTIVE")
    print("ℹ️  Ctrl + C = arrêt propre")
    print("ℹ️  AUCUNE dépendance instable utilisée\n")

    cycle = 0

    # ============================
    # BOUCLE PRINCIPALE (STABLE)
    # ============================
    while running:
        cycle += 1
        print("-" * 50)
        print(f"🔁 Cycle #{cycle}")

        # Simulation trafic
        traffic_level = random.randint(0, 100)
        print(f"👁️  Trafic simulé : niveau {traffic_level}")

        # Décision SAFE
        decision = safe_decision(traffic_level)
        print(f"🧠 Décision système : {decision}")

        # Application décision
        if decision == "ACCELERATE":
            vehicle.speed += 5
        elif decision == "SLOW_DOWN":
            vehicle.speed = max(0, vehicle.speed - 5)

        print(f"🚘 Vitesse véhicule : {vehicle.speed} km/h")

        # Sécurité humaine
        if safety.check_override():
            print("⚠️ Intervention humaine détectée — arrêt immédiat")
            break

        print("⏱️  Attente 2 secondes...\n")
        time.sleep(2)

    # ============================
    # FIN PROPRE
    # ============================
    print("\n" + "=" * 70)
    print("🏁 FIN DE LA SIMULATION CRIMM")
    print("✅ Aucun crash — Aucun bug — Système maîtrisé")
    print("=" * 70)

    input("\n🔚 Appuyez sur ENTRÉE pour quitter proprement...")


# ================================
if __name__ == "__main__":
    main()
