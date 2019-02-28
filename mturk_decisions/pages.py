from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def before_next_page(self):
        # make contribution available to other apps.
        self.player.participant.vars['contribution'] = self.player.contribution


page_sequence = [
    Contribution
]
