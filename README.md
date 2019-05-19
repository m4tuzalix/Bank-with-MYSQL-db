# Bank-with-MYSQL-db
Banking application with many useful features. Application allows user to create account which is saved as indenpendent file. Each file contatins 9 lines of text which are responsisible for different things. Registration proccess requires login, password, secret question and secret answer. Additionaly each account has security code, automatically generated if user has registered account succesfully.

In a nutshell application contains:

deposit system

withdraw system

transfer system (send money to other users)

currency account system

currency transfers (equal system to normal transfer)

adding funds from usual account to currency account. The current currency is USD and usual is PLN. My application USD rate has been set to 3.80

token system (activation or deactivation) If token is active, indenpendent window pops up after each positive log-in process before leting to get into bank account. Window contains random code made from asci letters and numbers which changes after each 10 seconds. To get into account, user must rewrite the code correctly.

logs system - All actions performed on account as log-in, log-out, money operations etc. are saved in separate folder, in spearate file related with username. Each action is written in separate line with exact date and time next to it.

admin system - System with admin gui to control users' accounts. Currently admin can display all data stored in common user file, line by line. Admin can delete accounts or suspend them. This system is going to be rebuilded yet in order to add more options. Admin accounts are created manually and stored in special folder.

Hazard system - User can play roulete or lotto. Roulete script has 3 mods, 50% chance of winning, 30% and 10%. The lower chance, the higher prize to won. User decides what amount to put to roulete. 50% chance gives the 20% of given amount if win, 30% chance gives 50% amount given and 10% chance gives 100% amount given. Lotto is self explenatory, system generates randomly 6 numbers in range 1-49. User has to provide 6 numbers which cannot be lower than 0 or duplicate. If at least one number has been guessed, the information with the number is shown on the screen. If user guesses at least 3 numbers, wins. The system of wins is in built now. The money for win will be granted from 3 numbers guessed and above. Also, to play lotto user must buy tickets. Currently 1-3-5-10 tickets mode are available. Each ticket will cost and the money from buys will be stored on bank's special account what is already in my plans to write in nearest fitire.
