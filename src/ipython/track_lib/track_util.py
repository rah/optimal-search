''' Track Utilities '''
import matplotlib.pyplot as plt
import pandas as pd


def summary_stats(df):
    ''' Calculate the mean and std-deviation of tracks
        Expects:
          df: dataframe: containing dict of tracks
        Returns:
          dataframe of results
    '''
    track = []
    mean_dist = []
    std_dist = []
    mean_abs_angle = []
    std_abs_angle = []

    for key in df.keys():
        track.append(key)
        mean_dist.append(df[key]['Distance'].mean())
        std_dist.append(df[key]['Distance'].std())
        mean_abs_angle.append(df[key]['Abs Angle'].mean())
        std_abs_angle.append(df[key]['Abs Angle'].std())

    summary_df = pd.DataFrame.from_items(
        [
            ('Track', track),
            ('Mean_Dist', mean_dist),
            ('Std_Dist', std_dist),
            ('Mean_Abs_Angle', mean_abs_angle),
            ('Std_Abs_Angle', std_abs_angle)
        ]
    )

    return summary_df


def plot_tracks(df):
    ''' Plot snail tracks showing track, distance moved,
        and abs angle for each time point
    '''
    dist_ylim = (0, max_distance(df))
    angle_ylim = (0, 180)

    plot_depth = 5
    n_tracks = len(df.keys())

    fig_width = 20
    fig_depth = plot_depth * n_tracks

    fig, axes = plt.subplots(
        nrows=n_tracks, ncols=3,
        figsize=(fig_width, fig_depth)
    )

    position = 0
    for key in df.keys():
        if n_tracks < 2:
            ax = df[key].plot(x='X-location.1', y='Y-location.1', ax=axes[0])
            ax.legend([key])
            df[key].plot(y='Distance', ax=axes[1], ylim=dist_ylim)
            df[key].plot(y='Abs Angle', ax=axes[2], ylim=angle_ylim)
        else:
            ax = df[key].plot(
                x='X-location.1',
                y='Y-location.1',
                ax=axes[position, 0]
            )
            ax.legend([key])
            df[key].plot(y='Distance', ax=axes[position, 1], ylim=dist_ylim)
            df[key].plot(y='Abs Angle', ax=axes[position, 2], ylim=angle_ylim)
            position = position + 1


def max_distance(df):
    ''' Calculate the max distance moved across all tracks in a set'''
    max_dist = 0

    for key in df.keys():
        md = df[key]['Distance'].max()
        if md > max_dist:
            max_dist = md

    return max_dist
