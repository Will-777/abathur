"""

test

"""

try :
    import pyttsx3

except ModuleNotFoundError:
    print('We have a situation here !\n' +\
          'Library pyttsx3 is missing. try ton install \n' +\
          'with <pip install pyttsx3> ')
    ModError = True

else:
    print('Import successsful')
    ModError = False
    

"""
except ImportError:
    raise ImportError('Library pyttsx3 is missing. try ton install ' +\
          'with <pip install pyttsx3> ')
"""


def runMe():
    if ModError == True:
        return
    
    else:
        yourName = input("What's your name ? ")
        engine = pyttsx3.init()

        #engine.setProperty('voice', voices[1].id)
        voices = engine.getProperty('voices')

        for voice in voices:
            print(voice, voice.id)
            engine.setProperty('voice', voice.id)

            engine.say('Good morning ' + yourName + '-san.')
            engine.runAndWait()
            engine.say('じゃ、またね！')
            engine.say('ja ma ta ne.')
            engine.runAndWait()



