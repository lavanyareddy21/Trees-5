#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'threatDetector' function below.
#
# The function accepts STRING_ARRAY textMessages as parameter.
#




def threatDetector(textMessages):
    for message in textMessages:
        if len(message) < 6:  # Account for the 3-character symbol
            print("Invalid input")
            continue
            
        symbol = message[-3:]
        alphanumeric_text = ''.join(c for c in message[:-3] if c.isalnum())
        
        if len(alphanumeric_text) < 4:
            print(f"{symbol} Ignore")
            continue
        
        score = calculate_score(alphanumeric_text)
        
        if 1 <= score <= 10:
            score_level = "Possible"
        elif 11 <= score <= 40:
            score_level = "Probable"
        elif 41 <= score <= 150:
            score_level = "Escalate"
        else:
            score_level = "Ignore"
            
        # Check if the message contains "IOT" and if so, set score_level to "Ignore"
        if "IOT" in message:
            score_level = "Ignore"
            
        print(f"{symbol} {score_level}")

def calculate_score(text):
    score = 0
    for i in range(len(text)):
        for j in range(i + 3, len(text) + 1):
            if palindrome_check(text[i:j]):
                score = score + (j - i)
    return score

def palindrome_check(s):
    return s == s[::-1] and len(s) >= 3








if __name__ == '__main__':
    textMessages_count = int(input().strip())

    textMessages = []

    for _ in range(textMessages_count):
        textMessages_item = input()
        textMessages.append(textMessages_item)

    threatDetector(textMessages)