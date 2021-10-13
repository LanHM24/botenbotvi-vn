import speech_recognition
from gtts import gTTS
import os
import playsound
from datetime import date,datetime
import webbrowser as wb

while True:
    # khởi tạo
    ai_brain = " " # Ban đầu nó chưa được học gì cả nên cũng chưa có thông tin
    ai_ear = speech_recognition.Recognizer()# nghe người dùng nói
    you = "" # Lời nói người dùng

    with speech_recognition.Microphone() as mic:
        print("tôi giúp gì được cho bạn")
        audio = ai_ear.record(mic, duration = 5)
        # AI nghe trong vòng 5 giây rồi tắt mic
        print("\nĐợi 1 xí nha ")
    try:
        # Nghe giọng nói của người Việt
        you = ai_ear.recognize_google(audio, language = 'vi-VN')
        if you:
            you = you.lower()  # chuyển văn bản về chữ THƯỜNG
        else:
            you = "Xin chào"
            you = you.lower()  # chuyển văn bản về chữ THƯỜNG

        print("\nLan công chúa:  " + you)
    except:
        # Nếu gặp lỗi thi
        ai_brain = "Tôi không hiểu bạn nói gì cả ! ..."
        print("\nAI:  " + ai_brain)
        continue

    if "Xin chào" in you:
        ai_brain = "Xin chào Bạn."
    elif "thời tiết" in you:
        ai_brain = "Thời tiết hôm nay nè."
        search = "thời tiết"
        url = f"https://google.com/search?q={search}"
        wb.get().open(url)
    elif "ngày" in you:
        today = date.today()
        ai_brain = today.strftime("%d/%m/%Y")
    elif "giờ" in you:
        now = datetime.now()
        ai_brain = now.strftime("%H:%M:%S")
    elif "google" in you:
        ai_brain = " Bạn cần đến google"
        search=you.lower()
        url = f"https://google.com/search?q"
        wb.get().open(url)
    elif "youtube" in you:
        ai_brain = " Bạn cần đến youtube"
        search=you.lower()
        url = f"https://www.youtube.com/"
        wb.get().open(url)    
    elif "facebook" in you:
        ai_brain = " Bạn cần đến facebook"
        search=you.lower()
        url = f"https://www.facebook.com/"
        wb.get().open(url)     
    elif "hẹn gặp lại" in you:
        ai_brain = "Chào tạm biệt và hẹn gặp lại."
        print("\nAI: " + ai_brain)
        exit()
    else:
        ai_brain = "Tôi không nghe rõ. Hãy nhắc lại xem "
        # print("\nAI: " + ai_brain)

    print("\nAI: " + ai_brain)