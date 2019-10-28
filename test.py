import requests
import dateutil.parser
from twilio.rest import Client
import time

account_sid = ""
auth_token  = ""
client = Client(account_sid, auth_token)

info = []

resp1 = requests.get("https://api.weather.gov/points/42.387647,-71.221412")

data1 = resp1.json()
data2 = data1["properties"]["forecast"]

resp2 = requests.get(data2)

data3 = resp2.json()

print(data3)
prop = data3["properties"]["periods"]
count = 0

for line in prop:
    d = dateutil.parser.parse(line.get("startTime"))
    data4 = d.strftime('%m,%d,%Y,%H,%M,%S').split(",")

    e = dateutil.parser.parse(line.get("endTime"))
    data5 = e.strftime('%m,%d,%Y,%H,%M,%S').split(",")

    date1 = str(data4[0]) + "/" + str(data4[1]) + "/" + str(data4[2])
    print(date1)

    if(int(data4[3])< 12):
        time1 = str(int(data4[3])) + ":00 AM"
        print(time1)
    else:
        time1 = str(int(data4[3])-12) + ":00 PM"
        print(time1)

    date2 = str(data5[0]) + "/" + str(data5[1]) + "/" + str(data5[2])
    print(date2)

    if (int(data5[3]) < 12):
        time2 = str(int(data5[3])) + ":00 AM"
        print(time2)
    else:
        time2 = str(int(data5[3])-12) + ":00 PM"
        print(time2)


    print(line.get("temperature"))
    print(line.get("detailedForecast"))

    time.sleep(1)
    if(count<1):
        message = client.messages.create(to="",from_="",body="\nFrom " + date1 + ": " + time1 + " to " + date2 + ": " + time2 + "\n" + "The temperature in farenheit is " + str(line.get("temperature")))
        message = client.messages.create(to="", from_="", body=str(line.get("detailedForecast")))

    time.sleep(1)

    count+=1


