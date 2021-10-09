from modules.starvation import Starvation
from modules.wrong_option import WrongOption
from python_test_system import TestSystem


if __name__ == '__main__':
    testSystem = TestSystem.TestSystem()

    testSystem.iterate([
        Starvation,
        WrongOption,
    ])