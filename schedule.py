"""
This is the main program
"""
import os
from os import path

import sys
import datetime
import json
import subprocess
import webuntis

CURRENT = os.path.dirname(sys.argv[0])
TODAY = datetime.date.today()
END = TODAY + datetime.timedelta(days=14)

class WrongPasswordError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def addToCalendar(school_input, server_input, untisid_input, username_input, password_input):
    from google_cal import add_event, delete_events
    
    try:
        with webuntis.Session(
            username=username_input,
            password=password_input,
            server=server_input,
            school=school_input,
            useragent='Chrome'
        ).login() as s:
            LESSON_REQ = s.timetable(student=untisid_input, start=TODAY, end=END)
            delete_events()
            for lesson in LESSON_REQ:
                if lesson.code != 'cancelled':
                    lesson.rooms = str(lesson.rooms).replace("[", "")
                    lesson.rooms = str(lesson.rooms).replace("]", "")
                    lesson.subjects = str(lesson.subjects).replace("[", "")
                    lesson.subjects = str(lesson.subjects).replace("]", "")
                    add_event(lesson.start, lesson.end, lesson.subjects, lesson.rooms)
    except webuntis.errors.BadCredentialsError:
        return("Ey da gaatnie goe he!")
