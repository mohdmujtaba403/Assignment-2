import os
import pandas as pd
from glob import glob

season_temps = {'Summer': [], 'Autumn': [], 'Winter': [], 'Spring': []}
station_data = {}

path_of_dataset =r'C:\Users\Dell\Downloads\HIT137 Assignment 2 S1 2025 (4)\temperature_data'
path=os.path.join(path_of_dataset,'*')
csv_files = glob(path)

for filepath in csv_files:
    
        # real csv files
        my_dataset = pd.read_csv(filepath)
        
        # Station name column
        station_column = 'STATION_NAME'
        
        if not station_column:
            print(f"It didn't find station name column in {filepath}")
            continue
            
        # process each row

        for _, row in my_dataset.iterrows():
            station_name = row[station_column]
            
            # Process monthly temperatures dataset in this way
            months_dataset = {
                'January': 1, 'February': 2, 'March': 3, 'April': 4,
                'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11, 'December': 12
            }
            
            for month_name, month_num in months_dataset.items():
                if month_name in my_dataset.columns:
                    
                        temp = float(row[month_name])
                        
                        # setting by season
                        if month_num in [12, 1, 2]:
                            season_temps['Summer'].append(temp)
                        elif month_num in [3, 4, 5]:
                            season_temps['Autumn'].append(temp)
                        elif month_num in [6, 7, 8]:
                            season_temps['Winter'].append(temp)
                        else:
                            season_temps['Spring'].append(temp)
                            
                        # check the station data
                        if station_name not in station_data:
                            station_data[station_name] = {
                                'temps': [temp],
                                'min': temp,
                                'max': temp
                            }
                        else:
                            station_data[station_name]['temps'].append(temp)
                            if temp < station_data[station_name]['min']:
                                station_data[station_name]['min'] = temp
                            if temp > station_data[station_name]['max']:
                                station_data[station_name]['max'] = temp
                  

# saving all results 
def save_results(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# Seasonal averages values
season_average_value = "\n".join([f"{season}: {sum(temps)/len(temps):.1f}°C" 
                       for season, temps in season_temps.items() if temps])
save_results('average_temp.txt', f"Average Temperatures by Season:\n{season_average_value}")

# Largest temperature range values
if station_data:
    max_range = max(data['max'] - data['min'] for data in station_data.values())
    max_stations = [s for s, data in station_data.items() 
                   if data['max'] - data['min'] == max_range]
    save_results('largest_temp_range_station.txt', 
                f"Stations with largest range ({max_range:.1f}°C):\n" + "\n".join(max_stations))

    # Warmest and coolest stations
    avg_temps = {s: sum(data['temps'])/len(data['temps']) for s, data in station_data.items()}
    warmest_values = max(avg_temps.values())
    coolest__values = min(avg_temps.values())
    warm_stations = [f"{s} ({t:.1f}°C)" for s, t in avg_temps.items() if t == warmest_values]
    cool_stations = [f"{s} ({t:.1f}°C)" for s, t in avg_temps.items() if t == coolest__values]
    
    save_results(r'C:\Users\Dell\Downloads\HIT137 Assignment 2 S1 2025 (4)\temperature_data\warmest_and_coolest_station.txt',
               "Warmest Stations is:\n" + "\n".join(warm_stations) +
               "\n\nCoolest Stations is : \n" + "\n".join(cool_stations))

print("Done ")