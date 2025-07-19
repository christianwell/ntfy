import requests # type: ignore # gører så jeg kan send ting til ntfy.sh
import feedparser # gører så jeg kan læse rss feeds

linkvejr = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=59.3294&longitude=18.0687"
    "&daily=weather_code,temperature_2m_max,temperature_2m_min,"
    "apparent_temperature_max,apparent_temperature_min"
    "&hourly=temperature_2m"
    "&current=temperature_2m,weather_code,apparent_temperature"
    "&forecast_days=11"
)

response = requests.get(linkvejr)
data = response.json()

# RIGTIG adgang til current data
nuvejr = data["current"]["temperature_2m"]
d = feedparser.parse("https://www.dr.dk/nyheder/service/feeds/senestenyt")
entry = d["entries"][0]
nyhed1 = entry["title"]
linknyhed = entry["link"]
kanye = requests.get("https://api.kanye.rest/").json()["quote"]
ntfy = "https://ntfy.sh/test101020"  # dit nfty topic

text = f'dagens sidste nyt er: ✏️ {nyhed1} ({linknyhed})\nKanye quote af i dag: "{kanye} " idags vejr er {nuvejr}°C. Husk at tage tøj på efter vejret! ☀️🌧️"'

requests.post(ntfy,data=text.encode('utf-8'),headers={"Title": "Godmorgen", "Priority": "high", "Tags": "morng"})

