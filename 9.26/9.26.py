print("輸入民國幾年出生，系統會幫你轉換成西元年")

tmp = input ("輸入Go開始計算:")

def Go():
    number = input("你民國幾年出生:")
    number = int(number)
    print(number + 1911)
    
if tmp == "Go":
    while True:
        Go()



# "="  ->賦值 (另左等於右)  [指派]
# "==" ->比較兩個值是否相同 (比較左是否等於右)
# "while" ->執行後面的動作，直到不滿足條件則會停止動作
# "while true" ->無限迴圈 (因為True永遠滿足條件，所以會一直迴圈)