# lfqa_eval
ACL 2023 paper [A Critical Evaluation of Evaluations for Long-form Question Answering](https://www.cs.utexas.edu/~fxu/pdfs/lfqa_eval_2022_website.pdf).
## Introduction
This is the repository for annotated data and model for this paper: </br>

> Fangyuan Xu*, Yixiao Song*, Mohit Iyyer and Eunsol Choi. [A Critical Evaluation of Evaluations for Long-form Question Answering](https://www.cs.utexas.edu/~fxu/pdfs/lfqa_eval_2022_website.pdf).
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
* WebGPT comparisons: [here](https://
openaipublic.blob.core.windows.net/webgpt-answer-viewer/comparisons.jsonl.)

### Raw expert annotations
Raw expert annotations as well as annotations interface are under `raw_annotation_data`.

### Automatic evaluation

We are working on releasing the scripts to reproduce the automatic metric evaluation in the paper.

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
