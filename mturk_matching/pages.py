from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage


# The custom mturk wait page has to be the first page of the app, thus we need two apps!
class GroupMatching(CustomMturkWaitPage):
    group_by_arrival_time = True
    use_task = False # Do not show a risk task or real effort task on wait page
    skip_until_the_end_of = 'experiment' # if waited too long and wants to quit, go to end of experiment
    startwp_timer = 15 # offer to quit study after 30s
    def after_all_players_arrive(self):
        # careful! This is also executed if the participant chooses to leave the study!
        self.group.calc_total_contribution()


class Results (CustomMturkPage):
    pass


class DropOuts(Page):
    def is_displayed(self):
        return not self.player.was_matched


page_sequence = [
    GroupMatching,
    Results,
    DropOuts
]
