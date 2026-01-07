class AutoParkMode:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.active = False
        self.step = 0

    def activate(self):
        self.active = True
        self.step = 0
        print("[AUTOPARK] Mode stationnement ACTIVÉ")

    def deactivate(self):
        self.active = False
        print("[AUTOPARK] Mode stationnement DÉSACTIVÉ")

    def run(self, danger_level=0):
        """
        Stationnement simulé en 3 étapes lentes :
        1) Avancer doucement
        2) Tourner le volant
        3) Freinage final
        """
        if not self.active:
            return

        if danger_level > 0:
            print("[AUTOPARK] Danger détecté → arrêt immédiat")
            self.vehicle.brake_emergency()
            self.deactivate()
            return

        if self.step == 0:
            print("[AUTOPARK] Avance lente")
            self.vehicle.accelerate(1)
            self.step += 1

        elif self.step == 1:
            print("[AUTOPARK] Braquage pour manœuvre")
            self.vehicle.steer(30)
            self.step += 1

        elif self.step == 2:
            print("[AUTOPARK] Freinage final – stationnement terminé")
            self.vehicle.brake_soft()
            self.deactivate()
