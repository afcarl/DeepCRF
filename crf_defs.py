from model_Defs import *

# takes features and outputs potentials
def potentials_layer(in_layer, config, params, reuse=False, name='Potentials'):
    pot_size = config.n_tags ** config.pot_window
    out_shape = [batch_size, num_steps] + [config.n_tags] * config.pot_window
    batch_size = int(in_layer.get_shape()[0])
    num_steps = int(in_layer.get_shape()[1])
    input_size = int(in_layer.get_shape()[2])
    if reuse:
        tf.get_variable_scope().reuse_variables()
        W_pot = params.W_pot
        b_pot = params.b_pot
    else:
        W_pot = weight_variable([input_size, pot_size], name=name)
        b_pot = bias_variable([pot_size], name=name)
    flat_input = tf.reshape(in_layer, [-1, input_size])
    pre_scores = tf.matmul(flat_input, W_pot) + b_pot
    pots_layer = tf.reshape(pre_scores, [batch_size, num_steps, out_shape])
    return (pots_layer, W_pot, b_pot)


# pseudo-likelihood criterion
def pseudo_likelihood(potentials, config, params):
    batch_size = int(potentials.get_shape()[0])
    num_steps = int(potentials.get_shape()[1])
    pots_shape = int(potentials.get_shape()[2:])
    pot_indices = tf.placeholder(tf.int32, [batch_size * num_steps])
    targets = tf.placeholder(tf.float32, [batch_size, num_steps, config.n_tags])
    flat_pots = tf.reshape(potentials, [-1, config.n_tags])
    flat_cond = tf.gather(flat_pots, pot_indices)
    pre_cond = tf.nn.softmax(flat_cond)
    conditional = tf.reshape(pre_cond, [batch_size, num_steps, -1])
    pseudo_ll = -tf.reduce_sum(targets * tf.log(conditional))
    for feat in config.l1_list:
        pseudo_ll += config.l1_reg * \
                     tf.reduce_sum(tf.abs(params.embeddings[feat]))
    return (pots_indices, targets, pseudo_ll)


# max a posteriori tags assignment
def map_tags(potentials, config, params):
    batch_size = int(potentials.get_shape()[0])
    num_steps = int(potentials.get_shape()[1])
    pots_shape = int(potentials.get_shape()[2:])


def log_partition(potentials, config, params):
    batch_size = int(potentials.get_shape()[0])
    num_steps = int(potentials.get_shape()[1])
    pots_shape = int(potentials.get_shape()[2:])


def marginals(potentials, config, params):
    batch_size = int(potentials.get_shape()[0])
    num_steps = int(potentials.get_shape()[1])
    pots_shape = int(potentials.get_shape()[2:])

