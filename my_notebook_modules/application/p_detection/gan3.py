import tensorflow as tf

@tf.keras.utils.register_keras_serializable(
    package="thesis-gan",
    name="SplitLayer"
)
class SplitLayer(tf.keras.Layer):
  def __init__(sf):
    super(SplitLayer, sf).__init__()

  def build(sf, input_shape__):
    pass

  def call(sf, inputs__):
    # inputs__: N x H x C
    split_tensor = tf.split(inputs__, num_or_size_splits=3, axis=2)
    return split_tensor
  
def INTERNAL_G():
  tf.random.set_seed(6969)
  def functional_model():
    input = tf.keras.Input(shape=(50,1))
    x = tf.keras.layers.BatchNormalization()(input)
    x = tf.keras.layers.Conv1DTranspose(filters=11, kernel_size=32, name='conv1d_transpose1')(x)
    x = tf.keras.layers.AveragePooling1D(pool_size=2, name='avgpool1d1')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Conv1DTranspose(filters=5, kernel_size=64, name='conv1d_transpose2')(x)
    x = tf.keras.layers.AveragePooling1D(pool_size=2, name='avgpool1d2')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Flatten(name='flatten1')(x)
    x = tf.keras.layers.Dense(300, activation='leaky_relu', name='dense1')(x)
    x = tf.keras.layers.Dense(400, activation='leaky_relu', name='dense2')(x)
    x = tf.keras.layers.Dense(350, activation='tanh', name='dense3')(x)
    x = tf.keras.layers.Reshape((350, 1))(x)
    return tf.keras.Model(inputs=input, outputs=x)

  func_model = functional_model()

  init_inputs = tf.keras.Input(shape=(50,3))
  inputs = SplitLayer()(init_inputs)

  ud_output = func_model(inputs[0])
  ew_output = func_model(inputs[1])
  ns_output = func_model(inputs[2])

  out = tf.keras.layers.Concatenate(axis=-1)([ud_output, ew_output, ns_output])

  return tf.keras.Model(inputs=[init_inputs], outputs=[out], name='generator_model')

def INTERNAL_D():
  tf.random.set_seed(6969)
  def functional_model():
    input = tf.keras.Input(shape=(350,1))
    x = tf.keras.layers.BatchNormalization()(input)
    x = tf.keras.layers.Conv1D(filters=10, kernel_size=10, name='conv1d1')(x)
    x = tf.keras.layers.AveragePooling1D(pool_size=2, name='avgpool1d1')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Conv1D(filters=3, kernel_size=40, name='conv1d2')(x)
    x = tf.keras.layers.Flatten(name='flatten1')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dense(300, activation='leaky_relu', name='dense1')(x)
    x = tf.keras.layers.Dense(200, activation='leaky_relu', name='dense2')(x)
    x = tf.keras.layers.Dense(50, activation='leaky_relu', name='dense3')(x)
    x = tf.keras.layers.Dense(5, activation='sigmoid', name='dense4')(x)
    return tf.keras.Model(inputs=input, outputs=x)


  func_model = functional_model()

  init_inputs = tf.keras.Input(shape=(350,3))
  inputs = SplitLayer()(init_inputs)

  ud_output = func_model(inputs[0])
  ew_output = func_model(inputs[1])
  ns_output = func_model(inputs[2])

  out = tf.keras.layers.Concatenate(axis=-1)([ud_output, ew_output, ns_output])
  out = tf.keras.layers.Dense(1, activation='sigmoid')(out)

  return tf.keras.Model(inputs=[init_inputs], outputs=[out], name='discriminator_model')

def gan3():
  model_loc = 'seis-deep-learning/my_notebook_modules/application/p_detection/keras/&.keras'
  gModel = INTERNAL_G()
  dModel = INTERNAL_D()
  
  gModel.load_weights(model_loc.replace('&', 'gan3_g'))
  dModel.load_weights(model_loc.replace('&', 'gan3_d'))
  return gModel, dModel