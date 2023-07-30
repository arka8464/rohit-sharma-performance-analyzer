import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import tabulate
from flask import Flask, render_template
import io
import base64

plt.switch_backend('agg')

odi_data = pd.read_csv('ODI.csv')
t20_data = pd.read_csv('T20.csv')
test_data = pd.read_csv('TEST.csv')
ipl_data = pd.read_csv('IPL.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/Group')
def Group():
    return render_template('Group.html')


@app.route('/scatter')
def scatter():
    return render_template('scatter.html')


@app.route('/line1')
def line1():
    return render_template('line1.html')


@app.route('/line2')
def line2():
    return render_template('line2.html')


@app.route('/line3')
def line3():
    return render_template('line3.html')


@app.route('/line4')
def line4():
    return render_template('line4.html')


@app.route('/boundariesperyear')
def boundariesperyear():
    return render_template('boundariesperyear.html')


@app.route('/FourNSix')
def FourNSix():
    return render_template('FourNSix.html')


@app.route('/strikerate')
def strikerate():
    return render_template('strikerate.html')


@app.route('/avgrunsperyear')
def avgrunsperyear():
    return render_template('avgrunsperyear.html')


@app.route('/dotpercentage')
def dotpercentage():
    return render_template('dotpercentage.html')


@app.route('/centuries')
def centuries():
    return render_template('centuries.html')


@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')


@app.route('/piechart')
def piechart():
    return render_template('piechart.html')

@app.route('/lineplot')
def lineplot():
    # Create a simple plot
    # Define colors to use for each graph
    colors = ["red", "green", "blue", "purple"]

    # Plot a line graph of runs scored over the years for each format
    formats = {"ODI": odi_data, "T20": t20_data,
               "Test": test_data, "IPL": ipl_data}

    for i, (format, df) in enumerate(formats.items()):
        plt.plot(df["Year"], df["Runs"], color=colors[i])
        plt.title("All fromat - Year vs Runs")
        plt.xlabel("Year")
        plt.xticks(rotation=90)
        plt.xticks(np.arange(min(df["Year"]), max(df["Year"])+1, 1.0))
        plt.ylabel("Runs")
        plt.grid(axis='x')
        # x = [1, 2, 3, 4, 5]
        # y = [i**2 for i in x]
        # plt.plot(x, y)

    # Encode the plot in PNG format
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url1 = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return render_template('line.html', plot_url1=plot_url1)


@app.route('/barchart')
def bar_chart():
    centuries = {'ODI': odi_data['100'].sum(), 'T20': t20_data['100'].sum(
    ), 'TEST': test_data['100'].sum(), 'IPL': ipl_data['100'].sum()}
    formats = list(centuries.keys())
    counts = list(centuries.values())
    colors = ['blue', 'green', 'red', 'purple']
    plt.bar(formats, counts, color=colors)
    plt.title('Number of centuries scored by Rohit Sharma in each format')
    plt.xlabel('Format')
    plt.ylabel('Count')
    imgbar = io.BytesIO()
    plt.savefig(imgbar, format='png')
    imgbar.seek(0)
    plot_url2 = base64.b64encode(imgbar.getvalue()).decode()
    plt.close()
    return render_template('bar.html', plot_url2=plot_url2)


if __name__ == '__main__':
    app.run(debug=True)
