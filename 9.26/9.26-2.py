print("將聽力成績及閱讀成績相加以算出你的多益成績是否達到藍色證書標準")

tmp = input("請輸入go來執行:")

def go():
    tmp1 = int(input("請輸入聽力成績:"))
    if tmp1 > 495 or tmp1 < 5:
        print("你的成績有誤")
        return
    tmp2 = int(input("請輸入閱讀成績:"))
    if tmp2 > 495 or tmp2 < 5:
        print("你的成績有誤")
        return
    sum = tmp1 + tmp2
    if sum >= 730 and sum <= 855:
        print("恭喜你拿到藍色證書")
    else:
        print("你的成績不夠拿到藍色證書，或你的成績已符合金色證書的標準")

if tmp == "go":
    go()

