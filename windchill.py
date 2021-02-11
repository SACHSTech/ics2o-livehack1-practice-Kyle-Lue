temperature = float(input("Enter the temperature in celcius: "))
windspeed = float(input("Enter the windspeed (km/h): "))

# compute windchill
windchill = 13.12 + (0.6215*temperature) - (11.37 * windspeed**0.16) + (0.3965 * temperature* windspeed**0.16)

# output windchill
print("With the windchill factor, it feels like " + str(round(windchill,1)) + "° outside.")

