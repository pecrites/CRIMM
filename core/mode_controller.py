class ModeController:
    def __init__(self, autopilot, safety, advisory, engine, autopark):
        self.autopilot = autopilot
        self.safety = safety
        self.advisory = advisory
        self.engine = engine
        self.autopark = autopark

    def update(self, danger_level=0, traffic_level=0):
        # MODE CONSEIL (toujours actif)
        self.advisory.advise(traffic_level=traffic_level)

        # MODE DANGER (priorité absolue)
        if danger_level > 0:
            self.safety.run(danger_level=danger_level)
            return

        # MODE STATIONNEMENT
        if self.autopark.active:
            self.autopark.run(danger_level=danger_level)
            return

        # MODE AUTONOME
        if self.engine.can_run_autonomy():
            self.autopilot.run()
