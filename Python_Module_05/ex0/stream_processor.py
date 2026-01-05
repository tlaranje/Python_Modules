from abc import ABC, abstractmethod
from typing import Any, List, Dict


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            return all(isinstance(d, (int, float)) for d in data)
        except Exception:
            return False

    def process(self, data: Any) -> str:
        return (f"Processed {len(data)} numeric values, "
                f"sum={sum(data)}, "
                f"avg={sum(data) / len(data)}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            text = str(data).strip()
            return bool(text) and ":" not in text.split(" ", 1)[0]
        except Exception:
            return False

    def process(self, data: Any) -> str:
        return str(f"Processed text: {len(data)} characters, "
                   f"{len(str(data).split())} words")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if ":" not in data:
                return False
            log_type, message = data.split(":", 1)
            return log_type.isupper() and message.strip() != ""
        except Exception:
            return False

    def process(self, data: Any) -> str:
        log_type, data_log = data.split(":", 1)
        log_type = log_type.strip()
        data_log = data_log.strip()

        log_levels: Dict[str, str] = {
            "ERROR": "ALERT",
            "INFO": "INFO",
            "WARNING": "WARNING",
        }

        level = log_levels.get(log_type, "UNKNOWN")
        return f"[{level}] {log_type} level detected: {data_log}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    """ Numeric Processor """
    data_num: List[Any] = [1, 2, 3, 4, 5]
    num_p = NumericProcessor()
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data_num}")
    if num_p.validate(data_num):
        print("Validation: Numeric data verified")
        print("Output:", num_p.format_output(num_p.process(data_num)))
    else:
        print("ERROR: The input data is not a valid int!")

    """ Text Processor """
    data_text = "Hello Nexus World"
    text_p = TextProcessor()
    print("\nInitializing Text Processor...")
    print(f"Processing data: \"{data_text}\"")
    if text_p.validate(data_text):
        print("Validation: Text data verified")
        print("Output:", text_p.format_output(text_p.process(data_text)))
    else:
        print("ERROR: The input data is either empty or not a valid str.")

    """ Log Processor """
    data_log = "ERROR: Connection timeout"
    log_p = LogProcessor()
    print("\nInitializing Log Processor...")
    print(f"Processing data: \"{data_log}\"")
    if log_p.validate(data_log):
        print("Validation: Log entry verified")
        print("Output:", log_p.format_output(log_p.process(data_log)))
    else:
        print("ERROR: The input data is either empty, not a valid string, or "
              "does not have a log type at the beginning of the str.")

    """ Polymorphic Demo """
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    data = [[1, 2, 3], "Hello World!", "INFO: System ready"]

    pros = [NumericProcessor(), TextProcessor(), LogProcessor()]

    i = 1
    for d in data:
        for p in pros:
            if p.validate(d):
                print(f"Result {i}: {p.format_output(p.process(d))}")
                i += 1
                break

    print("\nFoundation systems online. Nexus ready for advanced streams.")
