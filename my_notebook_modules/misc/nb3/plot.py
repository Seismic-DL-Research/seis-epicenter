import matplotlib.pyplot as plt
import tensorflow.math as tfm
import seaborn as sns
import numpy as np
import scipy

def heatmap(analysis_matrix__):
  f, ax = plt.subplots(ncols=2, figsize=(12,5))
  sns.heatmap(analysis_matrix__[:,:,0],
              cmap='coolwarm',
              annot=True,
              xticklabels=['min', 'max', 'avg', 'std'],
              yticklabels=['min', 'max', 'avg', 'std'],
              linecolor='black',
              linewidths='0.05',
              ax=ax[0],
              square=True,
              fmt='.05f')
  sns.heatmap(analysis_matrix__[:,:,1],
              cmap='coolwarm',
              annot=True,
              xticklabels=['min', 'max', 'avg', 'std'],
              yticklabels=['min', 'max', 'avg', 'std'],
              linecolor='black',
              linewidths='0.05',
              square=True,
              ax=ax[1],
              fmt='.05f')
  ax[0].set_title('Real Values Matrix')
  ax[1].set_title('Imaginary Values Matrix')
  plt.show()

def distance_dist(distances__, bins__):
  f, ax = plt.subplots(ncols=2, figsize=(12,5))
  b = scipy.stats.gaussian_kde(distances__)
  plt.tight_layout(pad=3)

  x = np.arange(0, 300, .1)
  xtick = np.arange(0, 300, 25)
  ax[0].set_title('Histogram')
  ax[0].hist(distances__, bins=bins__, color='black')
  ax[0].set_ylabel('Frequency')

  max_dist = tfm.reduce_max(distances__)
  min_dist = tfm.reduce_min(distances__)
  h_length = (max_dist - min_dist) / bins__

  text_info = f'Max Distance: {max_dist:.2f} km\n'
  text_info += f'Min Distance: {min_dist:.2f} km\n'
  text_info += f'Hist Length: {h_length:.2f} km'

  ax[0].text(0.95, 0.95, text_info, 
             va='top', ha='right',
             transform=ax[0].transAxes)
  ax[1].set_title('KDE Dist.')
  ax[0].set_xlabel('Distances')
  ax[0].set_xticks(xtick)
  ax[1].plot(x, b(x), color='black', label='KDE graph of distance distribution')
  ax[1].axvline(tfm.reduce_mean(distances__), color='red', label='Mean')
  ax[1].set_ylabel('Density')
  ax[1].set_xlabel('Distances')
  ax[1].legend()

  plt.show()

def real_imag_min_max(stats__):
  f, ax = plt.subplots(ncols=2, figsize=(12,5))
  plt.tight_layout(pad=3)
  ax[0].set_xlim(-10,10)
  ax[1].set_xlim(-10,10)
  ax[0].set_xlabel('Real Numbers')
  ax[1].set_xlabel('Imag Numbers')
  ax[0].set_ylabel('Frequency')
  ax[1].set_ylabel('Frequency')
  ax[0].set_title('Real Values Dist.')
  ax[1].set_title('Imag Values Dist.')
  ax[0].hist(stats__['max'][0,:], bins=250, color='red', label='max dist.')
  ax[0].hist(stats__['min'][0,:], bins=250, color='blue', label='min dist.')
  ax[0].legend()
  ax[1].hist(stats__['max'][1,:], bins=250, color='red', label='max dist.')
  ax[1].hist(stats__['min'][1,:], bins=250, color='blue', label='min dist.')
  ax[1].legend()
  plt.show()