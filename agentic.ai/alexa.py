
import requests
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    try:
        # Find city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo = requests.get(
            geo_url,
            params={"name": city, "count": 1, "language": "en"},
            timeout=15
        )
        geo.raise_for_status()
        places = geo.json().get("results", [])

        if not places:
            speak("Sorry, I could not find that city.")
            return

        place = places[0]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        response = requests.get(
            weather_url,
            params={
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": (
                    "temperature_2m,relative_humidity_2m,"
                    "apparent_temperature,wind_speed_10m,weather_code"
                ),
                "timezone": "auto"
            },
            timeout=15
        )
        response.raise_for_status()
        current = response.json()["current"]

        conditions = {
            0: "clear sky",
            1: "mainly clear",
            2: "partly cloudy",
            3: "overcast",
            45: "foggy",
            51: "light drizzle",
            61: "light rain",
            63: "moderate rain",
            65: "heavy rain",
            71: "snow",
            80: "rain showers",
            95: "thunderstorm"
        }

        condition = conditions.get(
            current["weather_code"], "variable conditions"
        )

        report = (
            f"Weather report for {place['name']}, {place.get('country', '')}. "
            f"The temperature is {current['temperature_2m']} degrees Celsius. "
            f"It feels like {current['apparent_temperature']} degrees. "
            f"Conditions are {condition}. "
            f"Humidity is {current['relative_humidity_2m']} percent. "
            f"Wind speed is {current['wind_speed_10m']} kilometers per hour."
        )

        speak(report)

    except requests.RequestException:
        speak("I cannot connect to the weather service. Please check your internet.")

def main():
    speak("Hello! I am your Alexa-style weather assistant.")

    while True:
        print("\n1. Enter city name")
        print("2. Speak city name")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()
            if city:
                get_weather(city)
            else:
                speak("Please enter a city name.")

        elif choice == "2":
            recognizer = sr.Recognizer()

            try:
                with sr.Microphone() as source:
                    speak("Please say the city name.")
                    recognizer.adjust_for_ambient_noise(
                        source, duration=0.5
                    )
                    audio = recognizer.listen(
                        source, timeout=5, phrase_time_limit=5
                    )

                city = recognizer.recognize_google(audio)
                print("You said:", city)
                get_weather(city)

            except sr.UnknownValueError:
                speak("Sorry, I could not understand you.")
            except sr.RequestError:
                speak("Voice recognition service is unavailable.")
            except (OSError, sr.WaitTimeoutError):
                speak("Microphone unavailable or no speech detected.")

        elif choice == "3":
            speak("Goodbye!")
            break

        else:
            speak("Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
