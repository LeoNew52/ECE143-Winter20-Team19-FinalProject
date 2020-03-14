from functions.poverty_calculations import count_data, plot_county_accident_rates,get_county_fips_code

def get_poverty_plots_demo(fname):
    df_pov=plot_county_accident_rates(fname)
    n_vehicles={'ALAMEDA': 1370115, 'ALPINE': 3264, 'AMADOR': 60090, 'BUTTE': 228105, 'CALAVERAS': 79159, 'COLUSA': 30711, 'CONTRA COSTA': 1115734, 'DEL NORTE': 28336, 'EL DORADO': 237553, 'FRESNO': 861046, 'GLENN': 38940, 'HUMBOLDT': 154008, 'IMPERIAL': 206223, 'INYO': 28500, 'KERN': 784942, 'KINGS': 119084, 'LAKE': 90898, 'LASSEN': 36631, 'LOS ANGELES': 8154560, 'MADERA': 150284, 'MARIN': 249524, 'MARIPOSA': 28989, 'MENDOCINO': 118908, 'MERCED': 244340, 'MODOC': 13763, 'MONO': 17918, 'MONTEREY': 408110, 'NAPA': 151094, 'NEVADA': 134753, 'ORANGE': 2943942, 'PLACER': 453466, 'PLUMAS': 33937, 'RIVERSIDE': 2113938, 'SACRAMENTO': 1357361, 'SAN BENITO': 69873, 'SAN BERNARDINO': 1937675, 'SAN DIEGO': 3046126, 'SAN FRANCISCO': 492336, 'SAN JOAQUIN': 707694, 'SAN LUIS OBISPO': 316758, 'SAN MATEO': 780898, 'SANTA BARBARA': 414334, 'SANTA CLARA': 1719914, 'SANTA CRUZ': 266643, 'SHASTA': 220710, 'SIERRA': 5689, 'SISKIYOU': 66278, 'SOLANO': 438507, 'SONOMA': 541806, 'STANISLAUS': 525565, 'SUTTER': 109477, 'TEHAMA': 77616, 'TRINITY': 19767, 'TULARE': 413682, 'TUOLUMNE': 80510, 'VENTURA': 828885, 'YOLO': 192840, 'YUBA': 75066}
    import addfips
    af=addfips.AddFIPS()
    n_vehicle_fips={}
    for i in range(len(n_vehicles)):
        fips=af.get_county_fips(list(n_vehicles.keys())[i], 'CA')
        n_vehicle_fips[fips]=list(n_vehicles.values())[i]
    df_vehicle=pd.DataFrame({'FIPS Code':list(n_vehicle_fips.keys()),'Number of Vehicles':list(n_vehicle_fips.values())})
    df_vehicle=pd.merge(df_pov,df_vehicle)
    fipss=count_data(get_county_fips_code(fname, 17, 16))
    temp_df=pd.DataFrame({'FIPS Code':list(fipss.keys()),'Accident Total':list(fipss.values())})
    df_vehicle=pd.merge(df_vehicle,temp_df)
    df_vehicle['Accident per Vehicle']=df_vehicle.apply(lambda df:df['Accident Total']/df['Number of Vehicles'],axis=1)
    poverty_scatter=sns.regplot('Poverty Percent, All Ages','Accident per Vehicle',data=df_vehicle,
                                scatter_kws={'alpha':.75},line_kws={"color": "red"},ci=95,
                                label='big')
    poverty_scatter.set_title('California')
    poverty_scatter.set_ylabel(ylabel='Accident \n per Vehicle',rotation=0,y=1.08)
    
