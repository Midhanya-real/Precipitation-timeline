class OutputService:
    def __init__(self, data: dict):
        self.data = data

    def __getattr__(self, item):
        return self.data[item]

    def output(self) -> None:
        for key, (date, value) in enumerate(self.data):
            print(f'{key}: {date} - {value}')
