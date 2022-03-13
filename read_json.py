#!/usr/bin/env python3
# coding: utf-8
#
### Modules import
import json

with open('dvds.json') as json_file:
    data = json.load(json_file)
    for p in data['DVDs']:
        print(' Titre: ' + p['Titre'])
        print(' Genres: ' + p['Genres'])
        print(' Année: ' + p['year'])
        print(' Durée: ' + p['duration'])
        print(' Synopsis: ' + p['Synopsis'])
        print('')
