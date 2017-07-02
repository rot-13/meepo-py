#!/usr/bin/env python

import random
import sys
import os
import requests
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pygameui as ui

import logging
log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

LIST_WIDTH = 280
MARGIN = 20
SMALL_MARGIN = 10

class PeopleScene(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        self.lastUpdate = datetime.now()

        scrollbar_size = ui.SCROLLBAR_SIZE

        self.list_view = ui.ListView(ui.Rect(0, 0, LIST_WIDTH, 400),[])
        self.update_people()
        self.list_view.on_selected.connect(self.item_selected)
        self.list_view.on_deselected.connect(self.item_deselected)
        self.scroll_list = ui.ScrollView(ui.Rect(
            MARGIN, MARGIN,
            LIST_WIDTH, 80), self.list_view)
        self.add_child(self.scroll_list)

    def layout(self):
        ui.Scene.layout(self)

    def item_selected(self, list_view, item, index):
        item.state = 'selected'

    def item_deselected(self, list_view, item, index):
        item.state = 'normal'

    def update_people(self):
        r = requests.get("https://meepo-api.herokuapp.com/people")
        items = [];
        for person in r.json()['people']:
            items.append(person['name'])

        label_height = ui.theme.current.label_height
        labels = [ui.Label(ui.Rect(
            0, 0, LIST_WIDTH, label_height), item, halign=ui.LEFT)
            for item in items]
        self.list_view.items = labels

    def update(self, dt):
        ui.Scene.update(self, dt)
        now = datetime.now()
        timediff = now - self.lastUpdate
        if timediff.total_seconds() > 10:
            self.update_people()
            self.lastUpdate = now

if __name__ == '__main__':
    ui.init('pygameui - Rothschild People', (320, 240))
    peopleScene = PeopleScene()
    ui.scene.push(peopleScene)
    ui.run()
