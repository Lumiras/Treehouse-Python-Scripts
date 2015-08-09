#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import sys
import os

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()    #content
    timestamp = DateTimeField(default=datetime.datetime.now)    #timestamp

    class Meta:
        database = db


def initialize():
    """create database"""
    """create table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """show menu"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {})'.format(key,value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    """add entry"""
    print("Enter you entry, press ctrl+d when finished")
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? Y/N ').lower() != 'n':
            Entry.create(content=data)
            print("Saved entry!")

def view_entries(search_query=None):
    """view all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+'='*len(timestamp))
        print('n) next entry')
        print('q) quit to main menu')
        print('d) delete entry')

        next_action = input('Action: [ndq]  ').lower().strip()
        if next_action == 'q':
            break
        if next_action == 'd':
            delete_entry(entry)

def search_entries():
    '''Search entries for a string'''
    view_entries(input('Search query: '))

def delete_entry(entry):
    """delete entry"""
    if input('Are you sure? [yN]').lower() == 'y':
        entry.delete_instance()
        print("Entry deleted!")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
