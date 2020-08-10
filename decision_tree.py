# outcomes = [{"values": [], "likelihood": 1}] outcome = {"values": [], "likelihood": 1}

# [a, b] [c,d]
# [a], 0.5. [b], 0.5
# [a,c], 0.25. [a,d], 0.25. [b,c], 0.25. [b,d], 0.25

# need to show each turn with probability

# requirement: calculate

BOMB = -1

class balance:
    def __init__(self, turn_values=None, probabilities=None):
        self.turn_values = []
        self.probabilities = []
        if turn_values:
            self.turn_values.extend(turn_values)
        if probabilities:
            self.probabilities.extend(probabilities)

    def __repr__(self):
        return "<decision tree object. turn values: %s, probabilities: %s >" % (self.turn_values, self.probabilities)

    def get_round(self, round_number):
        turn_values = self.turn_values[:round_number]
        probabilities = self.probabilities[:round_number]
        return balance(turn_values, probabilities)

    def total_balance(self):
        if self.turn_values[-1] == -1:
            balance = 0
        else:
            balance = sum(self.turn_values)
        return balance


def add_list_element(array, outcome):
    next_outcomes = []
    # need to move this up a level to save time
    probability = 1/len(array)
    for n, value in enumerate(array):
        # editing outcome for last step should add big time saving
        # can add exit point on bomb here
        new_outcome = balance()
        new_outcome.turn_values = outcome.turn_values.copy()
        new_outcome.probabilities = outcome.probabilities.copy()
        new_outcome.turn_values.append(value)
        try:
            new_outcome.probabilities.append(outcome.probabilities[-1] * probability)
        except IndexError:
            new_outcome.probabilities.append(1 * probability)
        next_outcomes.append(new_outcome)
    return next_outcomes



def calculate_outcomes(arrays):
    outcomes = [balance()]
    for array in arrays:
        all_next_outcomes = []
        for outcome in outcomes:
            try:
                if outcome.turn_values[-1] == -1:
                    single_next_outcomes = [outcome]
                else:
                    single_next_outcomes = add_list_element(array, outcome)
            except IndexError:
                single_next_outcomes = add_list_element(array, outcome)
            all_next_outcomes.extend(single_next_outcomes)
        outcomes = all_next_outcomes
    return outcomes
