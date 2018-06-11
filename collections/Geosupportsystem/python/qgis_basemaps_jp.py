"""
This script should be run from the Python consol inside QGIS.

It adds online sources to the QGIS Browser.
Each source should contain a list with the folowing items (string type):
[sourcetype, title, authconfig, password, referer, url, username, zmax, zmin]

You can add or remove sources from the sources section of the code.

Script by Klas Karlsson
Sources from https://qms.nextgis.com/

Licence GPL-3

change any source by Yfuruchin / MIERUNE

日本語環境で実行する場合は、C:_tempなどに保存後
QGIS3のPythonコンソールで
exec(open('C:\_temp/qgis_basemaps_jp.py',encoding='utf-8').read())
を実行する

"""


# Sources
sources = []
sources.append(["connections-xyz","MIERUNE_Color", "", "", "Maptiles by MIERUNE, under CC BY. Data by OpenStreetMap contributors, under ODbL.","https://tile.mierune.co.jp/mierune/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["connections-xyz","MIERUNE_BW", "", "", "Maptiles by MIERUNE, under CC BY. Data by OpenStreetMap contributors, under ODbL.","https://tile.mierune.co.jp/mierune_mono/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["connections-xyz","OpenStreetMap", "", "", "OpenStreetMap contributors","http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","日本CS立体図（5mメッシュあり）", "", "", "国土地理院（承認番号　平29情使、第77号）","http://kouapp.main.jp/csmap/tile/japan/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "15", "5"])
sources.append(["connections-xyz","北海道CS立体図(10mメッシュのみ）", "", "", "国土地理院（承認番号　平28情使、第830号）","http://kouapp.main.jp/csmap/tile/hokkaido/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "15", "7"])
sources.append(["connections-xyz","九州沖縄CS立体図（10mメッシュのみ）", "", "", "国土地理院（承認番号　平28情使、第912号）","http://kouapp.main.jp/csmap/tile/kyuoki/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "15", "7"])
sources.append(["connections-xyz","地理院標準地図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/std/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "18", "2"])
sources.append(["connections-xyz","地理院淡色地図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/pale/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "18", "12"])
sources.append(["connections-xyz","地理院白地図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/blank/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "14", "5"])
sources.append(["connections-xyz","地理院English", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/english/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "11", "5"])
sources.append(["connections-xyz","地理院色別標高図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/relief/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "5"])
sources.append(["connections-xyz","地理院写真", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/ort/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "18", "2"])
sources.append(["connections-xyz","国土画像情報（第一期：1974～1978年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo1/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "10"])
sources.append(["connections-xyz","国土画像情報（第二期：1979～1983年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo2/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "15"])
sources.append(["connections-xyz","国土画像情報（第三期：1984～1986年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo3/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "15"])
sources.append(["connections-xyz","国土画像情報（第四期：1988～1990年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo4/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "15"])
sources.append(["connections-xyz","空中写真（1961～1964年）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/ort_old10/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])
sources.append(["connections-xyz","空中写真（1945～1950年）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/ort_USA10/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])
sources.append(["connections-xyz","簡易空中写真（2004年～）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/airphoto/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "18", "5"])
sources.append(["connections-xyz","数値地図5000（土地利用）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/lum4bl_capital2005/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])
sources.append(["connections-xyz","土地利用図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/lum200k/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])

# Add sources to browser
for source in sources:
   connectionType = source[0]
   connectionName = source[1]
   QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
   QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
   QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
   QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
   QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
   QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
   QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])

# Update GUI
iface.reloadConnections()
