class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append([value, timestamp])  # Always append

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        entries = self.dictionary[key]
        left, right = 0, len(entries) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            if entries[mid][1] == timestamp:   # [1] is timestamp
                return entries[mid][0]         # [0] is value
            elif entries[mid][1] > timestamp:
                right = mid - 1
            else:
                result = entries[mid][0]  # Best candidate so far
                left = mid + 1

        return result  # Largest timestamp <= target, or "" if none

