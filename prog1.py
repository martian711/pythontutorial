import sys
def table1to10(num):
    for i in range(1,11):
        i=i*num
        print i
    return 0

def main():
    print 'Hello World. This is my First Program';
    a = 5
    if a == 5:
        a = a*5
    print a
if __name__ == '__main__':
    main()
    #num = input('Enter your number')
    #table1to10(num)
    print sys.argv[0]
#    print "\a"
#    print "\t\t\t \\ \\ \\ \\ \\ \\ \\"
#    print "\t\t\t \\ \\ \\ \\ \\ \\ \\"
#    print "You can concatenate two " + "strings with the '+' operator."
#    print "\nThis string " + "may not " + "seem terr" + "ibly impressive. " \
#+ "But what " + "you don't know," + " is that " + "it's one real" \
#+ "l" + "y" + " long string, created from the concatenation " \
#+ "of " + "thirty-two " + "different strings, broken across " \
#+ "nine lines." + " Now are you" + " impressed?\n\n" + "See, " \
#+ "even newlines can be embedded into a single string, making" \
#+ " it look " + "as " + "if " + "it" + "'s " + "got " + "to " \
#+ "be" + " multiple strings." + " Okay, now this " + "one " \
#+ "long" + " string " + "is over!"
#print 
#"""
#If you really like a string, you can repeat it. For example, who doesn't
#like pie? That's right, nobody. But if you really like it, you should
#say it like you mean it:""",
#print "Pie" * 10
#print "\nNow that's good eating."
#print \
#"""
#If a pregnant hippo, weighing 2,000 pounds, gives birth to a 100 pound calf,
#but then eats 50 pounds of food, how much does she weigh?"""
#raw_input("Press the enter key to find out.")
#print "2000 - 100 + 50 = ",
#print 2000 - 100 + 50
#print \
#"""
#If an adventurer returns from a successful quest and buys each of
#6 companions 3 bottles of ale, how many bottles does the adventurer buy?"""
#raw_input("Press the enter key to find out.")
#print "6 * 3 = ",
#print 6 * 3
#print \
#"""
#If a kid has 24 pieces of Halloween candy and eats 6 pieces a day,
#how many days will the stash last?"""
#raw_input("Press the enter key to find out.")
#print "24 / 6 = ",
#print 24 / 6
#print \
#"""
#If a group of 4 pirates finds a chest full of 107 gold coins, and
#they divide the booty evenly, how many coins will be left over?"""
#raw_input("Press the enter key to find out.")
#print "107 % 4 = ",
#print 107 % 4
#raw_input("\n\nPress the enter key to exit.")


a = "Vivekanand Pandey"
#print a[3]
#print a[3:5]
print a[-4:6]