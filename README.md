# PBL_tool: keyword search

## Idea:
We are using the API **PubMed** to get access to published papers and the textmining is done with **regex**. The user is will be able to use the tool on a webpage, we created with **html**. 
For the Layout we use **CSS**. All html files are resided in the templates folder.

## Workflow:
* For now the tool can be executed by running the *start.py* script and opening the link that is given in the output terminal.
* By opening the link, the *input.html* file is opened. Here the user input can be parsed, we allow a keyword, a number for the amount of papers that is wished to be returned, as well as filter options (filter options are not included into relevance score yet).
* When the submit button is pressed, the *input_post* function in the script *start.py* is executed. The user input is requested from the *input.html* file and the *runner.py* file is being called and gets parsed the user input.
* The *runner.py* file opens PubMed and returns the wished amount of papers, that contain the keyworld, for each paper an instance of the class *Paper* in the script *paper.py* is created.
* ***TODO***: Make the scanning Progress faster! It's taking AAAAGES!! ANY IDEAS ARE WELCOME
* You can run the *runner.py* with an argument parser for testing purposes. For more info on the parser execute *runner.py --help*
* In the Paper object we are saving the title, a list of the authors, the publishing date, and the PubMed Id for each paper, as well as a count of the occuring keyword.
* When the paper is created, the abstracts and titles are scanned for the keyword using regex and the relevance score is computed.
* ***TODO***: IMPROVE the relevance score
* The list of papers is then sorted by score
* The script *runner.py* creates a list of all the Paper-objects and parses it to the script *dataframe.py*, which creates a dataframe for a pandas table.
* This table is returned to the function *input_post* in the script *start.py*, which convertes it into an html table and returns the *output.html* tamplate, which gets parsed the html table.
* On the webpage, the *output.py* is shown, displaying a the table with the search results. It is possible to retun to the *input.html* at any time, clicking on input again.
* Here it is possible to resort the returned papers by date, author, title and score. When submitted, the function *sorting* in *start.py* requests the radio input and resorts the globally saved dataframe of papers (called *list*) by column.
* ***TODO***: links to PubMed pages for each resulting Paper.
