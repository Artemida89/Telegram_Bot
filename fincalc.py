# ввод своих фин остатков
y = ["Январе", "Феврале", "Марте", "Апреле", "Мае", "Июне", "Июле", "Августе", "Сентябре", "Октябре", "Ноябре",
     "Декабре"]

namber = 0
x = 1

nal_Y = int(input("Ввидите полалуйста '1' если у вас есть наличка. А если нету введите '2'\n"))

if nal_Y == 1:
    nal = input("Введите пожалуйста сколько у вас налички \n")
    b_nal = input("Введите пожалуйста сколько у вас карточки \n")
    while x != 13:
        nal: float = float(nal)
        b_nal = float(b_nal)
        nal = nal + 2000
        b_nal = b_nal + b_nal * 0.2
        nal = str(nal)
        b_nal = str(b_nal)
        x = str(x)
        print("У вас в " + y[namber] + " будет: \n Налички:" + nal + "\n На карточке:" + b_nal)
        x = int(x)
        x = x + 1
        namber = namber + 1
else:
    print("Идем верным путем")