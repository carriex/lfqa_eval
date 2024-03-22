"""
Please clone this repo https://github.com/salesforce/QAFactEval and copy this file over.
Before running, make sure to download all the models needed below.
For the input csv, `reference` is a concatenation of all the reference documents and `answer_paragraph` contains the answer.
"""

import json
import argparse
import pandas as pd
from qafacteval import QAFactEval


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Running QAFactEval')
    parser.add_argument('--fname', default=None, required=True)
    parser.add_argument('--outfname', default=None, required=True)
    parser.add_argument('--model_folder', default='models')
    parser.add_argument('--cuda_device', default=0, type=int)
    parser.add_argument('--use_lerc_quip', default=False, action='store_true')
    parser.add_argument('--verbose', default=False, action='store_true')
    parser.add_argument('--generation_batch_size', default=32, type=int)
    parser.add_argument('--answering_batch_size', default=32, type=int)
    parser.add_argument('--lerc_batch_size', default=8, type=int)

    args = parser.parse_args()
    kwargs = {"cuda_device": args.cuda_device, "use_lerc_quip": args.use_lerc_quip, \
        "verbose": args.verbose, "generation_batch_size": args.generation_batch_size, \
        "answering_batch_size": args.answering_batch_size, "lerc_batch_size": args.lerc_batch_size}
    print(kwargs)
    metric = QAFactEval(
        lerc_quip_path=f"{args.model_folder}/quip-512-mocha",
        generation_model_path=f"{args.model_folder}/generation/model.tar.gz",
        answering_model_dir=f"{args.model_folder}/answering",
        lerc_model_path=f"{args.model_folder}/lerc/model.tar.gz",
        lerc_pretrained_model_path=f"{args.model_folder}/lerc/pretraining.tar.gz",
        **kwargs
    )
    print('>> loaded the model')

    candidates = []
    references_list = []
    datas = []
    input_csv = pd.read_csv(args.fname)

    for _, data in input_csv.iterrows():
        datas.append(data)
        ref = data['reference'] # adpated for our usage.
        summ = data['answer_paragraph']
        candidates.append(ref)
        references_list.append([summ])

    print("{} pairs of data".format(len(candidates)))
    print("Scoring the data")
    results = metric.score_batch_qafacteval(candidates, references_list, return_qa_pairs=True)
    metric_list, qa_pair_list, qa_pair_original_list, pred_list = [], [], [], []
    for (metrics, qa_pairs, qa_pairs_original, predictions_cons) in results:
        metric_list.append(metrics)
        qa_pair_list.append(qa_pairs)
        qa_pair_original_list.append(qa_pairs_original)
        pred_list.append(predictions_cons)
    input_csv['metric'] = metric_list
    input_csv['qa_pair'] = qa_pair_list
    input_csv['qa_pair_unfiltered'] = qa_pair_original_list
    input_csv['pred'] = pred_list

    # save as json!
    input_csv.to_json(args.outfname)
    print("Output stored to {}".format(args.outfname))