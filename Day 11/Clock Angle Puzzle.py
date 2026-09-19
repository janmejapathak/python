hour = int(input("Hour: "))
minute = int(input("Minute: "))

hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)

if angle > 180:
    angle = 360 - angle

print("Angle:", angle)
