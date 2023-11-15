import random
import time
from typing import List

from prefect import flow, task


def randomly_fail():
    # Generate a random number between 0 and 1
    failure_probability = random.random()
    print(failure_probability)
    
    # Fail 50% of the time
    if failure_probability < 0.5:
        raise Exception("Random failure occurred!")
    else:
        print("Code executed successfully.")


@task(retries=2)
def run_validation_simulation(test_phrase: str, model_id: str):
    print(f"test_phrase {test_phrase}, model_id {model_id}")
    time.sleep(random.randint(0, 10))
    randomly_fail()
    return {"test_phrase": test_phrase, "model_id": model_id}


@flow(log_prints=True)
def run_validation_simulations(test_phrases: List[str], model_id: str):
    for test_phrase in test_phrases:
        run_validation_simulation(test_phrase, model_id)

    return {"test_phrases": test_phrases, "model_id": model_id}


if __name__ == "__main__":
    # create your first deployment
    run_validation_simulations.serve(
        name="1",
        # parameters={"test_phrases": ["a", "b", "c"], "model_id": "model1"}
    )
