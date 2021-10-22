import csv
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json("WB-JSON-8.json")
print(df)
df.to_csv("db.csv", index=False)


with open('db.csv', newline='') as File:
    reader = csv.reader(File)
    motion = []
    temperature = []
    voltage = []
    a, b, c = 0, 0, 0
    for m in reader:
        if m[1] != 'motion':
            motion.append(float(m[1]))
            a += 1
        if m[0] != 'temperature':
            temperature.append(float(m[0]))
            b += 1
        if m[2] != 'voltage':
            voltage.append(float(m[2]))
            c += 1

    min = []
    max = []
    for i in voltage:
        min.append(i) if i <=7.5 else max.append(i)

    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,1,2)
    ax1.set(title='motion')
    ax2.set(title='temperature')
    ax3.set(title='voltage')

    # Столбиковая диаграмма (гистограмма) движения
    ax1.bar(list(range(0, a)), motion)

    #Линейный график температуры
    ax2.plot(list(range(0, b)), temperature)

    #Круговая диаграмма (напряжение)
    ax3.pie([len(min), len(max)])
    labels = ['<=7.5', '>7.5']
    ax3.legend(labels, loc = 'lower right', fontsize=7)

    plt.show()