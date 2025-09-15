days = int(input("Enter how many days weather report u want"))
np.random.seed(42)
temp = np.random.normal(loc= 30,scale=5,size = days).round(2)
print("Temperatures",temp)
print()
# Calculate statistical measures such as minimum, maximum, and average temperature to understand overall weather conditions.
option = input("Select specific metric type 'min' or 'max' or 'avg' ")
print()
if(option == 'min'):
    print(f'Minimum Temperature in {days} days in the city :{np.min(temp)} {chr(176)}C ')
elif option =='max':
    print(f'Maxmimum Temperature in {days} days in the city : {np.max(temp)} {chr(176)}C')
elif option == 'avg':
    print(f'Average Temperaturein {days} days in the city :{np.mean(temp).round(2)} {chr(176)}C')
else:
    print("select in the provided range only")
print()
# Detect anomalies (outliers) in temperature readings using the Interquartile Range (IQR) method.
anom = input(f"Enter Yes if you want to know the temp anomalies in these {days} days")
print()
if(anom.lower() == 'yes'):
    Q1 = np.percentile(temp,25)
    Q3= np.percentile(temp,75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5*IQR
    upper_limit = Q3 + 1.5*IQR
    
    iqr_anomalies = temp[(temp<lower_limit )|( temp>upper_limit)]
    
    # Step 3b: Detect anomalies using Z-score
    z_scores = (temp-np.mean(temp))/np.std(temp)
    z_anomalies= temp[np.abs(z_scores)>2]
    coldest_temp = np.inf
    hottest_temp = -np.inf
    hottest=[]
    coldest=[]
    hot_day = 0
    cold_day = 0
    if(len(z_anomalies)>0):
        for val in z_anomalies:
            day = np.where(temp == val)[0][0] + 1
            if(val>np.mean(temp)):
                if(val>hottest_temp):
                    hottest_temp = val
                    hot_day = day
                hottest.append(val)
                # print(f"Hottest temperature in these {days} days is on Day {day} : {val} {chr(176)}C")
            else:
                 if(val<coldest_temp):
                    coldest_temp = val
                    cold_day = day
                 coldest.append(val)
                # print(f"coldest temperature in these {days} days is on Day {day} : {val} {chr(176)}C")
        if(hottest_temp != 0 ):
            print(f"Hottest temperature in these {days} days is on Day {hot_day} : {hottest_temp} {chr(176)}C")
            print("Hottest temperatures recorded were")
            for t in hottest:
                print(f"{t:.2f}{chr(176)}C")
        else:
            print('All days have moderate temperature not too hot ')
        print()
        if(coldest_temp != 100):
            print(f"coldest temperature in these {days} days is on Day {cold_day} : {coldest_temp} {chr(176)}C")
            print("Coldest temperatures recorded were")
            for t in coldest:
                print(f"{t:.2f}{chr(176)}C")
        else:
            print('All days have moderate temperature not too cold')
    elif(len(iqr_anomalies)>0):
         for val in iqr_anomalies:
            day = np.where(temp == val)[0][0] + 1
            if(val>np.mean(temp)):
                if(val>hottest_temp):
                    hottest_temp = val
                    hot_day = day
                hottest.append(val)
                # print(f"Hottest temperature in these {days} days is on Day {day} : {val} {chr(176)}C")
            else:
                 if(val<coldest_temp):
                    coldest_temp = val
                    cold_day = day
                 coldest.append(val)
                # print(f"coldest temperature in these {days} days is on Day {day} : {val} {chr(176)}C")
         if(hottest_temp != 0 ):
            print(f"Hottest temperature in these {days} days is on Day {hot_day} : {hottest_temp} {chr(176)}C")
            print("Hottest temperatures recorded were")
            for t in hottest:
                print(f"{t:.2f}{chr(176)}C")
         else:
            print('All days have moderate temperature not too hot ')
         print()
         if(coldest_temp != 100):
            print(f"coldest temperature in these {days} days is on Day {cold_day} : {coldest_temp} {chr(176)}C")
            print("Coldest temperatures recorded were")
            for t in coldest:
                print(f"{t:.2f}{chr(176)}C")
         else:
            print('All days have moderate temperature not too cold')
    #     for val in iqr_anomalies:
    #         day = np.where(temp == val)[0][0] + 1
    #         if(val>np.mean(temp)):
    #             print(f"Hottest temperature in these {days} days is on Day {day}: {val} {chr(176)}C")
                
    #         else:
    #             print(f"coldest temperature in these {days} days is on Day {day} : {val} {chr(176)}C")
    else:
        print('All days have moderate temperature not too hot or cold')
else:
    print("Thank you")
