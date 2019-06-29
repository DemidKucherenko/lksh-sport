# -*- coding: utf-8 -*-
from loader import *
from checker import *

players, sports, teams = load_data()
events = check_schedule()
check_events(events, True)
