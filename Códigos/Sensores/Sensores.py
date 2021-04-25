import time
import board
import busio
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
import adafruit_lis3mdl
import adafruit_lps2x
 
i2c = busio.I2C(board.SCL, board.SDA)
 
acel_giro = LSM6DS33(i2c)
magnetometro = adafruit_lis3mdl.LIS3MDL(i2c)
barometro = adafruit_lps2x.LPS25(i2c)

while True:
    mag_x, mag_y, mag_z = magnetometro.magnetic
 
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (acel_giro.acceleration))
    print("")
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (acel_giro.gyro))
    print("")
    print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
    print("")
    print("Pressure: %.2f hPa" % barometro.pressure)
    print("")
    time.sleep(0.1)
    