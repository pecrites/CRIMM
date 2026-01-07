class AutopilotMode:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.active = False

    def activate(self):
        self.active = True
        print("[AUTOPILOT] Mode autonome ACTIVÉ")

    def deactivate(self):
        self.active = False
        print("[AUTOPILOT] Mode autonome DÉSACTIVÉ")

    def run(self):
        if self.active:
            self.vehicle.accelerate(2)
            self.vehicle.steer(0)
