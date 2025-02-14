import speech_recognition as sr
import pyttsx3

#Based in CS Coach video in youtube Creating a Speech to Text Program with Python https://www.youtube.com/watch?v=LEDpgye3bf4

# initialize the recognizer
r = sr.Recognizer()

def record_text():
    # loop in case of errors
    while(1):
        try:
            # use the microphone as source for input
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_amazon(audio2,file_key='prueba4',job_name='prueba4',bucket_name="moand4bucket",region="us-east-2", access_key_id="AKIASBGQLFQKKZL7RXPS", secret_access_key="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")

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}",format(e))
        except sr.RequestError as e:
            print("Unknown error ocurred")

    return

def output_text(text):
    f =  open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text= record_text()
    output_text(text)

    print("Wrote text")