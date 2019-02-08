#!/usr/bin/env python3.6
import random

class CoinFlip():
	
	def hello():
		print ("Welcome to Coinflip!")
		
	hello()
		
	def cf():
		
		coins = ["Head", "Tale"]
		
		usrinput = input("Head (;)) or Tale?")
	    
		
		randomnumber = 5
		if usrinput == "Head":
			for x in range (random.randint(0,1000)):
				randomnumber = random.randint(0,1)
			print ("Coin:", coins[randomnumber])

		elif usrinput == "Tale":
			for x in range (random.randint(0,1000)):
				randomnumber = random.randint(0,1)
			print ("Coin:",coins[randomnumber])

		else:
			print ("Invalid input!")


	cf()
