![logo](https://github.com/YashShreshthaRaj404/binary_code/blob/main/binary-ndeaveyqv9hps1g9.jpg)

#### Binary Code
is the most basic form of computer code, consisting of two numbers: 0 and 1. These numbers form the basic layer of all computing systems and are the primary language of digital technologies. Binary code uses combinations of these two numbers to represent numbers, letters, or other types of information.



## Decimal numerals represented by binary Digits

#### decimal	binary	conversion...

0	0	0 ( 20 )
1	1	1 ( 20 )
2	10	1 ( 21 ) + 0 ( 20 )
3	11	1 ( 21 ) + 1 ( 20 )
4	100	1 ( 22 ) + 0 ( 21 ) + 0 ( 20 )
5	101	1 ( 22 ) + 0 ( 21 ) + 1 ( 20 )
6	110	1 ( 22 ) + 1 ( 21 ) + 0 ( 20 )
7	111	1 ( 22 ) + 1 ( 21 ) + 1 ( 20 )
8	1000	1 ( 23 ) + 0 ( 22 ) + 0 ( 21 ) + 0 ( 20 )
9	1001	1 ( 23 ) + 0 ( 22 ) + 0 ( 21 ) + 1 ( 20 )
10	1010	1 ( 23 ) + 0 ( 22 ) + 1 ( 21 ) + 0 ( 20 )

## Importance of binary code
The binary number system is the base of all computing systems and operations. It enables devices to store, access and manipulate all types of information directed to and from the CPU or memory. This makes it possible to develop applications that enable users to do the following:

•view websites
•create and update documents
•play games
•view streaming video and other kinds of graphical information
•access software and 
perform calculations and data analyses.

##### The binary schema of digital 1s and 0s offers a simple and elegant way for computers to work. It also offers an efficient way to control logic circuits and to detect an electrical signal's true (1) and false (0) states.

## How Binary Numbers Work

The binary system is the primary language of computing systems. Inside these systems, a binary number consists of a series of eight bits. This series is known as a byte. In the binary schema, the position of each digit determines its decimal value. Thus, by understanding the position of each bit, a binary number can be converted into a decimal number.

In decimal numbers, each additional place is multiplied by 10 as we move from right to left (first place, 10th place, 100th place, etc.). But, in binary numbers, each additional place while moving from right to left is multiplied by two. The two examples below explain this idea.

##### Example 1
Here's how the decimal values are calculated for an 8-bit (byte) binary number 01101000.

In this number, the first digit is at the far right, while the eighth digit is at the far left. The second (0) to the seventh (1) digits are read from right to left.

Bit position

1

2

3

4

5

6

7

8

Bit

0

0

0

1

0

1

1

0

Binary-to-decimal calculation (exponent)

20

21

22

23

24

25

26

27

Decimal value (x2)

1

2

4

8

16

32

64

128

As the bit position increases from one to eight, the previous decimal value is multiplied by two. That's why the first bit has a value of 1, the second bit has a value of 2, the third bit has a value of 4 and so on.

The final value of the decimal number is calculated by adding the individual values from the above table. However, only those values where the bit equals 1 should be added. These values represent the "on" position. The 0s represent the "off" position, so they are not counted in the decimal value calculation.

So, for the binary number 01101000, the decimal value is calculated as the following:

8 + 32 + 64 = 104

##### Example 2
Here's how the decimal values are calculated for the binary number 11111111.

Bit position

1

2

3

4

5

6

7

8

Bit

1

1

1

1

1

1

1

1

Binary-to-decimal calculation (exponent)

20

21

22

23

24

25

26

27

Decimal value

1

2

4

8

16

32

64

128

In this binary number, every bit has a value of 1, so all the individual values are added.

So, for this number, the decimal value is the following:

1 + 2 + 4 + 8 + 16+ 32 + 64 +128 = 255


## Representing decimal numbers in binary format

As mentioned earlier, the binary numbering system only works with 1s and 0s. However, the position of just these two digits can represent many more numbers. The examples in the previous section show how any decimal number from 0 to 255 can be represented using binary numbers. Numbers larger than 255 can also be represented by adding more bits to an 8-bit binary number.

Here are the decimal numbers from zero to 20 and their binary equivalents.

#### Decimal number	Binary number	Decimal number	Binary number

0

0

11

1011

1

1

12

1100

2

10

13

1101

3

11

14

1110

4

100

15

1111

5

101

16

10000

6

110

17

10001

7

111

18

10010

8

1000

19

10011

9

1001

20

10100

10

1010

![logo](https://github.com/YashShreshthaRaj404/binary_code/blob/main/non_printing_ascii_control_codes-f.png)

## Converting binary numbers into text characters

Binary numbers can be translated into text characters using American Standard Code for Information Interchange (ASCII) codes to store information in the computer's RAM or CPU. ASCII-capable applications, like word processors, can read text information from the RAM or CPU. They can also store text information that can then be retrieved by the user at a later time. ASCII codes are stored in the ASCII table, which consists of 128 text or special characters. Each character has an associated decimal value.



In the first example of the previous section, the binary number is 01101000 (decimal number 104). In ASCII, this number would produce lowercase h. To form words, more letters need to be added to h. In binary terms, this means adding more binary numbers to the binary number for h.

##### Example
The binary code for ASCII lowercase i is 01101001. So, to create the word hi, the binary number for i is added to the binary number for h. This yields the following binary number:

01101000 + 01101001 = 0110100001101001

In decimal terms, the decimal numbers for h and i are 104 and 105, respectively.

Other common examples of binary numbers converted to ASCII text code are the following.

Binary number	Decimal number	ASCII code
110000

48

0

1000001

65

A (uppercase)

1111111

127

DEL key

11011

27

ESC key


