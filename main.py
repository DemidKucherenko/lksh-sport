# -*- coding: utf-8 -*-
from loader import *
from checker import *

players, sports, teams = load_data()
events = load_schedule()
check_events(events, True)
