# Image 1
from nltk.translate.bleu_score import sentence_bleu
reference = [['a', 'man', 'sitting', 'on', 'the', 'ground', 'with', 'a', 'frisbee']]
candidate = ['The', 'little', 'boy', 'fell', 'face', 'first', 'into', 'the', 'grass', 'while', 'playing', 'football']
score = sentence_bleu(reference, candidate)
print(score)
# Image 2
from nltk.translate.bleu_score import sentence_bleu
reference = [['a', 'group', 'of', 'boys', 'play', 'flag', 'football', 'while', 'some', 'bystanders', 'watch']]
candidate = ['a', 'group', 'of', 'young', 'men', 'playing', 'a', 'game', 'of', 'soccer']
score = sentence_bleu(reference, candidate)
print(score)
# Image 3
from nltk.translate.bleu_score import sentence_bleu
reference = [['a', 'man', 'is', 'checking', 'out', 'an', 'injured', 'football', 'player', 'at', 'a', 'game']]
candidate = ['a', 'group', 'of', 'men', 'on', 'a', 'field', 'playing', 'baseball']
score = sentence_bleu(reference, candidate)
print(score)
# Image 4
from nltk.translate.bleu_score import sentence_bleu
reference = [['a', 'group', 'of', 'men', 'on', 'a', 'field', 'playing', 'baseball']]
candidate = ['a', 'football', 'team', 'doing', 'excercises']
score = sentence_bleu(reference, candidate)
print(score)
# Image 5
from nltk.translate.bleu_score import sentence_bleu
reference = [['a', 'football', 'player', 'is', 'getting', 'tackled']]
candidate = ['a', 'group', 'of', 'men', 'on', 'a', 'field', 'playing', 'soccer']
score = sentence_bleu(reference, candidate)
print(score)