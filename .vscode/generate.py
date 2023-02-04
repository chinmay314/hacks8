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
    def __init__(self, events, activitiesAdded, nextTimeSlot, names):
        # list of events(event objects), dict of activity types added, next time slot available
        self.events = events
        self.activitiesAdded = activitiesAdded
        self.nextTimeSlot = nextTimeSlot
        self.names = names

    def getEvents(self):
        return self.events

    def getActivitiesAdded(self):
        return self.activitiesAdded

    def getNextTimeSlot(self):
        return self.nextTimeSlot

    def getNames(self):
        return self.names


class e:
    def __init__(self, name, activityType):
        self.name = name
        self.activityType = activityType

    def getName(self):
        return self.name

    def getActivityType(self):
        return self.activityType

allEvents = [e("Nature trail1", "nature"), e("Museum1", "history"), e("Exhibition1", "art"), e("Exhibition2", "art"),
             e("Nature trail2", "nature"), e("Museum2", "history"), e("Bar1", "bars"), e("Bar2", "bars"),
             e("Live concert 1", "music"), e("Live concert 2", "music")]

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
    stack.append(schedule(eventsStart, activitiesAdded, 0, startnames))
    while (len(stack) != 0):
        s = stack.pop()
        if s.nextTimeSlot >= 900:
            finalSchedules.append(s)
            continue
        if 120 <= s.getNextTimeSlot() <= 300 and s.getActivitiesAdded()["food"] == 0:
            s.events.append(event("Lunch", (s.getNextTimeSlot(), s.getNextTimeSlot() + 90), "food1"))
            s.getActivitiesAdded()["food"] = 1
            s.nextTimeSlot += 35
            stack.append(s)
            continue
        if 510 <= s.getNextTimeSlot() <= 720 and s.getActivitiesAdded()["food"] == 1:
            s.events.append(event("Dinner", (s.getNextTimeSlot(), s.getNextTimeSlot() + 90), "food2"))
            s.getActivitiesAdded()["food"] = 2
            s.nextTimeSlot += 35
            stack.append(s)
            continue
        for e in allEvents:
            if (e.getActivityType() == "bars" or e.getActivityType() == "music") and s.getActivitiesAdded()["food"] != 2:
                continue
            if e.getActivityType() == "nature" and s.getActivitiesAdded()["food"] >= 1:
                continue
            if s.getActivitiesAdded()[e.getActivityType()] == 2 or e.getName() in s.getNames():
                continue
            eventsNew = s.getEvents().copy()
            eventsNew.append(event(e.getName(), (s.getNextTimeSlot(), s.getNextTimeSlot() + times[e.getActivityType()]),
                                   e.getActivityType()))
            newActivitiesAdded = s.getActivitiesAdded().copy()
            newActivitiesAdded[e.getActivityType()] += 1
            nts = s.getNextTimeSlot() + times[e.getActivityType()] + 35
            newnames = s.getNames().copy()
            newnames.append(e.getName())
            snew = schedule(eventsNew, newActivitiesAdded, nts, newnames)
            stack.append(snew)
    return finalSchedules

def rank(schedules, preferences):
    ranked = []
    ranked.append((0, 0))
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
            if r[0] <= points:
                ranked.insert(counter, (points, s))
                break
            counter+=1
    ranked.remove((0, 0))
    return ranked







schedules = generate(allEvents)
schedules = rank(schedules, ["art", "nature", "music", "bars", "history"])
#value = ""
#counter = 1
#for s in schedules:
#    points = s[0]
#    s = s[1]
#    value += "Schedule " + str(counter) + ": \n"
#    for e in s.getEvents():
#        value += e.getName() + " from " + str(e.getTimeRange()[0]) + " to " + str(e.getTimeRange()[1]) + "\n"
#    value += str(points) + " points total"
#    value += "\n \n"
#    counter += 1
#print(value)
