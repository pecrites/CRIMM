class HumanOverride:
    def __init__(self):
        self.override = False

    def activate(self):
        self.override = True
        print("[HUMAN] Override humain ACTIVÉ")

    def reset(self):
        self.override = False
