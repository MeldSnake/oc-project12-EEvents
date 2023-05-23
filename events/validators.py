from django.core.exceptions import ValidationError
from contracts.models import Contract
from django.utils.translation import gettext_lazy as _


def validate_signed_contract(contract: Contract | int):
    if isinstance(contract, int):
        if contract == 0:
            return
        contract = Contract.objects.get(pk=contract)
    if not contract.signed:
        raise ValidationError(
            _("The selected contract is not signed"),
            params={'contract': contract}
        )
