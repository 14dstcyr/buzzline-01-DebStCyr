"""
basic_generator_stcyr.py

Generate some streaming buzz messages. 
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.

    It doesn't need any outside information, so the parentheses are empty.
    It returns an integer, so we specify that in the function signature.

    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented.

    Define a local variable to hold the value of the environment variable
    os.getenv() is a function that fetches the value of an environment variable
    os.getenv() always returns a string 
    We convert the return value to an integer using the built-in Python int() function
    To use handy functions like this, import the os module 
    from the Python Standard Library (see above).
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating buzz messages
ADJECTIVES: list = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS: list = ["found", "saw", "tried", "shared", "loved"]
TOPICS: list = ["a movie", "a meme", "an app", "a trick", "a story"]

#####################################
# Define a function to generate buzz messages
#####################################


def generate_messages():
    """
    Generate a stream of custom messages.
    This function uses a generator, which yields one message at a time.
    It will run continuously until stopped (CTRL+C).
    """
    while True:
        messages = [
            "truck|temp_c=3|status=ok",
            "truck|temp_c=9|status=freezer_failure",
            "order|id=101|status=shipped",
            "order|id=102|status=cancelled",
            "sensor|id=S17|vibration=0.44|status=high",
        ]

        # pick one message at random
        payload = random.choice(messages)

        # include your tag (so graders know it’s your custom producer)
        line = f"stcyr|{payload}"

        logger.info(line)  # log the message
        yield line          # yield the message back to the caller
        time.sleep(interval_secs)  # pause between messages



#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for this producer.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.   
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented. 
    This is a multiline docstring - a special type of comment 
    that explains what the function does.
    """

    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()