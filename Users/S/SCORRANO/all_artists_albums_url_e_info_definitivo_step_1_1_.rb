require 'nokogiri'
require 'open-uri'
require 'date'
require 'yaml'
require 'json'
require 'pp'
require 'uri'
require 'net/http'
require 'scraperwiki/datastore'
require 'httpclient'
require 'scraperwiki/scraper_require'

url = "http://www.allmusic.com/artist/zero-7-mn0000696668"

doc = Nokogiri.HTML(open(url))

rows = doc.search('tbody tr') #nella pagina profilo dell'artista dò alla variabile rows il contenuto di ogni riga della tabella degli album
#puts rows

rows.each do |row| #itero su ogni riga (cioè su ogni album)
  link = row.search('a')[0]
  #puts link

  album = {}
  #album[:album_name] = row.search('a.title.full-title').inner_text #prende il nome dell'album
  #puts album[:name]
  album[:album_url] = "http://www.allmusic.com"+link[:href] #prende l'URL dell'album
  #puts album[:url]
  #album[:artist_url] = url #prende l'URL dell'artista autore dell'album
  #puts album[:artist_URL]
  #album[:year] = row.search('.year').inner_text.strip #prende l'anno di uscita dell'album
  #puts album[:year]
  #album[:label] = row.search('span.full-title').inner_text #prende la casa discografica che ha prodotto l'album
  #puts album[:label]

  ScraperWiki::save_sqlite([:album_url], album, table_name="ONLY_albums_URL", verbose=0) #salva il contenuto estratto per URL degli album (che saranno sempre diversi da artista ad artista), la tabella di salvataggio si chiamerà 'ONLY_albums_URL' e il verbose (cioè il printing nella 'data tab' durante il running è settato a 2, valore di default)
end #ends the .each on the rowsrequire 'nokogiri'
require 'open-uri'
require 'date'
require 'yaml'
require 'json'
require 'pp'
require 'uri'
require 'net/http'
require 'scraperwiki/datastore'
require 'httpclient'
require 'scraperwiki/scraper_require'

url = "http://www.allmusic.com/artist/zero-7-mn0000696668"

doc = Nokogiri.HTML(open(url))

rows = doc.search('tbody tr') #nella pagina profilo dell'artista dò alla variabile rows il contenuto di ogni riga della tabella degli album
#puts rows

rows.each do |row| #itero su ogni riga (cioè su ogni album)
  link = row.search('a')[0]
  #puts link

  album = {}
  #album[:album_name] = row.search('a.title.full-title').inner_text #prende il nome dell'album
  #puts album[:name]
  album[:album_url] = "http://www.allmusic.com"+link[:href] #prende l'URL dell'album
  #puts album[:url]
  #album[:artist_url] = url #prende l'URL dell'artista autore dell'album
  #puts album[:artist_URL]
  #album[:year] = row.search('.year').inner_text.strip #prende l'anno di uscita dell'album
  #puts album[:year]
  #album[:label] = row.search('span.full-title').inner_text #prende la casa discografica che ha prodotto l'album
  #puts album[:label]

  ScraperWiki::save_sqlite([:album_url], album, table_name="ONLY_albums_URL", verbose=0) #salva il contenuto estratto per URL degli album (che saranno sempre diversi da artista ad artista), la tabella di salvataggio si chiamerà 'ONLY_albums_URL' e il verbose (cioè il printing nella 'data tab' durante il running è settato a 2, valore di default)
end #ends the .each on the rows