# Import modules
try:
    import dryscrape
except:
    exit('Unable to import dryscrape.')
try:
    from bs4 import BeautifulSoup
except:
    exit('Unable to import BeautifulSoup from bs4.')

# Lyrics functions
class lyrics:
    def get(artist, title):
        artist = artist.replace(' ', '_')
        title = title.replace(' ', '_')
        session = dryscrape.Session()
        try:
            session.visit('http://lyrics.wikia.com/wiki/' + artist + '%3A' + title)
        except:
            exit('Lyrically - Couldn\'t connect to Wikia')
        page_html = session.body()
        soup = BeautifulSoup(page_html, 'lxml')
        try:
            lyrics_html = soup.findAll('div', {'class' : 'lyricbox'})[0]
        except:
            exit('Lyrically - You can only use lyrics.get once per session.')
        lyrics_html = str(lyrics_html)
        lyrics_html = lyrics_html[22:][:-38]
        lyrics_html = lyrics_html.replace('</div>', '')
        lyrics_html = lyrics_html.replace('<br/>', '\n')
        return(lyrics_html)
