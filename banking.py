{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "class Customer:\n",
    "    \"Customer Class With Bank Operation\"\n",
    "    bank_name=\"Apna Bank\"\n",
    "    def __init__(self,name,balance=0.0):\n",
    "        self.name=name\n",
    "        self.balance=balance\n",
    "    def deposite(self,amt):\n",
    "        self.balance=self.balance+amt\n",
    "        print(\"Balance After Deposite Is:\",self.balance)\n",
    "    def withdrawal(self,amt):\n",
    "        if amt>self.balance:\n",
    "            print(\"Insufficient Balance!!!!!Cannot Perform This Operation\")\n",
    "            sys.exit()\n",
    "        else:    \n",
    "            self.balance=self.balance-amt\n",
    "            print(\"Balance After Withdrawal Is:\",self.balance)\n",
    "print(\"Welcome To!!!\",Customer.bank_name)\n",
    "name=input(\"Enter Your Name:\")\n",
    "c=Customer(name)\n",
    "while True:\n",
    "    print(\"D-Deposite\\nW-Withdrawal\\nE-exit\")\n",
    "    option=input(\"Enter Your Option:\")\n",
    "    if option=='d' or option=='D':\n",
    "        amt=float(input(\"Enter Amount:\"))\n",
    "        c.deposite(amt)\n",
    "    elif  option=='w' or option=='W':\n",
    "        amt=float(input(\"Enter Amount:\"))\n",
    "        c.withdrawal(amt)\n",
    "    elif option=='e' or option=='E':\n",
    "        print(\"\\nThanks For Banking With Us!!!!!\")\n",
    "        sys.exit()\n",
    "    else:\n",
    "        print(\"Invalid Option!!!Please Choose Valid Option!!! \")\n",
    "\n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
