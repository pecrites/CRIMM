class DecisionEngine:
    def __init__(self, human_override):
        self.human_override = human_override

    def can_run_autonomy(self):
        if self.human_override.override:
            print("[ENGINE] Autonomie REFUSÉE (override humain)")
            return False
        return True
