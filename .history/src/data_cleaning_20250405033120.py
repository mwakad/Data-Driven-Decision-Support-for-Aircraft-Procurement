import pandas as pd
import numpy as np

def clean_data(df):
    """Cleans and preprocesses the DataFrame."""
    df = df.drop_duplicates()
    df['Event.Date'] = pd.to_datetime(df['Event.Date'])
    df = df[(df['Event.Date'].dt.year >= 2000) & (df['Event.Date'].dt.year <= 2023)]
    df = df.set_index('Event.Date')
    # Filling in missing values for float dtype columns  
    columns_to_drop = ['Event.Id', 'Latitude', 'Longitude', 'Airport.Code', 'Airport.Name', 'Aircraft.Category', 'Registration.Number', 'FAR.Description', 'Schedule', 'Air.carrier', 'Publication.Date', 'Injury.Severity', 'Report.Status', 'Broad.phase.of.flight', 'Amateur.Built','Accident.Number']
    df = df.drop(columns=columns_to_drop)
    df = df.dropna(subset=['Location', 'Aircraft.damage', 'Make', 'Model', 'Number.of.Engines', 'Engine.Type', 'Purpose.of.flight', 'Weather.Condition'])
    columns_to_check = ['Total.Fatal.Injuries', 'Total.Serious.Injuries', 'Total.Minor.Injuries', 'Total.Uninjured']
    for col in columns_to_check:
        df[col] = df[col].fillna(df[col].median())
    df = df[df['Aircraft.damage'].apply(lambda which_damage: which_damage != 'Unknown')]
    df = df[df['Engine.Type'].apply(lambda drop_unknown: (drop_unknown != 'Unknown') & (drop_unknown != 'UNK')& (drop_unknown != 'NONE')& (drop_unknown != 'LR'))]
    df = df[df['Purpose.of.flight'].apply(lambda niche: niche in ['Aerial Application', 'Business', 'Executive/corporate'])]
    df = df[df['Weather.Condition'].apply(lambda drop_unknown: (drop_unknown != 'Unk') & (drop_unknown != 'UNK'))]
    # using the str upper and str.strip methods to clean the make column
    df['Make'] = df['Make'].str.upper().str.strip()
    df = df[df['Country'].apply(lambda which_country: which_country == 'United States')]
    df['Abbreviation'] = df['Location'].apply(lambda x: x.split(', ')[-1] if isinstance(x, str) and ', ' in x else None)
    df['Location'] = df['Location'].apply(lambda x: x.split(', ')[0] if isinstance(x, str) and ', ' in x else x)
    abbreviation_col = df.pop('Abbreviation')
    df.insert(df.columns.get_loc('Location') + 1, 'Abbreviation', abbreviation_col)
    df = df.dropna(subset=['Abbreviation'])
    df['Investigation.Type'] = df['Investigation.Type'].astype('category')
    df['Aircraft.damage'] = df['Aircraft.damage'].astype('category')
    df['Number.of.Engines'] = df['Number.of.Engines'].astype(str)
    df['Engine.Type'] = df['Engine.Type'].astype('category')
    df['Purpose.of.flight'] = df['Purpose.of.flight'].astype('category')
    df['Weather.Condition'] = df['Weather.Condition'].astype('category')
    return df