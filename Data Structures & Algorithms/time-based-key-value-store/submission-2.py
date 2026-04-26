class TimeMap:

    def __init__(self):
        timeStore = defaultdict(dict)
        self.timeStore = timeStore

    def set(self, key: str, value: str, timestamp: int) -> None:
        ts = self.timeStore
        ts[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        ts = self.timeStore
        if timestamp in ts[key]:
            return ts[key][timestamp]
        else:
            temp = -1
            for time in ts[key].keys():
                if time < timestamp:
                    temp = time
                else:
                    break
            if temp == -1:
                return ""
            return ts[key][temp]