The dataset in this folder accompanies our paper accepted to [ACL 2023](https://2023.aclweb.org). This folder has two sub-folders as described below.

- Annotated_Dataset: 
	- Each `.json` file contains all the data annotated by one expert. The informative keys are the following:
		- `q_id`: ids of a question in the [r/explainlikeimfive](https://www.reddit.com/r/explainlikeimfive/) forum
		- `question_text`: a combination of `title` (the question) and `selftext` (further description of the question, if there is one) scraped from the [r/explainlikeimfive](https://www.reddit.com/r/explainlikeimfive/) forum
		- `answer1`: either a human-written or a model-generated answer
		- `answer2`: either a human-written or a model-generated answer
		- `answer1_label`: Each label consists of 3 letters and 1 or 2 numbers in square brackets. The label indicates whether the comparison is between human-written and model-generated answers (H/M) or between two human-written answers (H/H).
			- The first two letters:
				- `HH`: both answers are human-written
				- `HM`: one answer is human-written, the other is model-generated
			- The third letter indicates the type of `answer1`:
				- `H`: `answer1` is human-written with higher upvotes
				- `h`: `answer1` is human-written with lower upvotes
				- `M`: `answer1` is model-generated
			- The numbers indicate the upvote numbers of the human-written answers. Example: HHh[10][1] means that both answers are human-written, `answer1` has a lower upvote number (i.e., 1), `answer2` has a higher upvote number (i.e., 10).
		- `BetterAnswer`: Answer A = answer1, Answer B = answer2
		- `DifficultToChoose`: whether it was difficult to choose which answer is better
		- `Comments`: the free-form justification that the annotators offered
		- `annotator`: id number of the annotator
		
- `Label_Studio`
	- `Label_Studio.html`: the html interface for our experts to do the annotation tasks
	- `*_label_studio_common20.tsv`: the question-answer pairs that were to be annotated by the experts. Lines are tab separated. Each file has 5 columns: `q_id`, `question_text`, `answer1`, `answer2`, and `answer1_label`. They are the same as in the `.json` files.

		