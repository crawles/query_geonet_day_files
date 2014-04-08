sta_chans = open('geonet-sta-chan.txt')

queries = []
for row in sta_chans:
    col = row.split()
    sta = col[0]
    chan = col[1]
    query = 'java -jar code/GeoNetCWBQuery-4.2.0-bin.jar -b "2009/07/15 00:00:00" -s "NZ'+sta+".."+chan+'.." -d 100 -t ms -o %z%y%M%D%h%m.%y-%j.%s.%c.%l.%n.ms'
    queries.append(query)
    print query

