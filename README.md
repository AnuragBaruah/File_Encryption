# An App to Encrypt and Decrypt Files
With the help of this program the users will be able to generate an encrypted file. The encrypted file then can be stored or sent safely and secretly (for whatever purposes). The program will prompt the user with 2 options, encrypt or decrypt. After an option is selected, the user will be asked for the path of the desired file. The program will then create a new file which will contain the same information as the original file in the encrypted or decrypted form.<br><br>
1. Encryption.<br>
The rules for encryption will be generated randomly but uniquely. The first few lines of the encrypted file will contain the set of rules for decrypting. Those rules will be written in some predetermined code language. The next part of the encrypted file will contain the main contents of the file in the generated code language.<br>
i. Two types of files exist. Text files and binary files.<br>
ii. The binary files will be converted to their text forms.<br>
iii. Each character of the file (text or converted to text) will be coded in a “special way”.<br>
iv. The “special way” will be generated during the running of the program and the “special way” will be coded using a predetermined set of rules and then attached to the resulting encrypted file. There will be some separator symbol separating the “special way” and the main content. The original file format will also be mentioned along with the “special way”<br>
v. An encrypted file will always be a text file (“.txt”). <br>
<br>
2. Decryption.<br>
i. User will give the text file containing the encrypted information<br>
ii. The information from the file will be divided into 3 parts:<br>
a. “special way”<br>
b. Original file format <br>
• File extension<br>
• Type of data – string or bytes<br>
c. Coded information<br>
iii. The “special way” will be decoded using a pre programmed set of rules<br>
iv. Then the coded information will be decoded using the rules mentioned in the “special way”<br>
v. The information thus gathered (either strings or bytes) will be fed into a new file with the proper file extension.<br>
vi. Thus the encrypted file will be decrypted.<br>

Logic for Encryption<br>
1. Each and every character of content of the file will be encrypted.<br>
2. Each and every character code will be separated by a “.” (fullstop).<br>
3. Hence, “hello” will look something like “79.88.75.75.90” (this is not the real code though)<br>
4. All non alphanumeric characters (special characters and whitespace characters) will be coded as follows.<br>
a. A random number (positive or negative integer but not zero) will be generated at the beginning<br>
b. The corresponding ordinal (ASCII) value of the character will be added with that number.<br>
c. The resulting number will be converted to string form and there will be a “?” preceding the number. This is the character code for non alphanumeric characters <br>
5. Alphabets:<br>
a. Vowels<br>
i. Computer will randomly choose an even number greater than 26 and less than or equal to 100 and assign it to variable “a”.<br>
ii. Again computer will randomly choose an even number greater than 0 and less than or equal to 12 and assign it to variable “d”.<br>
iii. The position of the vowel in the alphabet will be stored in the variable “r”.<br>
iv. Code for the vowel will be as follows: c = a + (r -1)*d<br>
v. The resulting number will be converted to string form. This is the character code for vowels. <br>
b. Consonants:<br>
i. Computer will randomly choose an odd number 26<n<=100, and assign to “a”.<br>
ii. Again computer will randomly choose an even number 0<n<=12, and assign to “d”<br>
iii. The position of the consonant in the alphabet will be stored in “r”.<br>
iv. Code for the consonant: c = a + (r - 1)*d<br>
v. The resulting number will be converted to string form. This is the character code for consonants<br>
c. If any letter (vowel or consonant) is uppercase then, a random lowercase letter will precede the character code. Hence, the presence of a small letter before any letter’s code would mean that the particular letter is a capital letter.<br>
<br>
6. Digits<br>
a. A random non zero integer (positive or negative) will be generated first and assigned to “r”<br>
b. The code of the digit will be: c = <Some random capital letter> + str(digit + r)<br>
c. The presence of a random capital letter before any number in the code will indicate that the code represents a digit.<br>
7. The random numbers generated would be required for decryption. That information will be coded using Caesar’s chipper, where each character will be shifted towards the left (or right) by a certain value (say 5).<br>
8. Also the original file format (.txt or .exe or .mp4 or. jpg etc) will be coded using Caesar’s chipper using the same left (or right) shifting.
