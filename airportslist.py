#ambil airport list dan dimasukkan ke file excel baru


from FlightRadar24.api import FlightRadar24API
import pandas as pd
fr_api = FlightRadar24API()

#bagian dibawah ini ganti saja dengan apa yang ingin dicari: airport, airline, flight, zones
airports = fr_api.get_airports()


#data ditaruh di file excel
selesai = pd.DataFrame(airports)
selesai.to_excel("output.xlsx")
