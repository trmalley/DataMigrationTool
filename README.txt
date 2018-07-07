#########################################################################################################################
#  _____       _______         __  __ _____ _____ _____         _______ _____ ____  _   _   _______ ____   ____  _      #
# |  __ \   /\|__   __|/\     |  \/  |_   _/ ____|  __ \     /\|__   __|_   _/ __ \| \ | | |__   __/ __ \ / __ \| |     #
# | |  | | /  \  | |  /  \    | \  / | | || |  __| |__) |   /  \  | |    | || |  | |  \| |    | | | |  | | |  | | |     #
# | |  | |/ /\ \ | | / /\ \   | |\/| | | || | |_ |  _  /   / /\ \ | |    | || |  | | . ` |    | | | |  | | |  | | |     #
# | |__| / ____ \| |/ ____ \  | |  | |_| || |__| | | \ \  / ____ \| |   _| || |__| | |\  |    | | | |__| | |__| | |____ #
# |_____/_/    \_\_/_/    \_\ |_|  |_|_____\_____|_|  \_\/_/    \_\_|  |_____\____/|_| \_|    |_|  \____/ \____/|______|#
#########################################################################################################################

###Intro###
Let's the user pick two paths (Source/Destination) and will transfer the data accordingly.
This tool uses robocopy for windows to complete this task, therefore it will only work in windows.
Currently you cannot run the program until a source is selected, the destination has a default
of the current users desktop in a folder called 'Backup-current-date' Ex.( C:\Users\user\Desktop\Backup-07-06-18)

The program creates a log file in the main directory called batch.log. 
This can be viewed to ensure the transfer completed or to see how many items failed.
The batch.log file is also read an printed in the main GUI.

###STEPS###

1 - Select Source Path Ex.(D:\Users\user) <- user profile from HDD plugged in via USB

2 - Select Destination Path Ex. (C:\Users\user\Desktop\Backup-dd-mm-yy) <- This is the default Destination Path

3 - Once the Source Path is selected the "Run" button will be enabled. Hit Run to start the transfer.

4 - Wait for data transfer to finish, check log to confirm all required data has been transfered.

Extra Step 5 - Confirm the data has been transferd properly by comparing both folders

Once the transfer is started it will not stop until completion. To end Transfer early simply close the program.


###SAMPLE OUTPUT###

------------------------------------------------------------------------------

               Total    Copied   Skipped  Mismatch    FAILED    Extras
    Dirs :     11684       732     10952         0         0         5
   Files :         2         1         1         0         0         0
   Bytes :    13.4 k         0    13.4 k         0         0         0
   Times :   0:01:39   0:00:00                       0:00:00   0:01:39
   Ended : July 6, 2018 8:50:13 PM



This tool is still a work in progress, the GUI is plain and simple. 

###No Installation Required!###

The source code has been compiled into an exe and can be run from anywhere, even a USB!
All files need to stay in the same folder in order for the program to work
