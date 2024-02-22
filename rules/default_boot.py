
from boot.rules.stack import BOOT_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager

import PIL
import os

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True

    def __init__(self) -> None:
        super().__init__()

    def gpm_run(self, *args, **kwargs):
        """
        The run function for the boot profile.
        """
        res = kwargs.get('res')
        res.authenticated = res.is_authenticated()

BOOT_RULESTACK.set_rule(DefaultRuleClass())