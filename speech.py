def getLanguage(argument):
       switcher={
              1:"en-IN",
              2:"hi-IN"

       }
       return switcher.get(argument,0)
def getSelection():
       while True:
              try:
                     userInput=int(input())
                     if(userInput<1 or userInput>2):
                            print("Not an Integer! try again.")
                            continue
              except ValueError:
                     print("Not an Integer! try again.")
                     continue
              else:
                     return userInput
                     break
def startConvertion(path = 'G:\ezimex\4161_09511811689_2021-Jul-11 11-01-08.WAV',lang = 'en-IN'):
       with sr.AudioFile(path) as source:
              print('Fetching File')
              audio_text = r.listen(source)
              
       
              try:
                print('Converting audio transcripts into text ...')
                text = r.recognize_google(audio_text,language=lang)
                print("Hi i am ankit")
    

              except:
                   print('Sorry.. run again...')
if __name__=='__maim__':
       print('plz select language for translate:')
       print('1.English')
       print('2.Hindi')
       langaugeSelection=getLangauge(getSelection())
       startConvertion('G:\ezimex\4161_09957507023_2021-Jul-11 09-28-09.WAV',languageSelection)

def getLanguage(argument):
       switcher={
              1:"en-IN",
              2:"hi-IN"

       }
       return switcher.get(argument,0)
def getSelection():
       while True:
              try:
                     userInput=int(input())
                     if(userInput<1 or userInput>2):
                            print("Not an Integer! try again.")
                            continue
              except ValueError:
                     print("Not an Integer! try again.")
                     continue
              else:
                     return userInput
                     break
def startConvertion(path = 'G:\ezimex\4161_09957507023_2021-Jul-11 09-28-09.WAV',lang = 'en-IN'):
       with sr.AudioFile(path) as source:
              print('Fetching File')
              audio_text = r.listen(source)
              
       
              try:
                print('Converting audio transcripts into text ...')
                text = r.recognize_google(audio_text,language=lang)
                print("Hi i am ankit")
    

              except:
                   print('Sorry.. run again...')
if __name__=='__maim__':
       print('plz select language for translate:')
       print('1.English')
       print('2.Hindi')
       langaugeSelection=getLangauge(getSelection())
       startConvertion('G:\ezimex\4161_09511811689_2021-Jul-11 11-01-08.WAV',languageSelection)



