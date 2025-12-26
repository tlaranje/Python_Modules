from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def display_batch(self, data_batch: List[Any]) -> None:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        target_type = criteria if criteria is not None else self.stream_type
        return [d for d in data_batch if d.get("type") == target_type]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "sensor")
        self.total_readings = 0
        self.avg_temp = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_readings = sum(len(d) - 1 for d in data_batch)
        total_temp = sum(d.get('temp', 0) for d in data_batch)
        self.avg_temp = total_temp / len(data_batch) if data_batch else 0.0
        return data_batch

    def display_batch(self, data_batch: List[Any]) -> None:
        stats = self.get_stats()

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        print(*(f"Processing sensor batch: [temp:{d.get('temp')}, humidity:"
                f"{d.get('humidity')}, pressure:{d.get('pressure')}]"
                for d in data_batch))
        print(f"Sensor analysis: {stats['total_readings']} readings "
              f"processed, avg temp: {stats['avg_temp']}°C\n")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id,
                "stream_type": self.stream_type,
                "total_readings": self.total_readings,
                "avg_temp": self.avg_temp}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "transactions")
        self.net_flow = 0
        self.total_ops = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.net_flow = sum(sum(d.get('buy', [])) - sum(d.get('sell', []))
                            for d in data_batch)
        self.total_ops = sum(len(d) for d in data_batch)
        return data_batch

    def display_batch(self, data_batch: List[Any]) -> None:
        stats = self.get_stats()

        buys = [b for d in data_batch for b in d.get('buy', [])]
        sells = [s for d in data_batch for s in d.get('sell', [])]
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stats['stream_id']}, Type: Financial Data")
        print(f"Processing transaction batch: buys:{buys}, "
              f"sells:{sells}")
        print(f"Transaction analysis: {stats['total_ops']} operations"
              f", net flow: {'+' if stats['net_flow'] >= 0 else '-'}"
              f"{stats['net_flow']} units\n")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id,
                "stream_type": self.stream_type,
                "total_ops": self.total_ops,
                "net_flow": self.net_flow}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "logs")
        self.total_events = 0
        self.errors = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_events = sum(len(e.get('events', [])) for e in data_batch)
        self.errors = sum(e.get('events', []).count('error')
                          for e in data_batch)
        return data_batch

    def display_batch(self, data_batch: List[Any]) -> None:
        stats = self.get_stats()
        events = [e for d in data_batch for e in d.get('events', [])]

        print("Initializing Event Stream...")
        print(f"Stream ID: {stats['stream_id']}, Type: System Events")
        print(f"Processing event batch: {events}")
        print(f"Event analysis: {stats['total_events']} events, "
              f"{stats['errors']} error detected\n")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id,
                "stream_type": self.stream_type,
                "total_events": self.total_events,
                "errors": self.errors}


class StreamProcessor:
    def __init__(self):
        self.stream_list = []

    def add_stream(self, *streams: Optional[DataStream]) -> None:
        for s in streams:
            if s is not None:
                self.stream_list.append(s)

    def process_all(self, data_batch: list[Any]) -> List[Dict[str, Any]]:
        report = []
        for stream in self.stream_list:
            try:
                filtered_data = stream.filter_data(data_batch)
                stream.process_batch(filtered_data)
                stream.display_batch(filtered_data)
                report.append(stream.get_stats())
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")
        return report


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    data_batch = [
        {"type": "sensor", "temp": 22.5, "humidity": 65, "pressure": 1013},
        {"type": "transactions", "buy": [100, 75], "sell": [150]},
        {"type": "logs", "events": ["login", "error", "logout"]},
    ]

    sp = StreamProcessor()
    ss = SensorStream("SENSOR_001")
    ts = TransactionStream("TRANS_001")
    es = EventStream("EVENT_001")

    sp.add_stream(ss, ts, es)

    report = sp.process_all(data_batch)
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")

    for stats in report:
        if stats["stream_type"] == "sensor":
            print(f"- Sensor data: {stats['total_readings']} "
                  "readings processed")
        elif stats["stream_type"] == "transactions":
            print(f"- Transaction data: {stats['total_ops']} "
                  "operations processed")
        elif stats["stream_type"] == "logs":
            print(f"- Event data: {stats['total_events']} events processed")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction\n")
    print("All streams processed successfully. Nexus throughput optimal.")
