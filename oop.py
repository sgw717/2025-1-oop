class Car :
    color =""
    speed = 0
    MaxSpeed = 150

    def upSpeed(self,value) :
        self.speed += value
        if self.speed > Car.MaxSpeed :
            self.speed = Car.MaxSpeed

    
    def downSpeed(self,value) :
        self.speed -= value

myCar1 = Car()
myCar1.color = "Red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "Blue"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "Yellow"
myCar3.speed = 0

myCar1.upSpeed(200)
print("자동차1의 색깔은 %s이며, 현재 속도는 %d km입니다." %(myCar1.color , myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색깔은 %s이며, 현재 속도는 %d km입니다." %(myCar2.color , myCar2.speed))

myCar3.upSpeed(90)
print("자동차3의 색깔은 %s이며, 현재 속도는 %d km입니다." %(myCar3.color , myCar3.speed))