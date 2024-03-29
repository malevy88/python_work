# for loop intro
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# print message to each in a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# prints out both messages for each magician 
# (cycles through both until program/loop is done)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # \n inserts the line break between loops
    print(f"I can't wait to see your next trick, {magician.title()}.\n") 
    
#prints after for loop since not indented (part of)
print("Thanks you, everyone. That was a great magic show!") 

#won't run since there is no indentation
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician) 

#this is a logical error
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

#another logical error, last line indented so Python runs all the valid code
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")


#forgetting the colon (this won't run)
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians
  #  print(magicians)