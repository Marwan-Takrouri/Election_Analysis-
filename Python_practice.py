9

#score =int(input("what is your test score"))
#if score >=90:
   # print('your grade is A')
#elif score >=80:
   # print ('your grade is B')
#elif score >=70:
    #print('your grade is c')
#elif score >=60:
   # print ('your grade is d')
#else :

    #print ('your grade is f')
    

counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    
    #print("El Paso is not the list of counties.")
#if "Arapahoe" in counties or "El Paso"  not in counties:
 
      #  print("only Arapahoe is in the list of counties ")
#else :
      # print("Arapahoe is in the list or El Paso is not in the list of counties.")
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
   # print(county , "county has " , voters ,"number of voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for i n range(leni(voting_data)):        
    #print(voting_data[i],['county'])       

#for county_dict in voting_data:
     #print(county_dict['county'])
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items()
    #print(f"{county} county has {voters} registered voters.")
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
   # f"You received {candidate_votes} number of votes. "
   # f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100}% of the total votes.")
#print(message_to_candidate)
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
   # print(f"{county} county has {voters :,} registered voters")

voting_dict = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]   
for county, voters in voting_dict:
     print("county" + "  has " + str(voters) + " registered voters.")
   
        

    














