import requests 

# response = requests.get (
#     url="http://api.open-notify.org/iss-now.json"
#     )
# response.raise_for_status()


# data = response.json()

# longitud = data["iss_position"]["longitude"]
# latitud = data["iss_position"]["latitude"]

# international_space_station_loc = (longitud, latitud)

# print(international_space_station_loc)

""" ---------------------------------------- """

MY_LAT = 25.686613
MY_LONG = -100.316116
formatted = 0

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": formatted,

}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":"))

