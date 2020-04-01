# Machine learning and NLP applied to the discography of King Krule

**Data: Song titles per album**  
titles_6 Feet Beneath the Moon.txt  
titles_A New Place 2 Drown_titles.txt  
titles_Man Alive!.txt  
titles_TheOoz.txt  

**Code: Scraping**  
*This file scrapes the lyrics of King Krule's albums using as input the titles_\*.txt files. Scraped lyrics are saves in the dataset documents*
Genius_lyrics_api.py	Scraping lyrics

**Data: Lyrics datasets**
*Datasets of all song lyrics per album. All in .txt file, Man_alive album in .json as a result of different scraping techniques applied*  
lyrics_6feet.txt	  
lyrics_A New Place 2 Drown.txt	  
lyrics_Ooz.txt	  
man_alive.json		 

**Code: Word clouds**
*Creation of word clouds per album. First cloud generates word cloud of Krule's first three albums, the second file generates word cloud of his latest album*  
cloud_albums.py  
man_alive_cloud.py	 
