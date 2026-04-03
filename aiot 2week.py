from gpiozero import Buzzer, DigitalInputDevice    #gpipzero 라이브러리로부터 'Buzzer', 'DigitalInputDevice' 함수를 받아옴

import time                                        #time 라이브러리를 가져옴

bz = Buzzer(18)                                    #GPIO 18번에 연결된 부저를 제어하기 위한 객체생성  
gas = DigitalInputDevice(17)                       #GPIO 17번 핀에 연결된 가스 센서를 입력으로 받기 위한 객체 생성

try:                                               #아래 동작을 계속 반복
    while True:         
        if gas.value == 0:    # ← 0 = 가스 감지 (LOW) 센서값이 0이면  
            print("가스 감지됨")                      #화면에 "가스 감지됨" 출력  
            bz.on()                                #부저가 울림  
        else:                 # ← 1 = 정상 (HIGH)  센서값이 0이 아니면  
            print("정상")                           #화면에 "정상" 출력  
            bz.off()                               #부저 종료  

        time.sleep(0.2)                            #0.2초마다 확인  

except KeyboardInterrupt:                          #Ctrl C를 이용해 프로그램 종료  
    pass

bz.off()                                           #프로그램 종료 시 부저 끔  
