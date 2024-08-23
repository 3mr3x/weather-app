import requests

API_KEY = 'XXXXXXXXX'

def fetch_weather_data( city ):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}&units=metric"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data['cod'] == 200:   
        main_data = weather_data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_description = weather_data['weather'][0]['description']

        print(f"Sıcaklık: {temperature:.2f}°C")
        print(f"Nem: {humidity}%")
        print(f"Hava durumu açıklaması: {weather_description.capitalize()}")
    else:   
        print("Şehir bulunamadı. Lütfen tekrar deneyin.")

def main():
    while True:
        parameters = input("Şehrin adını girin (veya çıkmak için 'exit' yazın): ")
        if parameters.lower() == 'exit':
            print("Program Sonlandı.")
            break
        weather_data = fetch_weather_data(parameters)
        display_weather_data(weather_data)

if __name__ == "__main__":
    main()