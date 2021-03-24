"""Result item for the /decrypt method."""
from presidio_anonymizer.entities.engine.result import EngineResultItem


class DecryptedEntity(EngineResultItem):
    """Information about the decrypted entity."""

    def __init__(
            self,
            start: int,
            end: int,
            entity_type: str,
            decrypted_text: str,
    ):
        """
        Decrypted text data item.

        :param start: start index of the decrypted text in the general text.
        :param end: end index of the decrypted text in the general text.
        :param entity_type: the entity type of the text.
        :param decrypted_text: the text after the decryption.
        """
        EngineResultItem.__init__(self, start, end, entity_type)
        self.decrypted_text = decrypted_text

    def __eq__(self, other: 'DecryptedEntity') -> bool:
        """
        Verify two DecryptedEntity are equal.

        :param other: DecryptedEntity
        :return: bool
        """
        return (self.start == other.start
                and self.end == other.end
                and self.entity_type == other.entity_type
                and self.decrypted_text == other.decrypted_text)

    def get_text(self):
        """
        Get the text after we performed the operator over it.

        :return: the text we operated over and this decrypt result represent.
        """
        return self.decrypted_text
