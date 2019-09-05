#!/usr/bin/python

#BMI - Body Mass Index
#BMI = (weight in kg / height in meters squared)
#Imperial version: BMI * 703

def gather_info():
	height = float(input("What is your height? (inches or meters) "))
	weight = float(input("What is your weight? (pounds or kilograms) "))
	system = input("Are your measurements in metric ot imperial units? ").lower().strip()
	return (height, weight, system)

	sef calculate_bmi(weight, height, system='metric'):

		"""
		Return the Body Mass Index (BMI) for
		given weight, height and measurement system
		"""

	if system == 'metric':
		bmi = (weight / (height **2))
	else:
		bmi = 703 * (weight /(height ** 2))
	return bmi

while True:
	
