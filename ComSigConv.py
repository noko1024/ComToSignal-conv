import os, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()

fTyp = [("","*.txt")]

iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('信号命令コンバーター','命令ファイルを選択してください。')
filePath = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

#最終出力用
bitCommand = []

#命令ファイルを展開
with open(filePath,encoding='utf-8') as f:
    signalCommand = f.read().splitlines()

#行ごとにリスト化
sigLine = [x.split() for x in signalCommand]

i = 0
#単語ごとに取り出し、構文解析
for sigToken in sigLine:

    #変換後単語管理用
    bitToken = ""
    #角度指示Flag
    roteFlag = False
    #停止指示Flag
    stopFlag = False
    

    #構文解析
    if sigToken[0] == "前進":
        bitToken = "○● ○● "
    
    elif sigToken[0] == "後退":
        bitToken = "●○ ●○ "

    elif sigToken[0] == "右回転":
        roteFlag = True
        bitToken = "○● ●○ "
    
    elif sigToken[0] == "左回転":
        roteFlag = True
        bitToken = "●○ ○● "
    
    elif sigToken[0] == "右前進旋回":
        roteFlag = True
        bitToken = "○● ○○ "
    
    elif sigToken[0] == "右後退旋回":
        roteFlag = True
        bitToken = "●○ ○○ "
    
    elif sigToken[0] == "左前進旋回":
        roteFlag = True
        bitToken = "○○ ○● "
    
    elif sigToken[0] == "左後退旋回":
        roteFlag = True
        bitToken = "○○ ●○ "
    
    elif sigToken[0] == "停止":
        bitToken = "○○ ○○ "


    if roteFlag == True:
        #角度情報をビット命令へ変換

        angleData = int(float(sigToken[1])/7.5)
        angle = bin(angleData).lstrip("0b").zfill(4).replace("0","○").replace("1","●")
        bitToken+=angle

    elif stopFlag == True:
        #時間情報をビット命令へ変換
        timeData = int(float(sigToken[1])/0.25)
        time = bin(timeData).lstrip("0b").zfill(4).replace("0","○").replace("1","●")
        bitToken+=time
    
    else:
        #距離情報をビット命令へ変換
        distanceData = int(sigToken[1])
        distance = bin(distanceData).lstrip("0b").zfill(4).replace("0","○").replace("1","●")
        bitToken+=distance
    
    #出力向けに成形
    bitLine = "[{}] {}\n".format(str(i).zfill(3),bitToken)
    bitCommand.append(bitLine)
    i+=1

#ファイル出力
with open(iDir+"/bitCommand.txt",'w', encoding='utf-8') as f:

    f.writelines(bitCommand)

tkinter.messagebox.showinfo('信号命令コンバーター','出力しました。')