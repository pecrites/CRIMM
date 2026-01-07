class SimulatedVehicle:
    def __init__(self):
        self.speed = 0
        self.steering = 0

    def accelerate(self, value):
        self.speed += value
        print(f"[VEHICLE] Accélération → {self.speed} km/h")

    def brake_soft(self):
        self.speed = max(0, self.speed - 5)
        print("[VEHICLE] Freinage doux")

    def brake_emergency(self):
        self.speed = 0
        print("[VEHICLE] FREINAGE D'URGENCE")

    def steer(self, value):
        self.steering = value
        print(f"[VEHICLE] Direction → {value}")
