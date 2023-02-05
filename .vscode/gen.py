import random
class event:
    def __init__(self, name, timeRange, activityType):
        # name of event, tuple range of times, type of activity
        self.name = name
        self.timeRange = timeRange
        self.activityType = activityType

    def getName(self):
        return self.name

    def getTimeRange(self):
        return self.timeRange

    def getActivityType(self):
        return self.activityType


class schedule:
    def __init__(self, events, activitiesAdded, nextTimeSlot, names, points, id):
        # list of events(event objects), dict of activity types added, next time slot available
        self.events = events
        self.activitiesAdded = activitiesAdded
        self.nextTimeSlot = nextTimeSlot
        self.names = names
        self.points = points
        self.id = id

    def getEvents(self):
        return self.events

    def getActivitiesAdded(self):
        return self.activitiesAdded

    def getNextTimeSlot(self):
        return self.nextTimeSlot

    def getNames(self):
        return self.names
    def getPoints(self):
        return self.points
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id


class e:
    def __init__(self, name, activityType):
        self.name = name
        self.activityType = activityType

    def getName(self):
        return self.name

    def getActivityType(self):
        return self.activityType

allEvents = [("nature", (0, 0), "Nature trail1"), ("nature", (0, 0), "Nature trail2"), ("music", (0, 0), "Concert1"), ("music", (0, 0), "Concert2"),
             ("bars", (0, 0), "Bar1"), ("bars", (0, 0), "Bar2"), ("art", (0, 0), "Art museum1"), ("art", (0, 0), "Art museum2"),
             ("history", (0, 0), "WW2 museum"), ("history", (0, 0), "WW1 museum")]

def generate(allEvents):
    times = {
        "music": 90,
        "history": 165,
        "art": 165,
        "nature": 120,
        "bars": 90}
    stack = []
    eventsStart = []
    startnames = []
    activitiesAdded = {
        "food": 0,
        "history": 0,
        "art": 0,
        "bars": 0,
        "nature": 0,
        "music": 0
    }
    finalSchedules = []
    stack.append(schedule(eventsStart, activitiesAdded, 0, startnames, 0, 0))
    while (len(stack) != 0):
        s = stack.pop()
        if s.nextTimeSlot >= 840:
            finalSchedules.append(s)
            continue
        if 120 <= s.getNextTimeSlot() <= 300 and s.getActivitiesAdded()["food"] == 0:
            s.events.append(event("Lunch", (s.getNextTimeSlot(), s.getNextTimeSlot() + 90), "food1"))
            s.getActivitiesAdded()["food"] = 1
            s.nextTimeSlot += 90 + random.randint(1, 3)*15
            stack.append(s)
            continue
        if 510 <= s.getNextTimeSlot() <= 720 and s.getActivitiesAdded()["food"] == 1:
            s.events.append(event("Dinner", (s.getNextTimeSlot(), s.getNextTimeSlot() + 90), "food2"))
            s.getActivitiesAdded()["food"] = 2
            s.nextTimeSlot += 90 + random.randint(1, 3)*15
            stack.append(s)
            continue
        for e in allEvents:
            if e[0] == "food":
                continue
            if (e[0] == "bars" or e[0] == "music") and s.getActivitiesAdded()["food"] != 2:
                continue
            if e[0] == "nature" and s.getActivitiesAdded()["food"] >= 1:
                continue
            if s.getActivitiesAdded()[e[0]] == 2 or e[2] in s.getNames():
                continue
            if e[0] == "art" and s.getNextTimeSlot()+times["art"] >= 690:
                continue
            finaltime = s.getNextTimeSlot() + times[e[0]]
            if s.getNextTimeSlot() < max(e[1][0], 0) or (int(finaltime) > int(e[1][1]) and e[1][1] != 0):
                continue
            eventsNew = s.getEvents().copy()
            finishtime = min(s.getNextTimeSlot() + times[e[0]], 840)

            eventsNew.append(event(e[2], (s.getNextTimeSlot(), finishtime),
                                    e[0]))
            newActivitiesAdded = s.getActivitiesAdded().copy()
            newActivitiesAdded[e[0]] += 1
            nts = finishtime + random.randint(1, 3)*15
            newnames = s.getNames().copy()
            newnames.append(e[2])
            snew = schedule(eventsNew, newActivitiesAdded, nts, newnames, 0, 0)
            stack.append(snew)
    return finalSchedules

def rank(schedules, preferences):
    ranked = []
    max = 0
    for s in schedules:
        points = 0
        for i in range(5):
            amount = s.getActivitiesAdded()[preferences[i]]
            if amount == 1:
                points += 20*(i+1)
            if amount == 2:
                points += 1.5*20*(i+1)
        counter = 0
        for r in ranked:
            if points <= r.getPoints():
                ranked.insert(counter-1, s)
            counter+=1
        if counter==0:
            ranked.append(s)
    counter = 0
    for r in ranked:
        r.setId(counter)
        counter+=1
    return ranked







schedules = generate(allEvents)
schedules = rank(schedules, ["art", "nature", "music", "bars", "history"])
# value = ""
# counter = 1
# for s in schedules:
#    points = s[0]
#    s = s[1]
#    value += "Schedule " + str(counter) + ": \n"
#    for e in s.getEvents():
#        value += e.getName() + " from " + str(e.getTimeRange()[0]) + " to " + str(e.getTimeRange()[1]) + "\n"
#    value += str(points) + " points total"
#    value += "\n \n"
#    counter += 1
# print(value)
