# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:48:51 2019

@author: kruti
"""


def numUniqueEmails(emails: 'List[str]') -> 'int':
    add_email = []
    for i in emails:
        split1 = i.split("@")
        split2 = split1[0].split("+")
        concat1 = "".join(split2[0].split("."))
        concat2 = concat1+"@"+split1[1]
        add_email.append(concat2)
    #print(set(add_email))
    return len(set(add_email))

numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])