import speech_recognition as sr #recognise speechpip
import playsound #to play the audio file
from gtts import gTTS #goggle text so speech
import random
from time import ctime # time detials
import webbrowser
import ssl #This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side  and server-side.  This module uses the OpenSSL library
import certifi #Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.
import time
import os #to remove the creted audio the files
from  PIL import Image #The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.
import subprocess #The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
import pyautogui
import pyttsx3
import datetime
import locale
import bs4 as bs #Beautiful Soup is a library that makes it easy to scrape information from web pages. 
import urllib.request #The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
#import wikipedia
class person:
    name='aldi'
    def setName(self,name):
        self.name = name

class asis:
    name='lumine'
    def setName(self,name):
        self.name = name
        
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
       
def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() #initialize a recogniser
#listen for audio and convert to text
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        
        audio =r.listen(source, phrase_time_limit=5)#listen to audio via source
        print("sedang dalam prosess")
        voice_data = ''
        try :
            voice_data= r.recognize_google(audio, language='id-ID')#convert audio to text
            
                 
        except sr.UnknownValueError: #error: reconizer doesn't understand

                engine_speak('maaf, bisa ulangi lagi')
        except sr.RequestError:
                engine_speak("maaf, server kami sedang error")#error : recognizer is not connected
        print(">>", voice_data.lower())#print waht user said
        return voice_data.lower()
            
#get string and make audio file to be played
def engine_speak(audio_string):
    audio_string=str(audio_string) 
    tts = gTTS(text=audio_string , lang='id', slow=False)#text to speech(voice)
    r = random.randint(1,20000000)
    audio_file='audio' + str(r) + '.mp3'
    tts.save(audio_file)#save as mp3
    playsound.playsound(audio_file)#to play the sound
    print(asis_obj.name +":",audio_string)#print what app said
    os.remove(audio_file)#remove the audio file ##let us check at last by comenting it whether it says
    
def respond(voice_data):
    # 1) if got greeting
    if there_exists(['hey','hi','hola','hallo']):
        greetings=["halo ada yang bisa saya bantu?" +person_obj.name, "halo apa yang akan kita lalkukan hari ini?" +person_obj.name, "halo, lumine siap membantu"+person_obj.name]
        greet=greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
        
    #2))name
    if there_exists(["siapa namamu","katakan namamu","kamu siapa"]):
        if person_obj.name:
            engine_speak("ada apa dengan namaku")
        else:
            engine_speak("Saya tidak tahu tuan saya, tolong tetapkan nama saya dengan mengatakan perintah nama kamu harus ,,,, dan tuan akan diberi hak istimewa untuk mengetahui nama Anda ")
            
    if there_exists(["nama kamu harus"]):
        asis_name =voice_data.split("jadi")[-1].strip()
        engine_speak("baikla, saya akan mengingat nama saya"+asis_name)
        asis_obj.setName(asis_name)#remember name in asis object
        
    if there_exists(["nama saya"]):
        person_name = voice_data.split("adalah")[-1].strip()
        engine_speak("aku tau namamu, namamu adalah" + person_name)
        person_name.setName(person_name)#remember name in person object
        
    #3)) greeting
    if there_exists(["apa kabarmu","bagaimana kabarmu","apa yang sedang kamu lakukan"]):
        engine_speak("saya baik baik saja, bagaimana dengan mu? terimakasih sudah bertanya")
        
    #4))time
    if there_exists(["waktu","jam","jam berapa"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0]=="00":
            hours='12'
        else:
            hours = time[0]
        minutes = time[1]
        time = "sekarang jam"+ hours + "lebih" + minutes + "menit"
        engine_speak(time)
    
    if there_exists(["hari apa", "hari",]):
        locale.setlocale(locale.LC_ALL,'id_id')
        day = datetime.datetime.now().strftime('%A')
        time = "hari ini hari"+ day 
        engine_speak(day)

    if there_exists(["bulan apa", "tanggal","tahun"]):
        locale.setlocale(locale.LC_ALL,'id_id')
        date = datetime.datetime.now().strftime(':%A'+" bulan "+':%B'+" tanggal "+':%d'+" tahun "+':%Y')
        date = "sekarang hari "+ date 
        engine_speak(date)

    #5))search google
    if there_exists(["cari"]) and 'youtube' not in voice_data:
        search_term=voice_data.split("untuk")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("saya menemukan "+search_term + "di google")
        
    #6))) search youtube
    if there_exists(["cari di youtube","youtube"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.youtube.com/results?search_query="+ search_term
        webbrowser.get().open(url)
        engine_speak("saya menemukan "+ search_term + "di youtube")
    
    if there_exists(["lokasi","tempat saat ini"]):
        search = record_audio('katakan nama tempat atau jalan')
        url = 'https://www.google.co.id/maps/place/' + search +'/&amp'
        webbrowser.get().open(url)
        engine_speak('ini hasil pencarian '+ search)
        
    # #7)) time table
    # if there_exists(["show me my time table"]):
    #     im = Image.open(r"")
    #     im.show()
        
    #8))) get to know the weather
    if there_exists(["cuaca","keadaan cuaca saat ini","berikan laporan cuaca"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)#opens the webrowser
        engine_speak("ini laporan cuaca hari ini")
    
    #9)) get to know stock price
    if there_exists(["harga"]):
        search_term=voice_data.split("untuk")[-1]
        url="https://google.com/search?q="+ search_term
        webbrowser.get().open(url)
        engine_speak("menampilkan hasil pencarian"+ search_term)
    
    #10 get to listen music
    if there_exists(["musik","lagu"]):
        search_term=voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("nikmati lagumu")
    
    #11 screenshot
    if there_exists(["capture","screenshot"]):
        myScreenshot=pyautogui.screenshot()
        myScreenshot.save('')#kasih patch file simpan screenshot
        
    #4)) search wikipedia for defination
    
    if there_exists(["definisi","pengertian","penjelasan"]):
        definition=record_audio("apa yang ingin kamu ketahui?")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.txt))
        if definitions:
            if definitions[0]:#if condi is false
                engine_speak('maaf saya tidak mengerti apa yang anda cari, anda bisa mencoba mencari di google sebagai gantinya')
            elif definitions[1]:#if condition is true
                engine_speak('menampilkan hasil pencarian'+ definitions[1])
            # else:
            # engine_speak('Here is what i found '+ definitions[2])
        else:
            engine_speak('tidak bisa menemukan'+definitions +'mungkin karena server sedang sibuk')

    #10 stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("pilih batu, kertas, atau gunting")
        moves=["batu", "kertas", "gunting"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("lumine memilih" + cmove)
        engine_speak("kamu memilih " + pmove)
        #engine_speak("hi")


        if pmove==cmove:
            engine_speak("seri")
        elif pmove== "batu" and cmove== "gunting":
            engine_speak("kamu menang")
        elif pmove== "batu" and cmove== "kertas":
            engine_speak("lumine menang")
        elif pmove== "kertas" and cmove== "batu":
            engine_speak("kamu menang")
        elif pmove== "kertas" and cmove== "gunting":
            engine_speak("lumine menang")
        elif pmove== "gunting" and cmove== "kertas":
            engine_speak("kamu menang")
        elif pmove== "gunting" and cmove== "batu":
            engine_speak("lumine menang")

    #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["kepala", "ekor"]   
        cmove=random.choice(moves)
        engine_speak("komputer memilih " + cmove)

    #12 calc
    if there_exists(["tambah","kurangi","kali","bagi","pangkat","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("operator salah")
    # for exit       
    if there_exists(["keluar","sampai jumpa","udahan","udah","sudah"]):
        engine_speak("terimakasih, sampai jumpa kembali")
        exit()
        
        
time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'lumine'
engine = pyttsx3.init()



while(1):
    voice_data = record_audio("katakan sesuatu") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
