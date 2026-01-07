class TrafficAnalyzer:
    def analyze(self, traffic_level):
        """
        traffic_level:
        0 = fluide
        1 = dense
        2 = embouteillage
        """

        if traffic_level == 0:
            return "Trafic fluide – vitesse stable recommandée."

        elif traffic_level == 1:
            return "Trafic dense – vigilance accrue, ralentissement conseillé."

        elif traffic_level == 2:
            return "Embouteillage détecté – itinéraire alternatif recommandé."

        else:
            return "Analyse trafic indisponible."
