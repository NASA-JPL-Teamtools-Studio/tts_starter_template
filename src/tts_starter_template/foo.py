from typing import Optional

from tts_utilities.logger import create_logger

logger = create_logger(name="foo")


class Foo:
    """
    Description for placeholder class Foo.

    Parameters
    ----------
    input_1:
        Placeholder int input.
    input_2:
        Placeholder int input, which defaults to None.
    """

    def __init__(self, input_1: int, input_2: Optional[int] = None):
        self.input_1 = input_1
        self.input_2 = input_2

    def bar(self):
        """
        Description for placeholder method bar, which does addition and
        defaults to input_2 = 1 if none is provided.

        Parameters
        ----------
        input_1:
            Placeholder int input.
        input_2:
            Placeholder int input, which defaults to None.
        """

        if self.input_2 is None:
            logger.warning("Overriding input_2 to 1 since it is None")
            self.input_2 = 1

        return self.input_1 + self.input_2
