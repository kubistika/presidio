import logging
from typing import Dict

from presidio_anonymizer.entities import InvalidParamException
from presidio_anonymizer.operators import OperatorType, Operator


class OperatorsFactory:
    """Operators factory to get the correct operator class."""

    _anonymizers: Dict = None
    _decryptors: Dict = None

    def __init__(self):
        self.logger = logging.getLogger("presidio-anonymizer")

    def create_operator_class(self, operator_name: str,
                              operator_type: OperatorType) -> Operator:
        """
        Extract the operator class from the operators list.

        :param operator_type: Either Anonymize or Decrypt to defer between operators.
        :type operator_name: operator name.
        :return: operator class entity.
        """
        operator_class = {
            OperatorType.Anonymize: OperatorsFactory.get_anonymizers().get(
                operator_name),
            OperatorType.Decrypt: OperatorsFactory.get_decryptors().get(operator_name),
        }.get(operator_type)
        if not operator_class:
            self.logger.error(f"No such operator class {operator_name}")
            raise InvalidParamException(
                f"Invalid operator class '{operator_name}'."
            )
        self.logger.debug(f"applying class {operator_class}")
        return operator_class()

    @staticmethod
    def get_anonymizers() -> \
            Dict[str, "Operator"]:
        """Return all anonymizers classes currently available."""
        if not OperatorsFactory._anonymizers:
            OperatorsFactory._anonymizers = OperatorsFactory.__get_operators_by_type(
                OperatorType.Anonymize)
        return OperatorsFactory._anonymizers

    @staticmethod
    def get_decryptors() -> \
            Dict[str, "Operator"]:
        """Return all decryptors classes currently available."""
        if not OperatorsFactory._decryptors:
            OperatorsFactory._decryptors = OperatorsFactory.__get_operators_by_type(
                OperatorType.Decrypt)
        return OperatorsFactory._decryptors

    @staticmethod
    def __get_operators_by_type(operator_type: OperatorType):
        operators = Operator.__subclasses__()
        return {cls.operator_name(cls): cls for cls in operators if
                cls.operator_type(cls) == operator_type}
