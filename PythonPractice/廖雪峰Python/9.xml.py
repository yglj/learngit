from xml.parsers.expat import ParserCreate
from urllib import request
def parseXml(xml_str):
    def start(name,attrs):
        global city 
        if 'city' in attrs:
            city = attrs['city']
            #print('属性:',attrs)
        pass
    def end(name):
        pass
    def data(text):
        if 'city' in text:
            #print('文本:',text)
            pass

    #print(xml_str)
    p = ParserCreate()
    p.StartElementHandler = start
    p.EndElementHandler = end
    p.CharacterDataHandler = data
    p.Parse(xml_str)
    return {
        'city': city,
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
#print(result)
assert result['city'] == 'Beijing'
print('ok')

xml =r'''
<?xml version="1.0" encoding="UTF-8"?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2018-08-19T14:54:45Z" yahoo:lang="en-US"><results><channel><yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="mi" pressure="in" speed="mph" temperature="F"/><title>Yahoo! Weather - Beijing, Beijing, CN</title><link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/</link><description>Yahoo! Weather for Beijing, Beijing, CN</description><language>en-us</language><lastBuildDate>Sun, 19 Aug 2018 10:54 PM CST</lastBuildDate><ttl>60</ttl><yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/><yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="75" direction="20" speed="11"/><yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="86" pressure="1003.0" rising="0" visibility="16.1"/><yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="5:30 am" sunset="7:5 pm"/><image><title>Yahoo! Weather</title><width>142</width><height>18</height><link>http://weather.yahoo.com</link><url>http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif</url></image><item><title>Conditions for Beijing, Beijing, CN at 10:00 PM CST</title><geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">39.90601</geo:lat><geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">116.387909</geo:long><link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/</link><pubDate>Sun, 19 Aug 2018 10:00 PM CST</pubDate><yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="27" date="Sun, 19 Aug 2018 10:00 PM CST" temp="75" text="Mostly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="12" date="19 Aug 2018" day="Sun" high="82" low="71" text="Rain"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="20 Aug 2018" day="Mon" high="90" low="73" text="Mostly Sunny"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="21 Aug 2018" day="Tue" high="92" low="76" text="Partly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="22 Aug 2018" day="Wed" high="87" low="73" text="Mostly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="4" date="23 Aug 2018" day="Thu" high="89" low="70" text="Thunderstorms"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="24 Aug 2018" day="Fri" high="90" low="73" text="Sunny"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="4" date="25 Aug 2018" day="Sat" high="90" low="72" text="Thunderstorms"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="4" date="26 Aug 2018" day="Sun" high="90" low="73" text="Thunderstorms"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="47" date="27 Aug 2018" day="Mon" high="90" low="74" text="Scattered Thunderstorms"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="47" date="28 Aug 2018" day="Tue" high="90" low="75" text="Scattered Thunderstorms"/><description>&lt;![CDATA[&lt;img src="http://l.yimg.com/a/i/us/we/52/27.gif"/&gt;
&lt;BR /&gt;
&lt;b&gt;Current Conditions:&lt;/b&gt;
&lt;BR /&gt;Mostly Cloudy
&lt;BR /&gt;
&lt;BR /&gt;
&lt;b&gt;Forecast:&lt;/b&gt;
&lt;BR /&gt; Sun - Rain. High: 82Low: 71
&lt;BR /&gt; Mon - Mostly Sunny. High: 90Low: 73
&lt;BR /&gt; Tue - Partly Cloudy. High: 92Low: 76
&lt;BR /&gt; Wed - Mostly Cloudy. High: 87Low: 73
&lt;BR /&gt; Thu - Thunderstorms. High: 89Low: 70
&lt;BR /&gt;
&lt;BR /&gt;
&lt;a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/"&gt;Full Forecast at Yahoo! Weather&lt;/a&gt;
&lt;BR /&gt;
&lt;BR /&gt;
&lt;BR /&gt;
]]&gt;</description><guid isPermaLink="false"/></item></channel></results></query><!-- total: 5 -->
'''
