#reading from analog pin
import mraa
import time
#initialize analog pin 
mraa.addSubplatform(mraa.GROVEPI, "0")
temp=mraa.Aio(512)
#configure pin #1 as an input pin                                                
#temp.dir(mraa.DIR_IN)                                      
While 1:
	sensor=temp.read()                              
	voltage=(5000*sensor)/1024
	#temp in degree Celsius
	c=voltage/10
	print(c)
	print("Temperature in degree Celsius is {0}".format(c))
	f=(Celsius*1.8)+32
	print(f)
	print("Temperature in degree Celsius is {0} and temperature in Fahrenheit is{1}".format(c,f))
