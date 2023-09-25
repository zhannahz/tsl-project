import random


in_cave = False
in_market = False
in_town = False
count_in_town = 0
count_in_market = 0
count_in_cave = 0
passage = ""
summary = ""

def to_town(passage):
    seed_value = 13
    random.seed(13)

    global in_town, count_in_town
    if (random.random() < 0.6):
        in_town = True
        count_in_town += 1

    print("in town")
    return "to town"


def to_market(passage):
    seed_value = 67
    random.seed(seed_value)

    global in_market, count_in_market
    if (random.random() < 0.6):
        in_market = True
        count_in_market += 1

    print("in market")
    return "to market"

def to_cave(passage):
    seed_value = 43
    random.seed(seed_value)

    global in_cave, count_in_cave
    if (random.random() < 0.6):
        in_cave = True
        count_in_cave += 1
    print("in cave")
    return "to cave"


#
# def update_state(current_state):
#     # Define passage and summary as empty strings by default
#     global passage
#     global summary
#
#     if current_state == 0:
#         if not in_cave and not in_market and not in_town:
#             passage = to_town()
#             summary = update_summary
#             current_state = 1
#         elif in_cave or in_market or in_town:
#             current_state = 2
#     elif current_state == 1:
#         if not in_cave and not in_market and in_town:
#             passage = to_market()
#             summary = update_summary
#             current_state = 3
#         elif in_cave:
#             current_state = 7
#         elif in_market:
#             passage = to_cave()
#             current_state = 7
#         elif in_town:
#             passage = to_cave()
#             current_state = 7
#     elif current_state == 2:
#         if not in_cave and not in_market and not in_town:
#             current_state = 2
#         elif in_cave or in_market or in_town:
#             current_state = 7
#     elif current_state == 3:
#         if not in_cave and in_market and not in_town:
#             passage = to_town()
#             summary = update_summary
#             current_state = 4
#         elif in_cave:
#             current_state = 7
#         elif in_market:
#             passage = to_cave()
#             current_state = 7
#         elif in_town:
#             passage = to_cave()
#             current_state = 7
#     elif current_state == 4:
#         if not in_cave and in_market and not in_town:
#             passage = to_market()
#             summary = update_summary
#             current_state = 5
#         elif in_cave:
#             current_state = 7
#         elif in_market:
#             passage = to_cave()
#             current_state = 7
#         elif in_town:
#             passage = to_cave()
#             current_state = 7
#     elif current_state == 5:
#         if not in_cave and in_market and not in_town:
#             passage = to_cave()
#             summary = update_summary
#             current_state = 6
#         elif in_cave:
#             current_state = 7
#         elif in_market:
#             passage = to_cave()
#             current_state = 7
#         elif in_town:
#             passage = to_cave()
#             current_state = 7
#     elif current_state == 6:
#         if not in_cave:
#             current_state = 7
#         elif in_cave:
#             passage = to_cave()
#             current_state = 7
#
#     return current_state, passage, summary


def update_summary(sum):
    # Update the summary
    sum = "summary"
    return sum


def update_state(current_state):
    passage = ""
    summary = ""

    if current_state == 0:
        if not (in_cave) and not (in_market) and not (in_town):
            passage = to_town(passage)
            summary = update_summary(passage)
            current_state = 1
        if in_cave:
            current_state = 2
        if in_market:
            current_state = 2
        if in_town:
            current_state = 2
    elif current_state == 1:
        if not (in_cave) and in_market and in_town:
            passage = to_town(passage)
            summary = update_summary(passage)
            current_state = 3
        if not (in_cave) and not (in_market) and in_town:
            passage = to_market(passage)
            summary = update_summary(passage)
            current_state = 4
        if in_cave:
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if in_cave:
            current_state = 8
        if in_cave:
            summary = update_summary(passage)
            summary = summary
            current_state = 8
        if not (in_town):
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_town):
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            current_state = 8
        if not (in_town):
            summary = update_summary(passage)
            summary = summary
            current_state = 8
    elif current_state == 2:
        if not (in_cave):
            current_state = 2
        if in_cave:
            current_state = 8
    elif current_state == 3:
        if not (in_cave) and not (in_market) and in_town:
            passage = to_market(passage)
            summary = update_summary(passage)
            current_state = 5
        if not (in_cave) and in_market and in_town:
            passage = to_cave(passage)
            summary = update_summary(passage)
            current_state = 6
        if in_cave:
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if in_cave:
            current_state = 8
        if in_cave:
            summary = update_summary(passage)
            summary = summary
            current_state = 8
        if not (in_town):
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_town):
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            current_state = 8
        if not (in_town):
            summary = update_summary(passage)
            summary = summary
            current_state = 8
    elif current_state == 4:
        if not (in_cave) and in_market:
            passage = to_town(passage)
            summary = update_summary(passage)
            current_state = 3
        if in_cave:
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = to_town(passage)
        if in_cave:
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if in_cave:
            current_state = 8
        if in_cave:
            summary = update_summary(passage)
            summary = summary
            current_state = 8
        if not (in_market):
            current_state = 8
        if not (in_market):
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if not (in_market):
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_market):
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if not (in_market):
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_market):
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if not (in_market):
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if not (in_market):
            current_state = 8
        if not (in_market):
            summary = update_summary(passage)
            summary = summary
            current_state = 8
    elif current_state == 5:
        if not (in_cave) and in_market:
            passage = to_cave(passage)
            summary = update_summary(passage)
            current_state = 6
        if in_cave:
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if in_cave:
            current_state = 8
        if in_cave:
            summary = update_summary(passage)
            summary = summary
            current_state = 8
        if not (in_market):
            current_state = 8
        if not (in_market):
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if not (in_market):
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_market):
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if not (in_market):
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_market):
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if not (in_market):
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if not (in_market):
            current_state = 8
        if not (in_market):
            summary = update_summary(passage)
            summary = summary
            current_state = 8
    elif current_state == 6:
        if in_cave and in_market:
            summary = update_summary(passage)
            passage = passage
            current_state = 7
        if in_cave and not (in_town):
            summary = update_summary(passage)
            passage = passage
            current_state = 7
        if not (in_cave):
            current_state = 8
        if not (in_cave):
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if not (in_cave):
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_cave):
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if not (in_cave):
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_cave):
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if not (in_cave):
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if not (in_cave):
            current_state = 8
        if not (in_cave):
            summary = update_summary(passage)
            summary = summary
            current_state = 8
        if in_cave and not (in_market) and in_town:
            summary = update_summary(passage)
            passage = passage
            current_state = 8
    elif current_state == 7:
        if not (in_cave) and not (in_town):
            passage = to_town(passage)
            summary = update_summary(passage)
            current_state = 3
        if not (in_cave) and not (in_market) and in_town:
            passage = to_market(passage)
            summary = update_summary(passage)
            current_state = 5
        if not (in_cave) and in_market and in_town:
            passage = to_cave(passage)
            summary = update_summary(passage)
            current_state = 6
        if in_cave:
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if in_cave:
            current_state = 8
        if in_cave:
            summary = update_summary(passage)
            summary = summary
            current_state = 8
        if not (in_town):
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_town):
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if not (in_town):
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if not (in_town):
            current_state = 8
        if not (in_town):
            summary = update_summary(passage)
            summary = summary
            current_state = 8
    elif current_state == 8:
        if not (in_cave) and not (in_market):
            passage = to_market(passage)
            summary = update_summary(passage)
            current_state = 5
        if not (in_cave) and in_market:
            passage = to_cave(passage)
            summary = update_summary(passage)
            current_state = 6
        if in_cave:
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_market(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_cave(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = to_town(passage)
            current_state = 8
        if in_cave:
            passage = to_market(passage)
            passage = passage
            current_state = 8
        if in_cave:
            passage = to_town(passage)
            passage = passage
            current_state = 8
        if in_cave:
            current_state = 8
        if in_cave:
            summary = update_summary(passage)
            summary = summary
            current_state = 8

    return current_state, passage, summary


current_state = 0

print("initial:", current_state,
      ", in_cave:", in_cave, count_in_town,
      ", in_market", in_market, count_in_market,
      ", in_town", in_town, count_in_town)

# iterate through the states until in_cave is true
i = 0
while not in_cave:
    current_state, passage, summary = update_state(i)
    i += 1

print("end:", current_state,
      ", in_cave:", in_cave, count_in_town,
      ", in_market", in_market, count_in_market,
      ", in_town", in_town, count_in_town)
