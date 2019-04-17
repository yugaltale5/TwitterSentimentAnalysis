# TwitterSentimentAnalysis
It includes good looking GUI made with Python Tkinter library.
Uses Tweepy for fetching the tweets and TextBlob library for Analysis.
Creates a Pie chart based on observations and displays the result in Browser or Text editor.


*Requirements:
1. Twitter Developer Account to get Secret Keys to access API.
   Enter those keys in test.py program.
   Install Tweepy by using following command
   
   sudo pip install tweepy
   
2. Install TextBlob Library

   sudo pip install TextBlob
   
3. Install tkinter

   sudo pacman -S tk  (for Arch Linux users)
   
   sudo apt-get install python-tk  (for Debian based OS users)
   
   pip install EasyTkinter  (For Windows users)
   
4. Install Matplotlib
   
   sudo pip install matplotlib
   sudo pacman -S python-matplotlib  (for Arch Users)
   
How to Use:

Just run TSA.py on Linux based os as:

(Make sure that Firefox is installed as Final report will be opened in new tab of Browser if result contains emojies else report will be displayed in TK window itself.)
    
    python TSA.py
And:
    python tsa.py   (for Windows)
    
1: In Input Box enter Word.

2: Hit Submit Button.

3: Hit Show Sentiment Analysis Report.
   Pie Chart will appear after few Seconds. 
   Close that window to view per Tweet Analysis.
   
 
