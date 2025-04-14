class Task:
    def __init__(self, name, priority):
        self.name = name 
        self.priority = priority

    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority
        }
    
    @staticmethod
    def from_dict(data):
        return Task(data["name"], data["priority"])
    