# -*- coding: utf-8 -*-
from loader import *
from checker import *

players, sports, teams = load_data()
events = load_schedule()
errors = check_events(events)
if len(errors) > 0:
    for error in errors:
        print(error)
    assert False
check_all_playground(sports, events, True)
