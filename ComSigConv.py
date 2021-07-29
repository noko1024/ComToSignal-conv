import os, sys, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()

fTyp = [("","*.txt")]

iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('信号命令コンバーター','命令ファイルを選択してください。')
filePath = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
print(filePath)

filename = "bitCommand"
#最終出力用
bitCommand = []

if filePath == "":
    tkinter.messagebox.showerror('信号命令コンバーター',"ファイルが指定されませんでした。")
    sys.exit()

#命令ファイルを展開
with open(filePath,encoding='utf-8') as f:
    signalCommand = f.read().splitlines()

#行ごとにリスト化
sigLine = [x.split() for x in signalCommand]

def LightConv():
    i = 0
    #単語ごとに取り出し、構文解析
    for sigToken in sigLine:

        #変換後単語管理用
        bitToken = ""
        #角度指示Flag
        roteFlag = False
        #停止指示Flag
        stopFlag = False

        #命令要素が2つ以外の時はスキップ
        if not len(sigToken) == 2:
            bitLine = "[###] {}\n".format("#ERROR#")
            bitCommand.append(bitLine)
            continue

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
            stopFlag = True


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

    #EOFを追加
    bitLine = "[{}] {}\n".format(str(i).zfill(3),"●● ●● ●●●●")
    bitCommand.append(bitLine)


def BinConv():
    i = 0
    #単語ごとに取り出し、構文解析
    for sigToken in sigLine:

        #変換後単語管理用
        bitToken = ""
        #角度指示Flag
        roteFlag = False
        #停止指示Flag
        stopFlag = False

        #命令要素が2つ以外の時はスキップ
        if not len(sigToken) == 2:
            bitLine = "###:{}\n".format("#ERROR#")
            bitCommand.append(bitLine)
            continue

        #構文解析
        if sigToken[0] == "前進":
            bitToken = "b0101 "
    
        elif sigToken[0] == "後退":
            bitToken = "b1010 "

        elif sigToken[0] == "右回転":
            roteFlag = True
            bitToken = "b0110 "
    
        elif sigToken[0] == "左回転":
            roteFlag = True
            bitToken = "b1001 "
    
        elif sigToken[0] == "右前進旋回":
            roteFlag = True
            bitToken = "b0100 "
    
        elif sigToken[0] == "右後退旋回":
            roteFlag = True
            bitToken = "b1000 "
    
        elif sigToken[0] == "左前進旋回":
            roteFlag = True
            bitToken = "b0001 "
    
        elif sigToken[0] == "左後退旋回":
            roteFlag = True
            bitToken = "b0010 "
    
        elif sigToken[0] == "停止":
            bitToken = "b0000 "
            stopFlag = True


        if roteFlag == True:
            #角度情報をビット命令へ変換

            angleData = int(float(sigToken[1])/7.5)
            angle = bin(angleData).lstrip("0b").zfill(4)
            bitToken+=angle

        elif stopFlag == True:
            #時間情報をビット命令へ変換
            timeData = int(float(sigToken[1])/0.25)
            time = bin(timeData).lstrip("0b").zfill(4)
            bitToken+=time
    
        else:
            #距離情報をビット命令へ変換
            distanceData = int(sigToken[1])
            distance = bin(distanceData).lstrip("0b").zfill(4)
            bitToken+=distance
    
        #出力向けに成形
        bitLine = "{}:{}\n".format(str(i).zfill(3),bitToken)
        bitCommand.append(bitLine)
        i+=1
        print(bitCommand)

    #EOFを追加
    bitLine = "{}:{}\n".format(str(i).zfill(3),"b1111 1111")
    bitCommand.append(bitLine)


#命令形式を選択
order = tkinter.messagebox.askyesno('信号命令コンバーター','出力する命令形式を選択してください。\n信号式命令を出力したい方は「はい」\nバイナリ式命令を出力したい方は「いいえ」\nを選択して下さい。')
print(order)
if order == True:
    #信号式が選択されたとき
    LightConv()

elif order == False:
    #バイナリ式が選択されたとき
    filename = "binOrder"
    BinConv()

else:
    tkinter.messagebox.showerror('信号命令コンバーター',"命令形式が指定されませんでした。")
    sys.exit()


#ファイル出力
with open(os.path.dirname(filePath)+"/"+filename+".txt",'w', encoding='utf-8') as f:

    f.writelines(bitCommand)

tkinter.messagebox.showinfo('信号命令コンバーター','出力しました。')