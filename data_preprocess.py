def process(features):
    
    All_Airlines={'Air Asia': 0, 'Air India': 1, 'GoAir': 2, 'IndiGo': 3, 'Jet Airways': 4, 'Jet Airways Business': 5, 'Multiple carriers': 6, 'Multiple carriers Premium economy': 7, 'SpiceJet': 8, 'Trujet': 9, 'Vistara': 10,'Vistara Premium economy': 11}
    All_Sources={'Banglore': 0, 'Chennai': 1, 'Delhi': 2, 'Kolkata': 3, 'Mumbai': 4}
    All_Destination={'Banglore': 0, 'Cochin': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4,'New Delhi': 5}
    All_Additional_info={'1 Long layover': 0, '1 Short layover': 1, '2 Long layover': 2, 'Business class': 3, 'Change airports': 4, 'In-flight meal not included': 5, 'No Info': 6, 'No check-in baggage included': 7, 'No info': 8, 'Red-eye flight': 9}

    Stops=features[0].astype(int)
    dep_hour=features[1].split(':').str[0].astype(int)
    dep_min=features[1].split(':').str[1].astype(int)
    Arrival_hour=features[2].split(':').str[0].astype(int)
    Arrival_min=features[2].split(':').str[1].astype(int)
    duration=features[3].astype(int)
    Airline=All_Airlines[features[4]]
    Source=All_Sources[features[5]]
    Destination=All_Destination[features[6]]
    Additional_info=All_Additional_info[features[7]]


    