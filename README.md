# Hi, how-are-you?

This project is a small script which, when paired with your `.bashrc`, asks you each day (the first time you open your terminal that day) to rank how you're feeling and logs it. 

Running the `how-are-you.py` script generates a file called `feelings.txt` which is used to store your feelings entries.  For now, I'm not going to upload my `feelings.txt`, for obvious reasons.


To make this work with your `.basrhc`,  you can paste these lines at the end of your `.bashrc`:

```
# runs script when the terminal is opened
# note: script won't prompt you if you've already answered that day
python "/path/to/script/how-are-you.py"
```

This prompt only happens the first time you open a terminal that day. Every other time you open your terminal that day, you won't see this prompt.
