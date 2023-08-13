class PmType:
    def __init__(self, name, weakTo, resists, immuneTo):
        self.name = name
        self.weakTo = weakTo
        self.resists = resists
        self.immuneTo = immuneTo

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return {"name": {self.name},
                "weakTo": {self.weakTo},
                "resists": {self.resists},
                "immuneTo": {self.immuneTo}}