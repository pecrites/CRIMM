from perception.traffic_analyzer import TrafficAnalyzer

class AdvisoryMode:
    def __init__(self):
        self.traffic = TrafficAnalyzer()

    def advise(self, traffic_level=0):
        message = self.traffic.analyze(traffic_level)
        print(f"[ADVISORY] {message}")
