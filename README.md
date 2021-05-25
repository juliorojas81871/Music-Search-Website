# NJIT School Assignment
# project1-jcr38 (Milestone 1)

## Requirements
* Python 3.5 or higher to use Flask
* Flask to move data from python to html
* API Access to Spotify and New York Times
* AWS Cloud9 & Git + Github (but these not required but useful) 

## Installation / Create Account
* Spotify Developer Account (API): https://developer.spotify.com/dashboard/login
* New York Times Developer Account (API): https://developer.nytimes.com/accounts/login
* Flask: `pip install flask`

Use this page if you are having problems installing flask in AWS: 
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html

## Libraries Used 
* requests: To request data from Spotify & New York Times
* os: to run the data to the specific port and IP
* random: For the first two versions do you can randomly select an artist.
* Flask & render_template: to collect and move data from python to html
* load_dotenv & find_dotenv: To get the keys required for the API in .env, you will create. 
Also, to prevent people from finding out what they are once you use .gitignore.

## Steps (to get Version 2 working)
1. create a Spotify development account
2. create an app at the dashboard of Spotify development
3. create a .env and add your CLIENT_ID & SECRET you obtain from Spotify when
you create the app (.gitignore is so you can run .env so people won't be able to see your keys)
4. install flask
5. download version 2 codes and run it

## Versions
Version 1 - Use Spotify API to look at three artists and search for
their song, picture, and preview song URL. It will display all the data 
in cmd (this program only use python, .env, & .gitignore)

Version 2 - Create an HTML and CSS to display the data received 
from version 1 on a browser. Also, it will play the
preview music if there is any (this program use flask to 
bring the data from python to HTML, .env, & .gitignor) [this 
program will complete what was required of me in the assignment]

Version 2.5 - From Version 1, I add the New York Times API
to search three articles for one of the artists picked. I also add a 
while loop for the artist's name because there were multiple artists in them 
in some cases. Lastly, this program allows people to choose what artist & song
they want (this program only use python, .env, & .gitignore)

Version 3 - Going off the data from Version 2.5, I modified Version
2 to display the new data. The question & answers still will only be on cmd, though. 
(this program use flask to bring the data from python to HTML, .env, & .gitignore) 
[this program will complete extra credit 1 & 2]

## Questions & Answers
What are at least 3 technical issues you encountered with your project? How did you fix them?

One technical issue I had was the audio in HTML. In the end, I needed someone to tell me that.
I spelled scr instead of src. The second technical issue is that the CSS file wasn't updating. 
In the end, I create another file, change its name, & deleted the old file to get it working again.
Next time I will try `app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0` after `app = Flask(__name__)`.
The last technical issues were that I was getting Response 404 when requesting data from Spotify. 
I need a TA to tell me that I have forgotten `'market': 'US'` in the params.
______________________________________________________________________________________________
What are known problems (still existing), if any, with your project? 

I only can think of one minor issue; it not very big at all. If you look at the song list for
The Weekend only will display the song "After Hours” twice. I do not know how to fix
this. Another problem is when the person pick a number higher than two, it will get
"IndexError: list index out of range" error. I should have used try / except or a while loop 
till they get the right number, but I ran out of time.

______________________________________________________________________________________________
What would you do to improve your project in the future?

One area I would like to improve is asking the questions. In version 3, I did the Q&A in the cmd, 
I want to do it in the HTML next time using Flask & this Youtube video: https://www.youtube.com/watch?v=z8Ewd7z1WpQ. 
The last area is that I will have like to use Twitter next time. I could not attempt this time because, for some reason I 
must get approval first. 


# project1-jcr38 (Milestone 2)

## Requirements
* Python 3.5 or higher to use Flask
* Flask to move data from python to html
* API Access to Spotify, Genius, and New York Times
* AWS Cloud9 & Git + Github (but these not required but useful) 

## Installation / Create Account
* Spotify Developer Account (API): https://developer.spotify.com/dashboard/login
* New York Times Developer Account (API): https://developer.nytimes.com/accounts/login
* Genius (API): https://docs.genius.com/#/getting-started-h1
* Flask: `pip install flask`

Use this page if you are having problems installing flask in AWS: 
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html

## Libraries Used 
* requests: To request data from Spotify & New York Times
* os: to run the data to the specific port and IP
* random: For the first two versions do you can randomly select an artist.
* Flask & render_template: to collect and move data from python to html
* load_dotenv & find_dotenv: To get the keys required for the API in .env, you will create. 
Also, to prevent people from finding out what they are once you use .gitignore.
* re so I can resub the Song name so I the program have a higher chance of dinding the song in
* BeautifulSoup - to get lyric from page

## Steps (to get Version 5 & 6 working)
1. create a Spotify development account
2. create an app at the dashboard of Spotify development
3. create a .env and add your CLIENT_ID & SECRET you obtain from Spotify when
you create the app (.gitignore is so you can run .env so people won't be able to see your keys)
4. get you NYT key (NYT_KEY) and Genius token (GENIUS_ACCESS_TOKEN) (again create and add to .env)
4. install flask
5. download version 5 codes and run it

## Versions
Version 3.5 - just add Genius to a Version 1 

Version 4 - just add genius to the Version 3

Version 5 - Added the an html to allow to ask what artsit they want. Took away the asking the user
what song the want in cmd and switch it to random. Fix the naming so it doesn't name the album 
but the song instead. Lastly, I seperate the three api to seperate files. (was remove to be able to put in 
version 6)

Version 6 - Allow the user to pick their song they want in a seperate html. I also add Spotify
track api so I can get more detail of the song. (Now Version 5)

## Questions & Answers
What are at least 3 technical issues you encountered with your project? How did you fix them?

One technical issue I had that the song name in Spotify wasn't working well when using them 
for Genius. The reason for this is because some of the title have lyrics like '(feate Drake)'
To fix this I resub the song title removing '()' and eveerything in between. The second issue I
had was adding the second html page. I basically have to rework the entire main.py and spotify.py
by adding more def in those files. The last technical issue I had was adding the files into heroku. 
The sad thing it took me 10 minutes and a TA to point out that I misspelled requirements.
______________________________________________________________________________________________
What are known problems (still existing), if any, with your project? 

The only problem I see is that somre of the song title I get from Spotify still doesn't work well 
when searching for the lyric in Genius. The only way I think I can fix this is by reducing the song
allow th user to pick becauase it usually happen at the end. As of right now if I can get a lyric 
the html display the Genius can find any in Version 6. Other than that I think I am good. 
______________________________________________________________________________________________
What would you do to improve your project in the future?

On way I think I can improve open this program is to put the NYT and Genius lyric in their own html. 
The only way I could think this will work if I create more def just for the to api, but than I have 
the problem going back. I also want to add to make nicer looking webpage, because as of right now I 
think it is kindof bland. I am planning to use this website to help me: https://learn.shayhowe.com/advanced-html-css/


