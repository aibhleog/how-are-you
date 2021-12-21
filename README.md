# Hi, how-are-you?

This project is a small script which, when paired with your `.bashrc`, asks you each day (the first time you open your terminal that day) to rank how you're feeling and logs it. 

Running the `how-are-you.py` script generates a file called `feelings.txt` which is used to store your feelings entries.  For now, I'm not going to upload my `feelings.txt`, for obvious reasons -- however I've generated a fake feelings list (`random_feelings.txt`) that I used to make example plots (`random_tracker.pdf` & `random_hist.pdf`).


To make this work with your `.basrhc`,  you can paste these lines at the end of your `.bashrc`:

```bash
# runs script when the terminal is opened
# note: script won't prompt you if you've already answered that day
python "/path/to/script/how-are-you/how-are-you.py"
```

This prompt only happens the first time you open a terminal that day. Every other time you open your terminal that day, you won't see this prompt.


## Other scripts in this repo
There are three other scripts in this repo that hopefully you'll also find useful!  I'll describe them below.

- `see-feelings.py` -- reads in your `feelings.txt` file and plots up how you've been answering over time.
- `see-hist.py` -- reads in your `feelings.txt` file and plots the entries as a histogram to get idea of how you've answered overall (this script is run at the end of `see-feelings.py`).
- `update-feeling.py` -- allows you to update your feeling entry for the present date (pulls & replaces the value in the last row of the `feelings.txt` file.
- `generate-fake-feelings.py` -- a quick script I threw together to make `random_feelings.txt` so you can see how the feelings are stored and how they're used in the plots (check out `random_tracker.pdf` & `random_hist.pdf` for plot examples!).

I recommend you reference both `see-feelings.py` and `update-feelings.py` as aliases in your `.bashrc` file!  That way you can run this from your terminal, regardless of location.  Here's how mine look:

```bash
# alias for showing feelings tracker
alias feel='python /path/to/script/how-are-you/see-feelings.py'
# alias for updating feelings entry
alias newfeel='python /path/to/script/how-are-you/update-feeling.py'
```
