import matplotlib.pyplot as plt
import pandas as pd

def plot_safest_aircraft(df, multi_engine=False, image_path="./images/"):
    """Plots the safest aircraft based on uninjured passengers."""
    if multi_engine:
        df = df[df['Number.of.Engines'].apply(lambda x: x >= 2)]
        filename = "most-safe-multi-engine-aircraft.png"
    else:
        filename = "most-safe-aircraft.png"
    uninjured_by_make_model = df.groupby(['Make', 'Model'])['Total.Uninjured'].sum().sort_values(ascending=False).head(10)
    make_model_labels = [f"{make} - {model}" for make, model in uninjured_by_make_model.index]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(make_model_labels[::-1], uninjured_by_make_model.values[::-1])
    ax.set_title('Most Safe Aircraft Total Uninjured')
    ax.set_xlabel('Total Uninjured Passengers')
    ax.set_ylabel('Make and Model')
    fig.tight_layout()
    plt.savefig(image_path + filename, dpi=300, facecolor='white')
    plt.show()

def plot_riskiest_aircraft(df, multi_engine=False, image_path="./images/"):
    """Plots the riskiest aircraft based on fatalities."""
    if multi_engine:
        df = df[df['Number.of.Engines'].apply(lambda x: x >= 2)]
        filename = "least-safe-multi-engine-aircraft.png"
    else:
        filename = "least-safe-aircraft.png"
    Fatality_by_make_model = df.groupby(['Make', 'Model'])['Total.Fatal.Injuries'].sum().sort_values(ascending=False).head(10)
    make_model_labels = [f"{make} - {model}" for make, model in Fatality_by_make_model.index]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(make_model_labels[::-1], Fatality_by_make_model.values[::-1], color='coral')
    ax.set_title('Least Safe Aircraft by Total Fatalities')
    ax.set_xlabel('Total Fatalities')
    ax.set_ylabel('Make and Model')
    fig.tight_layout()
    plt.savefig(image_path + filename, dpi=300, facecolor='white')
    plt.show()

def plot_recommended_aircraft(df, multi_engine=False, image_path="./images/"):
    """Plots the recommended aircraft for each purpose of flight."""
    if multi_engine:
        df = df[df['Number.of.Engines'].apply(lambda x: x >= 2)]
        filename = "recommended-multi-engine-aircraft.png"
    else:
        filename = "recommended-aircraft.png"
    df_filtered = df[df['Purpose.of.flight'].isin(['Aerial Application', 'Business', 'Executive/corporate'])]
    uninjured_by_purpose_make_model = df_filtered.groupby(['Purpose.of.flight', 'Make', 'Model'])['Total.Uninjured'].sum().reset_index()
    safest_aircraft = uninjured_by_purpose_make_model.loc[uninjured_by_purpose_make_model.groupby('Purpose.of.flight')['Total.Uninjured'].idxmax()]
    safest_aircraft['Make - Model'] = safest_aircraft['Make'] + ' - ' + safest_aircraft['Model']
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    bars = ax.bar(safest_aircraft['Purpose.of.flight'], safest_aircraft['Total.Uninjured'], color=colors)
    legend_labels = safest_aircraft['Make - Model'].tolist()
    ax.legend(bars, legend_labels, title="Safest Aircraft")
    ax.set_title('Recommended Aircraft')
    ax.set_xlabel('Purpose of Flight')
    ax.set_ylabel('Total Uninjured Passengers')
    fig.tight_layout()
    plt.savefig(image_path + filename, dpi=300, facecolor='white')
    plt.show()