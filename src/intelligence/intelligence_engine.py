class IntelligenceEngine:
    def process(self, event):
        """
        Converts raw event into an internal state representation.
        This is data profiling + feature abstraction.
        """

        attributes = event.get("attributes", {})

        state = {
            "event_id": event.get("event_id"),
            "timestamp": event.get("timestamp"),
            "num_features": len(attributes),
            "numeric_summary": {},
        }

        for key, value in attributes.items():
            if isinstance(value, (int, float)):
                state["numeric_summary"][key] = {
                    "value": value,
                    "is_high": value > 10000
                }

        return state
