import random
import time
from datetime import datetime

class Observer:
    def observe(self):
        """
        Simulates ingestion of a real-time financial event.
        This will later be replaced by Kafka / API / DB streams.
        """

        event = {
            "event_id": random.randint(100000, 999999),
            "timestamp": datetime.utcnow().isoformat(),
            "attributes": {
                "amount": round(random.uniform(10, 50000), 2),
                "velocity": random.randint(1, 10),
                "location_change": random.choice([0, 1]),
                "device_change": random.choice([0, 1])
            }
        }

        time.sleep(0.5)  # simulate streaming delay
        return event
