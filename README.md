# Double Side Printing for MPC Fill
<p>Pyhton script to merge Magic the Gathering decks.</p>
It creates a CSV file to be used at MPCfill.com<br>
It has been tested with txt files downloaded from mtggoldfish.com<br>
<s>The file merge.py and the 2 .txt deck files (front.txt and back.txt) need to be in the same folder.</s><br>
Place the decklist text files in the respective front_decks or back_decks folder.
To run the script type:<br>
<i>python merge.py</i><br>
The file merged.csv will be generated and placed in the CSV folder.<br>
Upload that file to mpcfill.com<br>
 changelog:<br>
    0.2 = Added a new feature: merging multiple decks for front and back cards. Decklist can be added directly to <br>
    the front_decks and back_decks folders. Also created a temp folder to keep temporary files in one place.
    

Created with python 3.10.
