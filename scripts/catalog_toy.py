import cgi
import os
import sys
import xml.etree.ElementTree as et

HTML_PAGE = """
<html>
<title>Каталог ігрушок</title>
<body>
<h3>Додавання ігрушок</h3>
<br>
<form method="POST" action="/{}">
	<table>
		<tr>
			<td align=right>
				<font size="5" color="blue">
					Введіть назву іграшки
				</font>
			</td>
			<td>
				<input type="text" name="name_toy" value="">
			</td>
		</tr>
		<tr>
			<td align=right>
				<font size="5" color="blue">
					Введіть ціну
				</font>
			</td>
			<td>
				<input type="text" name="price_toy" value="">
			</td>
		</tr>
		<tr>
			<td align=right>
				<font size="5" color="blue">
					Введіть вік дитини
				</font>
			</td>
			<td>
				<input type="text" name="vik_toy" value="">
			</td>
		</tr>
		<tr>
		        <td><input type="submit" name="" value="Добавити"></td>
		</tr>
	</table>
</form>
<br>
</body>
</html>
"""

HTML_PAGE_PRINT = """
<html>
<title>Каталог ігрушок</title>
<body>
<h3>Підбір іграшок</h3>
<br>
<form method="POST" action="/{}">
	<table>		
		<tr>
			<td align=right>
				<font size="5" color="blue">
					Введіть максимальну ціну
				</font>
			</td>
			<td>
				<input type="text" name="price_toy" value="">
			</td>
		</tr>
		<tr>
			<td align=right>
				<font size="5" color="blue">
					Введіть вік дитини
				</font>
			</td>
			<td>
				<input type="text" name="vik_toy" value="">
			</td>
		</tr>
		<tr>
		        <td><input type="submit" name="" value="Підібрати"></td>
		</tr>
	</table>
</form>
<br>
</body>
</html>
"""

def add_toy(n,p,v):
        #root=et.Element("toys")
        #toys=et.ElementTree(root)
        toys = et.parse("toys.xml")
        root = toys.getroot()

        toy = et.Element("toy")        
        toy.set("price", p)
        toy.set("vik", v)
        toy.text = n

        root.append(toy)

        toys.write("toys.xml", encoding="utf-8")        
        

def filtr_toy(p,v):
        
        toys = et.parse("toys.xml")
        root = toys.getroot()

        f_root=et.Element("toys")
        f_toys=et.ElementTree(root)                
        
        # знайти всі вузли "toy"
        for t in toys.iterfind('toy'):
                print (t.get("price"),t.get("vik"))
                if int(t.get("price"))<=int(p) and int(t.get("vik"))>=int(v):
                    f_toys.append(t)   
                        
        print (f_toys)
        return f_toys


def application(environ, start_response):
        command=environ.get("PATH_INFO", "").lstrip("/")
        if command in {"add", "print"}:
                form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
                if command=="add":
                        if 'name_toy' in form:
                                nameT=form['name_toy'].value
                                priceT=form['price_toy'].value
                                vikT=form['vik_toy'].value
                                Toys=add_toy(nameT, priceT, vikT)                                
                                body=HTML_PAGE.format(command)
                                start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
                        else:
                                body=HTML_PAGE.format(command)
                                start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
                else:
                        if 'price_toy' in form:
                                priceT=form['price_toy'].value
                                vikT=form['vik_toy'].value
                                Toys=filtr_toy(priceT,vikT)                                
                                root = Toys.getroot()
                                body=et.tostring(root, encoding="utf-8").decode("utf-8")
                                start_response("200 OK", [("Content-Type","application/xml; charset=utf-8")])
                        else:
                                body=HTML_PAGE_PRINT.format(command)
                                start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
        else:
                start_response("404 NOT FOUND", [("Content-Type", "text/plain")])
                body="Сторінку не знайдено"
        return [bytes(body, encoding='utf-8')]

if __name__ == '__main__':
    # створити та запуститити WSGI-сервер
    from wsgiref.simple_server import make_server
    print('=== Local WSGI webserver ===')
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()
