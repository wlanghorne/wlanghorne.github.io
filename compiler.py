import os 
from bs4 import BeautifulSoup

# template files
templates = ['footer.html', 'aside.html', 'header.html']

# list of html files
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.html') and f not in templates]

# gather templates
for template in templates:
	with open(os.path.join('./', template), 'r') as f_template:
		temp_contents = f_template.read()

		soup = ''
		for file in files:
			print(file)
			with open(os.path.join('./', file), 'r') as f_html:
				template_soup = BeautifulSoup(temp_contents, 'html.parser')
				contents = f_html.read()
				soup = BeautifulSoup(contents, 'html.parser')

				element = soup.find(template.replace('.html', ''))
				element.clear()
				element.insert(1,template_soup)
			f_html.close()

			with open(os.path.join('./', file), 'w') as f_html:
				f_html.write(str(soup))
			f_html.close()
	f_template.close()
