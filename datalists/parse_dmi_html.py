import glob
import bs4
import numpy as np

links = []
filenames = []
html_files = glob.glob('*html')
for html_file in html_files:
    with open(html_file, 'rt') as f:
        s = bs4.BeautifulSoup(f, 'html.parser')
    for a in s.find_all('a'):
        if 'href' in a.attrs and 'https://data.dtu.dk/ndownloader/files'  in a.attrs['href']:
            link = a.attrs['href']
            spans = a.parent.parent.find_all('span')
            for span in spans:
                if len(span.contents) > 0 and ('_dmi_prep' in span.contents[0] or '_cis_prep' in span.contents[0]):
                    filename = span.contents[0]
                    filenames.append(filename)
                    links.append(link)
                    break

linksu, linksui = np.unique(links, return_index=True)
filenamesu = np.array(filenames)[linksui]
i  = np.argsort(filenamesu)
filenamesu, linksu = [list(j[i]) for j in [filenamesu, linksu]]

for year in [2018, 2019, 2020, 2021]:
    with open(f'wget{year}.sh', 'wt') as f:
        for filename, link in zip(filenamesu, linksu):
            if filename.startswith(str(year)):
                f.write(f'wget -nc -nd -O {filename}nc {link}\n')
