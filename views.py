from django.shortcuts import render
from kernel.http import Response
from boot.rules.stack import BOOT_RULESTACK
from profiles.decorators import load_profile

@load_profile
def load_basic_data(request):
    """
    This function is used to load basic data for the application
    """
    res = Response(request=request)
    list_rules = BOOT_RULESTACK.list_rules()
    for rule in list_rules:
        rule.gpm_run(res=res)
    return res.success()
