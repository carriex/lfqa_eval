# lfqa_eval

## Introduction
This is the repository for annotated data and model for this paper: </br>

> Fangyuan Xu*, Yixiao Song*, Mohit Iyyer and Eunsol Choi. [A Critical Evaluation of Evaluations for Long-form Question Answering](https://arxiv.org/abs/2305.18201).
> In: Proceedings of ACL. 2023.
> *= Equal Contribution.

We collected expert preferences for pairwise machine-generated and human-written long-form answers, together with free-form justification of why they prefer one answer than the other. We curated a collection of human preferences of long-form answers from previous work. 
We evaluated a suite of automatic metrics on this collection of human evaluation data. We release the human evaluation data as well as code for automatic evaluations.


## Data

We release processed pairwise human preference data under `preference_data/`. This collection includes  the expert annotations we collected and previously released human evaluation from these prior work:

* "[Hurdles to Progress in Long-form Question Answering](https://arxiv.org/abs/2103.06332)".
* "[WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)".

Each example is a json with the following field:
* `question`: The question.
* `answer_a` and `answer_b`: the two answer paragraphs being compared
* `doc_a` and `doc_b` (optional): the corresponding evidence documents, only available for WebGPT comparisons.
* `answer_a_type` and `answer_b_type`: corresponds to the name of the model which generated the answer, or `human` for human-written answers.
* `overall_preference`: Overall preference, value is -1 (`answer_a` wins), 0 (tie) or 1 (`answer_b` wins).
* `coherence_preference` (optional): Coherence preference, value is -1 (`answer_a` wins), 0 (tie) or 1 (`answer_b` wins).
* `factuality_preference` (optional): Factuality preference, value is -1 (`answer_a` wins), 0 (tie) or 1 (`answer_b` wins).
* `justification` (optional): free-form justification of why the annotator prefers one answer over the other.

Note:
* WebGPT comparisons distinguish between "better than" and "much better than". We collapse the data to a binary preference or tie.
* The processed data contains preferences with tie, whereas in our automatic evaluation we removed tie data.

The unprocessed data from the prior work can be found at: 
* Hurdles comparisons: [here](https://github.com/martiansideofthemoon/hurdles-longform-qa).
* WebGPT comparisons: [here](https://openaipublic.blob.core.windows.net/webgpt-answer-viewer/comparisons.jsonl)

### Raw expert annotations
Raw expert annotations as well as annotations interface are under `raw_annotation_data`.

### Automatic evaluation

For Self-BLEU, refer to this [script](https://github.com/ari-holtzman/degen/blob/master/metrics/self_bleu.py).

#### Reference-based
Please refer to the respective repo for [BertScore](https://github.com/Tiiiger/bert_score) and [BLEURT](https://github.com/google-research/bleurt).

For BERTScore, we use the default `roberta-large` model for English (https://github.com/Tiiiger/bert_score) and report the maximal F1 BERTScore against the set of reference answers.

For BLEURT, we use the `BLERUT-20` checkpoint.

#### (Question, answer) metics
Please refer to [BARTScore](https://github.com/neulab/BARTScore) repo for running BARTScor. We use `facebook/bart-large-cnn` which is fine-tuned on the CNN/DM dataset.

For RANKGEN, refer to [RANKGEN](https://github.com/martiansideofthemoon/rankgen), we use the question as the prefix and the entire answer paragraph as the suffix to rank. We use the [RankGen-XL-all](https://huggingface.co/kalpeshk2011/rankgen-t5-xl-all).

#### (Answer, reference) metric
Refer to the [QAFactEval](https://github.com/salesforce/QAFactEval) repo for downloading the models and setting up the environments. We provide a script `run_qafacteval.py` which can be used to run QAFactEval to check the answer against the reference documents.

#### Lerened metrics
We are cleaning the code to release the learned long-former based reward model. Please contact the author (fangyuan[at]utexas.edu) if you would like to test it on your own data.


## Citation and contact
If you find our work helpful, please cite us as

```
@inproceedings{lfqa23,
author={Fangyuan Xu and Yixiao Song and Mohit Iyyer and Eunsol Choi},
Booktitle = {Association of Computational Linguistics},
Year = "2023",
Title={A Critical Evaluation of Evaluations for Long-form Question Answering},
}
```

📧 Please contact Fangyuan Xu at `fangyuan[at]utexas.edu` if you have any questions.
