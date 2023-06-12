import matplotlib.pyplot as pyl

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = pyl.subplots()
    ax.pie(values, labels=labels)
    pyl.savefig("pie.png")
    pyl.close