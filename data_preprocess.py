import numpy as np
def process(features):
    
    All_Airlines={'Air Asia': 0, 'Air India': 1, 'Go Air': 2, 'IndiGo': 3, 'Jet Airways': 4, 'Jet Airways Business': 5, 'Multiple carriers': 6, 'Multiple carriers Premium economy': 7, 'SpiceJet': 8, 'Trujet': 9, 'Vistara': 10,'Vistara Premium economy': 11}
    All_Sources={'Banglore': 0, 'Chennai': 1, 'Delhi': 2, 'Kolkata': 3, 'Mumbai': 4}
    All_Destination={'Banglore': 0, 'Cochin': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4,'NewDelhi': 5}
    All_Additional_info={'1 Long layover': 0, '1 Short layover': 1, '2 Long layover': 2, 'Business class': 3, 'Change airports': 4, 'In-flight meal not included': 5, 'No Info': 6, 'No check-in baggage included': 7, 'No info': 8, 'Red-eye flight': 9}

    Stops=int(features[0])
    dep_hour=int(features[1].split(':')[0])
    dep_min=int(features[1].split(':')[1])
    Arrival_hour=int(features[2].split(':')[0])
    Arrival_min=int(features[2].split(':')[1])
    duration=int(features[3].split('h')[0])
    Airline=int(All_Airlines[features[4]])
    Source=int(All_Sources[features[5]])
    Destination=int(All_Destination[features[6]])
    Additional_info=int(All_Additional_info[features[7]])                    #         | S      #|Dest       |Additional
    l=[Stops,Arrival_hour,Arrival_min,dep_hour,dep_min,duration,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                                               #Airline
    #Airline=6 after
    l[5+Airline]=1
    l[17+Source]=1
    l[22+ Destination]=1
    l[28+Additional_info]=1
    l=np.array(l)
    return l

    