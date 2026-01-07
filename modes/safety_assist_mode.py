class SafetyAssistMode:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.active = False
        self.control_taken = False

    def activate(self):
        self.active = True
        print("[SAFETY] Mode danger AVANCÉ ACTIVÉ")

    def deactivate(self):
        self.active = False
        self.control_taken = False
        print("[SAFETY] Mode danger DÉSACTIVÉ")

    def run(self, danger_level=0):
        """
        danger_level:
        0 = aucun danger
        1 = danger léger (freinage doux)
        2 = danger critique (prise de contrôle temporaire)
        """

        if not self.active:
            return

        if danger_level == 1:
            print("[SAFETY] Danger léger détecté → freinage préventif")
            self.vehicle.brake_soft()

        elif danger_level == 2:
            print("[SAFETY] DANGER CRITIQUE → PRISE DE CONTRÔLE")
            self.control_taken = True
            self.vehicle.brake_emergency()

        else:
            if self.control_taken:
                print("[SAFETY] Situation stabilisée → contrôle rendu au chauffeur")
                self.control_taken = False
