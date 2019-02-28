from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mturk_demo'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    contribution_sum = models.IntegerField()

    def calc_total_contribution(self):
        # check if there are actually two players in the group, otherwise somebody clicked "finish study"
        num_players = len(self.get_players())
        if num_players == 1:
            return

        sum = 0
        for player in self.get_players():
            # load each players contribution and mark as matched
            contribution = player.participant.vars.get('contribution', 0)
            player.was_matched = True

            # then sum up contributions
            sum += contribution


        self.contribution_sum = sum


class Player(BasePlayer):
    was_matched = models.BooleanField(initial=False)