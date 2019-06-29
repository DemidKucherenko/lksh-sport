from event import *


def check_two_events(event1, event2, error_level):
    if not is_intersecting(event1, event2):
        return True
    for player1 in event1.players:
        for player2 in event2.players:
            if player1 is player2:
                if error_level:
                    assert False, "player " + player1.name + " in two games " + event1.str() + " " + event2.str()
                return False
    return True


def check_events(events, error_level):
    for event1 in events:
        for event2 in events:
            if event1 is event2:
                continue
            if not check_two_events(event1, event2, error_level):
                return False
    return True


def check_playground(events, error_level):
    for event1 in events:
        for event2 in events:
            if event1 is event2:
                continue
            assert event1.sport is event2.sport
            if is_intersecting(event1, event2):
                if error_level:
                    assert False, "playground for " + event1.sport.name + " is busy by two games " + event1.str() \
                                  + " " + event2.str()
                return False
    return True


def check_all_playground(sports, events, error_level):
    sport2events = {}
    for sport in sports:
        sport2events[sport] = []
    for event in events:
        sport2events[event.sport].append(event)
    for sport in sports:
        check_playground(sport2events[sport], error_level)
