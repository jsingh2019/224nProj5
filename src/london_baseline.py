# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

#need to import utils because of line 21, tqdm and argparse because 18
import utils
from tqdm import tqdm
import argparse

#getting args
argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
#argparse.ArgumentParser().add_argument('--outputs_path', default=None)
args = argp.parse_args()

#Actual Eval
correct = 0
total = 0
predictions = []
for line in tqdm(open(args.eval_corpus_path)):
    pred = "London"
    predictions.append(pred)
total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('Predictions written to {}; no targets provided'
            .format(args.outputs_path))
