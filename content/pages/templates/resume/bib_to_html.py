import collections
import sys
import re

f = open('resume.bib', 'r')

title = ''
journal = ''
year = ''
authors = ''
url = ''

print('<div class="publications">')

for line in f:
  line = line.strip()
  
  matcher = re.search(r'title.+\= \{(.+)\}', line)
  
  if matcher is not None:
    title = matcher.group(1)
    
  matcher = re.search(r'journal.+\= \{(.+)\}', line)
  
  if matcher is not None:
    journal = matcher.group(1)
  
  matcher = re.search(r'year.+\= \{(.+)\}', line)
  
  if matcher is not None:
    year = matcher.group(1)
  
  matcher = re.search(r'author.+\= \{(.+)\}', line)
  
  if matcher is not None:
    authors = '  <div class="pub-authors">{}</div>'.format(matcher.group(1))
    authors = re.sub(r'\\mkbibbold\{(.+)\}', r'<span style="font-weight: 700;">\g<1></span>', authors)
    
  matcher = re.search(r'url.+\= \{(.+)\}', line)
  
  if matcher is not None:
    url = matcher.group(1)
    
  
  if title != '' and journal != '' and year != '' and authors != '':
    print('<div class="pub-article">')
    
    if url != '':
      print('  <div class="pub-title"><a class="pub-title-link" href="{}">{}</a></div>'.format(url, title))
    else:
      print('  <div class="pub-title">{}</div>'.format(title))
      
    print(authors)
    print('  <div class="pub-journal">{}. {}</div>'.format(journal, year))
    
    print('</div>')
    
    title = ''
    journal = ''
    year = ''
    authors = ''
    url = ''

print('</div>')
    
f.close()
