import pandas as pd

rankings_file_path = "../../data/Daily_Ranking.csv"
output_folder_path = "output_song_data"

df = pd.read_csv(rankings_file_path);
particular_song_name = "Shape of You"

song_d = df[df["Track Name"] == particular_song_name]
# song_d = song_d[song_d["Position"] < 50]
song_d["Inv_Pos"] = 200 - song_d["Position"]
new_song_d = song_d.drop(columns=['Track Name', 'Artist', 'URL'])
new_song_d.to_csv("{}/test.csv".format(output_folder_path),index=False)
