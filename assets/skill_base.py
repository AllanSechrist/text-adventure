


class Skill():
    """
    Base class for making skills
    Power will be used as a percentage multiplier
    Type should be a string -> 'offensive', 'defensive', 'buff', 'debuff', 'charge'
    """
    def __init__(self, caster, power, tp_cost, type):
        self.caster = caster
        self.power = power
        self.tp_cost = tp_cost
        self.type = type
        self.element = None
        self.skill_level = 0






            
