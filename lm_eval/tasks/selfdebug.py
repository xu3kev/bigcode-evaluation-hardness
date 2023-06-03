# This template file is adapted from: https://github.com/EleutherAI/lm-evaluation-harness/blob/master/templates/new_task.py
from evaluate import load

# TODO: Remove all TODO comments once the implementation is complete.
"""
TODO: Add the Paper Title on this line.
TODO: Add the paper's PDF URL (preferably from arXiv) on this line.
TODO: Write a Short Description of the task.
Homepage: TODO: Add the URL to the task's Homepage here.
"""
from lm_eval.base import Task

# TODO: Add the BibTeX citation for the task.
_CITATION = """
"""


# TODO: Replace `NewTask` with the name of your Task.
class SelfDebug(Task):
    # TODO: Add the `DATASET_PATH` string. This will be the name of the `Task`
    # dataset as denoted in HuggingFace `datasets`.
    PREVIOUS_CODEGEN = "./starcoder_humaneval_t02.json"
    # TODO: Add the `DATASET_NAME` string. This is the name of a subset within
    # `DATASET_PATH`. If there aren't specific subsets you need, leave this as `None`.
    DATASET_NAME = None

    DATASET_PATH = "openai_humaneval"

    def __init__(self):
        super().__init__(
            stop_words=["\nclass", "\n#", "\n@", "\nprint", "\nif", "\nFeedback", "correct.\n"],
            requires_execution=True,
        )

    def get_dataset(self):
        """Returns dataset for the task or an iterable of any object, that get_prompt can handle"""
        return self.dataset["test"]

    def get_prompt(self, doc):
        """Builds the prompt for the LM to generate from."""
        import json
        with open("starcoder_humaneval_t02.json", "r") as f:
            data = json.loads(f.read())
        with open("./lm_eval/tasks/few_shot_examples/self_debug_few_shot.py") as f:
            fewshot_code = f.read()
        #import pdb; pdb.set_trace()
        task_id = int(doc["task_id"].split("/")[-1])
        previous_code = data[task_id][0]

        try:
            extract_comments = doc["prompt"].split('"""')[1] 
        except:
            try:
                extract_comments = doc["prompt"].split("'''")[1]
            except:
                import pdb; pdb.set_trace()


        extract_comments = "\n".join(line.lstrip() for line in extract_comments.split("\n"))
        extract_comments = '"""' + extract_comments + '"""\n'
        
        #ret = fewshot_code + extract_comments  + previous_code + "\nFeedback: The code above is wrong. Please fix it.\ndef " + doc["entry_point"] + "("
        ret = fewshot_code + extract_comments  + previous_code + "\nFeedback: The code above is "
        print(ret)
        
        return ret

    def get_reference(self, doc):
        """Builds the reference solution for the doc (sample from the test dataset)."""
        test_func = doc["test"]
        entry_point = f"check({doc['entry_point']})"
        return "\n" + test_func + "\n" + entry_point

    @staticmethod
    def _stop_at_stop_token(decoded_string, stop_tokens):
        """
        Produces the prefix of decoded_string that ends at the first occurrence of
        a stop_token.
        WARNING: the decoded_string *must not* include the prompt, which may have stop tokens
        itself.
        """
        print(decoded_string)
        min_stop_index = len(decoded_string)
        for stop_token in stop_tokens:
            stop_index = decoded_string.find(stop_token)
            if stop_index != -1 and stop_index < min_stop_index:
                min_stop_index = stop_index
        return decoded_string[:min_stop_index]

    def postprocess_generation(self, generation, idx):
        """Defines the postprocessing for a LM generation.
        :param generation: str
            code generation from LM
        :param idx: int
            index of doc in the dataset to which the generation belongs
            (not used for Humaneval-Task)
        """
        prompt = self.get_prompt(self.dataset["test"][idx])
        generation = generation[len(prompt) :]
        if generation.strip().split(" ")[0][0:5] == "wrong":
            if "\nFeedback" in generation:
                #entry_point = self.dataset["test"][idx]["entry_point"]
                ret = generation.split("\n",1)[-1].split("\nFeedback",1)[0]
                print(ret)
                return ret

        import json
        with open("starcoder_humaneval_t02.json", "r") as f:
            data = json.loads(f.read())
        task_id = int(self.dataset["test"][idx]["task_id"].split("/")[-1])
        ret = data[task_id][0]
        print(ret)
        return ret

    def process_results(self, generations, references):
        """Takes the list of LM generations and evaluates them against ground truth references,
        returning the metric for the generations.
        :param generations: list(list(str))
            list of lists containing generations
        :param references: list(str)
            list of str containing refrences
        """
        code_metric = load("code_eval")
        results, _ = code_metric.compute(
            references=references,
            predictions=generations,
        )
        return results