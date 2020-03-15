from flask import Flask, render_template
from data import title, departures, tours, subtitle, description

app = Flask(__name__)

@app.route('/')
def render_index_html():
    tour = []
    for i in range(1, 7):
        tour.append(tours[i])
    return render_template('index.html', title_page=title, nav=departures, sub_title=subtitle, des=description, tour=tour)

@app.route('/departure/<departure>')
def render_departure(departure):
    list_departure = []
    list_tour = []
    for i in tours:
        if tours[i]['departure'] == departure:
            list_departure.append(i)
    for j in list_departure:
        list_tour.append(tours[j])
    temp_price = []
    temp_night = []
    for pn in list_tour:
        temp_price.append(pn['price'])
        temp_night.append(pn['nights'])
    description_content = []
    description_content.append(min(temp_price))
    description_content.append(max(temp_price))
    description_content.append((min(temp_night)))
    description_content.append((max(temp_night)))

    return render_template('departure.html', title_page=title, nav=departures, tour=list_tour, tour_id=list_departure, departure_id=departure, content=description_content)

@app.route('/tour/<id>/')
def render_tour(id):
    return render_template('tour.html', title_page=title, nav=departures, tour=tours[int(id)])

if __name__ == '__main__':
    app.run()
