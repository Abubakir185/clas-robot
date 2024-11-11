class Robot:
    def __init__(self, name, x, y, yonalishi):
        self.name = name
        self.x = x
        self.y = y
        self.yonalish = yonalishi

    def yurish(self, qadam):
        if self.yonalish == "tepaga":
            self.y += qadam
        elif self.yonalish == "pastga":
            self.y -= qadam
        elif self.yonalish == "chapga":
            self.x -= qadam
        elif self.yonalish == "onga":
            self.x += qadam
        
    def yonalishni_ozgartirish(self, yangi_yonalish):
        self.yonalish = yangi_yonalish

    def robotning_koordinatasi(self):
        print(f"X: {self.x} Y: {self.y}")




tony = Robot("Tony", 0, 0, "onga")

tony.yurish(5)
tony.yonalishni_ozgartirish("pastga")
tony.yurish(5)
tony.robotning_koordinatasi()

