import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def get_json(url):
    """Fetch JSON data from an API."""
    request = Request(
        url,
        headers={"User-Agent": "PythonWeatherReport/1.0"}
    )
    with urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def describe_weather(code):
    """Convert Open-Meteo weather codes into readable descriptions."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return descriptions.get(code, "Unknown conditions")


def get_weather(city):
    """Find a city and print its current weather report."""
    # Step 1: Find the city coordinates.
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search?" + urlencode({
        "name": city,
        "count": 5,
        "language": "en",
        "format": "json",
    })
    places = get_json(geocoding_url).get("results", [])

    if not places:
        print(f"\nSorry, I couldn't find '{city}'. Check the spelling and try again.")
        return

    # If several places have the same name, show options.
    if len(places) > 1:
        print("\nI found several matching places:")
        for index, place in enumerate(places, start=1):
            area = place.get("admin1", "")
            country = place.get("country", "")
            details = ", ".join(part for part in [area, country] if part)
            print(f"{index}. {place['name']}" + (f" — {details}" if details else ""))

        choice = input("Enter the number for your city (or press Enter for option 1): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            place = places[int(choice) - 1]
        else:
            place = places[0]
    else:
        place = places[0]

    # Step 2: Get current weather for the selected coordinates.
    weather_url = "https://api.open-meteo.com/v1/forecast?" + urlencode({
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "current": (
            "temperature_2m,relative_humidity_2m,apparent_temperature,"
            "is_day,precipitation,rain,weather_code,wind_speed_10m"
        ),
        "timezone": "auto",
    })
    data = get_json(weather_url)
    current = data.get("current", {})
    units = data.get("current_units", {})

    location_parts = [
        place.get("name", city),
        place.get("admin1", ""),
        place.get("country", ""),
    ]
    location = ", ".join(dict.fromkeys(part for part in location_parts if part))

    print("\n" + "=" * 42)
    print(f"       WEATHER REPORT: {location.upper()}")
    print("=" * 42)
    print(f"Local time       : {current.get('time', 'Not available')}")
    print(f"Condition        : {describe_weather(current.get('weather_code', -1))}")
    print(f"Temperature      : {current.get('temperature_2m', 'N/A')} {units.get('temperature_2m', '°C')}")
    print(f"Feels like       : {current.get('apparent_temperature', 'N/A')} {units.get('apparent_temperature', '°C')}")
    print(f"Humidity         : {current.get('relative_humidity_2m', 'N/A')}{units.get('relative_humidity_2m', '%')}")
    print(f"Wind speed       : {current.get('wind_speed_10m', 'N/A')} {units.get('wind_speed_10m', 'km/h')}")
    print(f"Precipitation    : {current.get('precipitation', 'N/A')} {units.get('precipitation', 'mm')}")
    print(f"Rain             : {current.get('rain', 'N/A')} {units.get('rain', 'mm')}")
    print(f"Day or night     : {'Day' if current.get('is_day') == 1 else 'Night'}")
    print("=" * 42)
    print("Weather data by Open-Meteo: https://open-meteo.com/")


def main():
    print("Welcome to the City Weather Report")
    city = input("Enter a city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    try:
        get_weather(city)
    except HTTPError as error:
        print(f"Weather service returned an HTTP error: {error.code}")
    except URLError:
        print("Could not connect. Please check your internet connection and try again.")
    except TimeoutError:
        print("The request timed out. Please try again.")
    except (KeyError, ValueError, json.JSONDecodeError):
        print("The weather service returned unexpected data. Please try again.")


if __name__ == "__main__":
    main()
